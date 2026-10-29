# Video Production OS — Creative Evidence Gate (v0.2)

**Why this gate exists:** A batch can contain several technically valid MP4s with different script copy and still be **one repeated editing template**. Four concepts are not four production styles. The editor, producer and QA reviewer must inspect the **rendered media**, not infer quality from plans, successful encoding or brand compliance.

## 1. Evidence before adjectives

| Claim in client communication | Minimum evidence required |
|---|---|
| "MP4 with audio" | Probe, full decode and accessible exact link |
| "Authentic motion footage" | Inspect several frames AND source at different timecodes; record source and usage rights |
| "Story / acting" | Seen actions that create causality, reaction, timing and change — not three unrelated stock shots |
| "Dialogue" | Audible dialogue and/or clearly staged conversation with shot–reverse-shot, reactions and meaningful pause; on-screen captions alone are **not acting** |
| "Cinematic commercial" | Planned scene, subject continuity, framing, purposeful camera/light/audio, narrative resolution; arbitrary licensed clips + titles do **not** qualify |
| "Animated 3D" | Original 3D geometry/rig/physical motion demonstrated in the render, not photos with transforms or 2D overlays |
| "Product demonstration" | Real product **interaction in motion** showing an actual completed operation and correct UI; a static screenshot with copy is a product still |
| "Diverse batch" | Different audience-facing visual/narrative grammar proven by side-by-side evidence; different filenames, hooks or music are insufficient |
| "Ready for publication" | Technical PASS **and** independent creative PASS **and** factual/rights PASS **and** user authorization |
| "Successful content" | Published and observed platform signals with valid denominators, not subjective appreciation or a good-looking mockup |

Use exact, narrower language when proof is missing. Never claim full quality based solely on a ffmpeg smoke, a contact sheet or a CI green check. A reviewer must watch the complete actual clips **with and without sound**.

## 2. Hard gate before production: method feasibility

For each promised route, identify whether its defining feature can actually be produced *with today's tools and materials*.

- **Cinematic everyday scene:** actors or genuine filmed action with continuity; if only unrelated stock footage exists, **route unavailable** as pitched. Do not relabel a montage.
- **Natural humorous pet content:** recognizable situation + setup + behavioral payoff. Generic clips with captions are a rough assembly; not a constructed joke.
- **Product utility:** accurate working screen recording and performed task. A still screenshot proves a look, not a workflow.
- **3D character comedy:** rendered acting from actual original/licensed models with rights and lip/body motion. A photomontage or dialogue cards cannot substitute.
- **Human AI performance:** if human motion/face/voice looks synthetic or unreliable, switch to genuine recorded scenes with permission, not repeated regeneration by default.

If route is unavailable, **state BLOCKED honestly and request a new authorized method**. Do not quietly substitute an easier method while still counting it among the four desired distinct styles.

## 3. Creative differentiation gate for a portfolio

Build a comparison matrix **before producing full videos** and again **after rendering**. Inspect footage at 0%, 25%, 50%, 75% and end, plus shots at actual scene boundaries. Evaluate these **material dimensions**:

1. Primary screen language: real filmed actors/pets in a continuous scene, original 3D/2D acting, UGC handheld, real product operation, graphic-only explainer.
2. Story engine: situation→conflict→payoff, observation/meme, demonstration task→result, fictional character dialogue, sensory/emotional narrative.
3. Editing grammar: continuity acting; split-screen response; screen walkthrough; rapid comedic smash cuts; voice-driven documentary. Switching words over identical cuts does not change grammar.
4. Role of sound: live dialogue, voiceover, meaningful SFX, ambient/observational sound, music-only.
5. Brand reveal and actual product evidence: brand as resolution, product-first demonstration, punchline end card, subtle integrated product.
6. **Source reuse:** which stock videos, shots, default end cards, templated overlays, soundtrack and duration are repeated. Track actual IDs and visible frames. Brand consistency is exempt from style differentiation, but not the entire template.

**Block a "different formats" batch** when the primary screen language and editing grammar are substantially identical across proposed items, *even if stories, captions and titles differ*. A reviewer must explain at least **two material viewer-visible differences** beyond hook wording, song choice, pets or logo color, with explicit shots/timecodes. If not demonstrated, `DIVERSITY_NOT_DEMONSTRATED`. The threshold is a falsification check, not a guarantee of creative success.

Diversity is a **portfolio gate**, not a command to make everything visually inconsistent with the brand. Diverse audience response may still be due to many confounds, so never label this a controlled A/B test.

## 4. Creative screen test / independent veto

Before committing an entire batch:
- Render **one key 3–5-second moment** *from each fundamentally distinct technique*, with the unique acting/action/interaction. A text-on-photo test cannot validate 3D or cinematic acting.
- Watch at normal speed, **sound on and sound off** (not only inspect four still frames). Evaluate if hook, action, spatial clarity and payoff are visible.
- Have one reviewer assess it **without seeing the script, tool selection, production effort or client's initial preference**, if independent review is available. Human or PO feedback can highlight quality risks, but it is not audience performance.
- Assign `CREATIVE_PASS | CREATIVE_REVISE | CREATIVE_FAIL | NOT_EVALUATED` per clip, with specific visual evidence and blocking reasons.
- A technical render is `TECHNICAL_RENDER_VERIFIED`, **never automatically `PILOT_QA_PASS`**.
- Portfolio is `BATCH_EXPERIMENT_READY` only if technical, rights, truthful claims, creative and differentiation gates PASS, and permission to publish is separate.

**No silent substitution:** a failed 3D attempt stays blocked and must not be represented as "the 3D video" by switching to real footage + subtitles.

## 5. Evidence record / operational learning

Write a **postmortem** when promises exceed results:
- Original promised outcome and objective observed deliverables (with links and formats).
- Exact creative differences attempted versus visible differences actually delivered.
- Failed checks/why they were bypassed; resource constraints; what cannot be done yet.
- Which skills/docs and QA scripts were changed. A document update is **not model retraining** and does not certify new artistic skill or tools.
- New **regression fixtures**: a false-diverse batch that the gate must reject, a truly distinct batch that it may allow for review.
- Revision plan: work on a single exemplar with a different production method and review it against its actual target before producing variants.

**Audience data:** Once released with permission, review retention, completions, clicks, acquisition and activations. The user's liking a video, and the producer's liking it, are creative feedback; **neither makes it an audience winner**. But an objectively incomplete or misrepresented production should not be marketed as a clean experiment while waiting for data.

## 6. User-facing reporting

Show a compact factual production report:

`concept | real method seen | creative QA | rights | status | published? | evidence`

Avoid unsupported words "professional", "cinematic", "high quality", "fully animated", "original dialogue" and "four different formats". If only one method is currently deliverable, say that clearly and demonstrate it rather than selling four unsupported routes.

**Policy:** No new paid subscriptions or campaign spend without approval. Do not upload or publish low-quality batch material to product feeds or ad platforms automatically. Do not modify the application to patch a failed video production.
