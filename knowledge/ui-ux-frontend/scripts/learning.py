"""Local, deterministic feedback ledger. Python stdlib only; no model or network."""
import argparse
from collections import defaultdict
from datetime import date
import json
import os
from pathlib import Path
import re
import sys

SCHEMA = 1
POLICY = "contextual-v1"
WEIGHTS = {"APPROVED": 2, "REJECTED": -2, "CORRECTED": -1, "PARTIAL": 0, "UNVERIFIED": 0}
STAGES = {"REFERENCE", "PREVIEW", "IMPLEMENTATION", "PROCESS", "AUTHORIZATION"}
PO_SOURCES = {"PO_DIRECT", "DOCUMENTED_PO"}
SOURCES = PO_SOURCES | {"TECHNICAL", "UNKNOWN"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def iso(value):
    require(isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value), "Use YYYY-MM-DD")
    return date.fromisoformat(value)


def scope(event):
    return event["product"], event["screen"], event["component"], event["context"]


def validate(events):
    ids, aspects = {}, {}
    evidence = set()
    for event in events:
        require(isinstance(event, dict), "Event must be an object")
        require(event.get("schema_version") == SCHEMA, "Unsupported schema_version")
        eid = event.get("id")
        require(text(eid) and re.fullmatch(r"[a-zA-Z0-9_.-]+", eid), "Invalid event id")
        require(eid not in ids, f"Duplicate id: {eid}")
        require(text(event.get("product")) and event["product"] != "*", "Product must be explicit")
        when = iso(event.get("date"))
        source = event.get("source", {})
        require(isinstance(source, dict) and source.get("kind") in SOURCES and text(source.get("ref")), "Source kind/ref required")
        require(text(event.get("feedback")), "Feedback or uncertainty required")
        if event.get("kind", "feedback") == "retraction":
            target = ids.get(event.get("target"))
            require(target and target.get("kind", "feedback") == "feedback", "Retraction must target prior feedback")
            require(target["product"] == event["product"] and when >= iso(target["date"]), "Invalid retraction scope/date")
        else:
            require(event.get("kind", "feedback") == "feedback", "Unknown event kind")
            require(all(text(event.get(k)) for k in ("screen", "component")), "Screen and component required; use explicit * for broad scope")
            context = event.get("context")
            require(isinstance(context, dict) and all(text(k) and text(v) for k, v in context.items()), "Context must be a string map")
            require(event.get("stage") in STAGES, "Invalid decision stage")
            require(event.get("decision") in WEIGHTS, "Invalid decision")
            require(event.get("artifact_status") in {"AVAILABLE", "UNAVAILABLE", "NOT_CHECKED"}, "Artifact status required")
            require(text(event.get("result")), "Observed/reported result or limit required")
            items = event.get("aspects")
            require(isinstance(items, list) and items, "At least one aspect required")
            for item in items:
                require(isinstance(item, dict), "Aspect must be an object")
                key = item.get("key")
                require(text(key) and re.fullmatch(r"[a-zA-Z0-9_.-]+", key), "Invalid aspect key")
                aid = f"{eid}#{key}"
                require(aid not in aspects, "Duplicate aspect key")
                require(all(text(item.get(k)) for k in ("pattern", "dimension", "lesson")), "Pattern, dimension and lesson required")
                status = item.get("status")
                require(status in WEIGHTS, "Invalid aspect status")
                if status in {"APPROVED", "REJECTED", "CORRECTED"}:
                    require(source["kind"] in PO_SOURCES, "Technical/unknown evidence cannot confer a PO verdict")
                if event["decision"] != "PARTIAL":
                    require(status == event["decision"], "Mixed verdicts require decision PARTIAL")
                targets = item.get("supersedes", [])
                require(isinstance(targets, list) and all(isinstance(t, str) for t in targets), "Supersedes must be aspect refs")
                for target_id in targets:
                    require(status in {"APPROVED", "REJECTED", "CORRECTED"}, "Unverified/partial aspects cannot supersede a decision")
                    require(target_id in aspects, f"Unknown/forward supersession: {target_id}")
                    prior_event, prior_item = aspects[target_id]
                    require(scope(prior_event) == scope(event) and prior_item["dimension"] == item["dimension"], "Supersession must retain product/screen/component/context/dimension")
                    require(when >= iso(prior_event["date"]), "Supersession cannot predate target")
                    require(source["kind"] in PO_SOURCES, "Supersession requires documented PO decision")
                require(isinstance(item.get("process_issue", ""), str), "process_issue must be a string")
                aspects[aid] = event, item
            if "valid_until" in event:
                require(iso(event["valid_until"]) >= when, "Expiry cannot predate event")
            signature = json.dumps([scope(event), event["stage"], source["ref"], event["feedback"],
                                    [(i["pattern"], i["dimension"], i["status"]) for i in items]], sort_keys=True)
            require(signature not in evidence, "Duplicate feedback evidence; do not reward a replay")
            evidence.add(signature)
        ids[eid] = event
    return aspects


def load(store):
    store = Path(store)
    require(store.is_file(), f"Store not found: {store}; initialize explicitly")
    events = [json.loads(line) for line in store.read_text(encoding="utf-8").splitlines() if line.strip()]
    validate(events)
    return events


