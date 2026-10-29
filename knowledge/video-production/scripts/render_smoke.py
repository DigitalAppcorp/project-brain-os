#!/usr/bin/env python3
"""Smoke gratuito: still autorizado + audio opcional -> MP4 verificable.

No demuestra calidad creativa ni animación 3D. Requiere FFmpeg/ffprobe.
"""
import argparse
import json
import shutil
import subprocess
from pathlib import Path


def run(command):
    return subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--image', type=Path, required=True)
    parser.add_argument('--audio', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=4.0)
    args = parser.parse_args()
    if not args.image.is_file() or (args.audio and not args.audio.is_file()):
        parser.error('Missing input file')
    if not 2 <= args.seconds <= 15:
        parser.error('seconds must be 2..15')
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        parser.error('ffmpeg and ffprobe are required')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    d = args.seconds
    vf = ("scale=540:960:force_original_aspect_ratio=increase,"
          "crop=540:960,"
          "zoompan=z='min(zoom+0.0008,1.08)':"
          "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=540x960:fps=24,"
          f"fade=t=in:st=0:d=0.15,fade=t=out:st={d-0.25:.3f}:d=0.25")
    cmd = ['ffmpeg','-hide_banner','-loglevel','error','-y',
           '-loop','1','-framerate','24','-i',str(args.image)]
    if args.audio:
        cmd += ['-stream_loop','-1','-i',str(args.audio)]
    cmd += ['-vf',vf,'-t',str(d),'-c:v','libx264','-preset','veryfast',
            '-pix_fmt','yuv420p','-r','24']
    if args.audio:
        cmd += ['-c:a','aac','-b:a','128k','-af',
                f'afade=t=in:st=0:d=0.1,afade=t=out:st={d-0.2:.3f}:d=0.2']
    else:
        cmd += ['-an']
    cmd += ['-movflags','+faststart',str(args.output)]
    run(cmd)
    meta = json.loads(run(['ffprobe','-v','error','-show_streams','-show_format',
                           '-of','json',str(args.output)]).stdout)
    vids = [s for s in meta['streams'] if s['codec_type'] == 'video']
    auds = [s for s in meta['streams'] if s['codec_type'] == 'audio']
    if len(vids) != 1 or (vids[0]['width'],vids[0]['height']) != (540,960):
        raise RuntimeError('Video output invalid')
    if bool(auds) != bool(args.audio):
        raise RuntimeError('Audio output invalid')
    if abs(float(meta['format']['duration']) - d) > 0.11:
        raise RuntimeError('Duration mismatch')
    run(['ffmpeg','-v','error','-i',str(args.output),'-f','null','-'])
    result = {'status':'TECHNICAL_SMOKE_PASS','output':str(args.output),
              'duration_s':float(meta['format']['duration']),'resolution':'540x960',
              'video_codec':vids[0]['codec_name'],
              'audio_codec':auds[0]['codec_name'] if auds else None,
              'bytes':args.output.stat().st_size,
              'creative_qa':'NOT_CHECKED','rights_qa':'NOT_CHECKED',
              'claims_3d_or_human_ad':'NOT_VALIDATED'}
    args.output.with_suffix('.qa.json').write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))


if __name__ == '__main__':
    main()