def record(store, incoming):
    """Validate the whole batch, atomically replace ledger, refuse concurrent writes."""
    store = Path(store)
    lock = store.with_name(store.name + ".lock")
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    temp = store.with_name(store.name + ".pending")
    try:
        events = load(store)
        by_id = {event["id"]: event for event in events}
        added = []
        for event in incoming:
            require(isinstance(event, dict), "Event must be an object")
            if event.get("id") in by_id:
                require(by_id[event["id"]] == event, "Conflicting event id; append a correction or retraction")
                continue
            added.append(event)
            by_id[event.get("id")] = event
        validate(events + added)
        if added:
            with temp.open("x", encoding="utf-8", newline="\n") as stream:
                for event in events + added:
                    stream.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temp, store)
        return {"added": len(added), "total": len(events) + len(added)}
    finally:
        os.close(fd)
        lock.unlink()
        # A leftover .pending after interruption is preserved for explicit recovery.


def active(events, as_of):
    events = [e for e in events if iso(e["date"]) <= iso(as_of)]
    all_aspects = validate(events)
    retracted = {e["target"] for e in events if e.get("kind") == "retraction"}
    candidates = {aid: pair for aid, pair in all_aspects.items() if pair[0]["id"] not in retracted}
    superseded = set()

    def disable(aid):
        if aid in superseded:
            return
        superseded.add(aid)
        for older in all_aspects[aid][1].get("supersedes", []):
            disable(older)

    for event, item in candidates.values():
        for target in item.get("supersedes", []):
            disable(target)
    return {aid: pair for aid, pair in candidates.items()
            if aid not in superseded and pair[0].get("valid_until", "9999-12-31") >= as_of}, retracted, superseded


def query(events, product, screen, component, context, as_of):
    current, _, _ = active(events, as_of)
    groups = {}
    for aid, (event, item) in current.items():
        if event["product"] != product or event["screen"] not in (screen, "*") or event["component"] not in (component, "*"):
            continue
        if not all(context.get(k) == v for k, v in event["context"].items()):
            continue
        specificity = (1 if event["screen"] != "*" else .5) * (1 if event["component"] != "*" else .5)
        delta = WEIGHTS[item["status"]] * specificity
        if event["stage"] == "AUTHORIZATION":
            delta = 0  # Historical permission never authorizes current operations.
        key = item["dimension"], item["pattern"]
        group = groups.setdefault(key, {"dimension": key[0], "pattern": key[1], "raw_score": 0, "evidence": []})
        group["raw_score"] += delta
        group["evidence"].append({"aspect": aid, "date": event["date"], "status": item["status"],
                                  "stage": event["stage"], "source": event["source"], "delta": delta,
                                  "lesson": item["lesson"], "artifact_status": event["artifact_status"], "result": event["result"]})
    ranked = []
    for group in groups.values():
        group["score"] = max(-6, min(6, group["raw_score"]))
        ranked.append(group)
    return {"schema_version": SCHEMA, "policy": POLICY, "product": product, "as_of": as_of,
            "patterns": sorted(ranked, key=lambda g: (-g["score"], g["dimension"], g["pattern"])),
            "notice": "Heuristic priorities, not probabilities or authorization; retain gates and explore when appropriate."}


def audit(events, product, as_of):
    # Filter product AFTER validating references within the complete ledger.
    current, retracted, superseded = active(events, as_of)
    issues = defaultdict(set)
    historical = validate([e for e in events if iso(e["date"]) <= iso(as_of)])
    for event, item in historical.values():
        if event["id"] in retracted:
            continue
        if event["product"] == product and item["status"] in {"REJECTED", "CORRECTED"} and item.get("process_issue"):
            issues[item["process_issue"]].add(event["id"])
    own_ids = {e["id"] for e in events if e["product"] == product}
    return {"product": product, "policy": POLICY, "events": len(own_ids),
            "active_aspects": [aid for aid, (e, _) in current.items() if e["product"] == product],
            "retracted_events": sorted(retracted & own_ids),
            "superseded_aspects": sorted(aid for aid in superseded if aid.split("#")[0] in own_ids),
            "process_issues": [{"issue": issue, "count": len(ids), "recurring": len(ids) >= 2, "events": sorted(ids)}
                               for issue, ids in sorted(issues.items())]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["init", "record", "query", "audit"])
    parser.add_argument("--store", required=True)
    parser.add_argument("--input", help="JSON object or array; - reads stdin")
    parser.add_argument("--product")
    parser.add_argument("--screen")
    parser.add_argument("--component")
    parser.add_argument("--context", default="{}", help="JSON string map")
    parser.add_argument("--as-of", help="Explicit local decision date YYYY-MM-DD")
    args = parser.parse_args(argv)
    if args.command == "init":
        path = Path(args.store)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8"):
            pass
        result = {"initialized": str(path), "schema_version": SCHEMA}
    elif args.command == "record":
        require(args.input, "record requires --input FILE or -")
        incoming = json.loads(sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8"))
        result = record(args.store, incoming if isinstance(incoming, list) else [incoming])
    else:
        require(args.product and args.as_of, "query/audit require --product and --as-of")
        iso(args.as_of)
        events = load(args.store)
        if args.command == "query":
            require(args.screen and args.component and args.screen != "*" and args.component != "*", "Query must name a screen and component")
            context = json.loads(args.context)
            require(isinstance(context, dict) and all(text(k) and text(v) for k, v in context.items()), "Invalid query context")
            result = query(events, args.product, args.screen, args.component, context, args.as_of)
        else:
            result = audit(events, args.product, args.as_of)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"learning: {error}", file=sys.stderr)
        sys.exit(1)
