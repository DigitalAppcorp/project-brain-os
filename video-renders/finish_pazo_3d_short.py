#!/usr/bin/env python3
"""Post edit for actual animated Blender frames. Cinematic claims are not automatic.
Video is independently rendered 3D geometry, not image motion or stock footage.
"""
import json, math, subprocess, urllib.request, wave
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cairosvg

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"delivery"/"acting_3d"
FPS=20
W,H=480,854
def run(cmd):
    subprocess.run([str(x) for x in cmd],check=True)
def probe(path):
    return json.loads(subprocess.run(["ffprobe","-v","error","-show_format","-show_streams","-of","json",str(path)],text=True,capture_output=True,check=True).stdout)
frames=list(OUT.glob("frame_*.png"))
if len(frames)!=220:raise RuntimeError(f"Render incomplete: {len(frames)}/220 frames")
for idx in [20,86,118,163]:
    if not (OUT/f"frame_{idx:04}.png").exists():raise RuntimeError(f"Missing meaningful acting beat {idx}")
scene_movie=OUT/"acting_only.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-framerate",str(FPS),"-i",OUT/"frame_%04d.png",
     "-c:v","libx264","-preset","fast","-crf","19","-pix_fmt","yuv420p","-r",str(FPS),scene_movie])
# Closing PAZO official vector, supplied as brand reference/traced by project. No redesign.
url="https://raw.githubusercontent.com/DigitalAppcorp/project-brain-os/media/pazo-first-real-footage-ad-20261029/video-renders/pazo-official-traced.svg"
logo_svg=OUT/"pazo_brand.svg"
try:
    req=urllib.request.Request(url,headers={"User-Agent":"PAZO-local-render"})
    with urllib.request.urlopen(req,timeout=20) as r:logo_svg.write_bytes(r.read())
    cairosvg.svg2png(bytestring=logo_svg.read_bytes(),write_to=str(OUT/"brand.png"),output_width=450)
except Exception as e:
    raise RuntimeError(f"Official traced mark unavailable; refuse inaccurate brand imitation: {e}")
im=Image.new("RGB",(W,H),(24,75,66))
logo=Image.open(OUT/"brand.png").convert("RGBA")
im.paste(logo,((W-logo.width)//2,300),logo)
d=ImageDraw.Draw(im)
fontpath="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font=ImageFont.truetype(fontpath,24)
s="Their own little world."
box=d.textbbox((0,0),s,font=font)
d.text(((W-(box[2]-box[0]))/2,580),s,fill=(244,245,235),font=font)
u="pazo-app.vercel.app"
f2=ImageFont.truetype(fontpath,18)
b=d.textbbox((0,0),u,font=f2)
d.text(((W-(b[2]-b[0]))/2,640),u,fill=(206,224,207),font=f2)
im.save(OUT/"endcard.png")
end_movie=OUT/"brand_end.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate",str(FPS),
     "-i",OUT/"endcard.png","-t","1.6","-r",str(FPS),"-c:v","libx264","-crf","19","-pix_fmt","yuv420p",end_movie])
concat=OUT/"concat.txt"
concat.write_text("".join(f"file '{path.resolve()}'\n" for path in [scene_movie,end_movie]))
silent=OUT/"silent_full.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",concat,"-c","copy",silent])
duration=12.6
sr=32000
t=np.arange(int(duration*sr),dtype=np.float64)/sr
audio=np.zeros_like(t)
def fade(x,local,dur):
    return (np.clip(local/.018,0,1)*np.clip((dur-local)/.16,0,1))*x
def add_note(start,hz,dur,amp=.09,overtones=(1,2,3)):
    rel=t-start; sel=(rel>=0)&(rel<dur)
    a=np.zeros(sel.sum())
    x=rel[sel]
    for q in overtones:
        a+=(amp/q**1.5)*np.sin(2*np.pi*hz*q*x)
    audio[sel]+=a*np.exp(-x*3)*np.clip(x/.01,0,1)*np.clip((dur-x)/.07,0,1)
def add_swish(at,length=.5,amp=.095):
    rng=np.random.default_rng(44);n=int(sr*length)
    noise=rng.standard_normal(n)
    smooth=np.convolve(noise,np.ones(5)/5,mode="same")
    env=np.sin(np.linspace(0,np.pi,n))**1.8
    st=int(at*sr);audio[st:st+n]+=amp*smooth*env
def add_tap(at,pitch=130,amp=.07,length=.28):
    st=int(at*sr);n=int(sr*length);tau=np.arange(n)/sr
    tone=amp*np.sin(2*np.pi*(pitch-55*tau)*tau)*np.exp(-tau*26)
    audio[st:st+n]+=tone
# Sparse original musical motifs. Deliberate silence for the dog's 7.5-9.6s reaction.
for i,pitch in enumerate([220,246.94,196,164.81]):
    add_note(.24+i*.48,pitch,.44,.030)
add_tap(1.40,115,.045)
add_tap(3.30,180,.045)
add_note(4.56,293.66,.32,.030)
add_swish(5.03,.42,.12)  # paw/ball contact
add_tap(5.47,125,.13)
add_tap(6.07,194,.052)
add_note(7.15,146.83,.17,.018)   # leave the next beat empty
add_note(9.38,174.61,.53,.035)
add_note(10.1,196,.32,.03)
# Short brand closing arpeggio
for i,pitch in enumerate([196,246.94,293.66]):
    add_note(11.05+i*.16,pitch,1.18-i*.14,.042)
# Constrain levels without crushing dynamics.
peak=np.max(np.abs(audio))
if peak>.83:audio*=.83/peak
audio=np.int16(np.clip(audio,-1,1)*32767)
wav=OUT/"original_sound_design.wav"
with wave.open(str(wav),"wb") as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(audio.tobytes())
final=OUT/"PAZO_Acting_Test_Original_3D.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",silent,"-i",wav,"-map","0:v","-map","1:a",
     "-c:v","copy","-c:a","aac","-b:a","144k","-movflags","+faststart","-shortest",final])
run(["ffmpeg","-v","error","-i",final,"-f","null","-"])
metadata=probe(final)
stream=[x for x in metadata["streams"] if x["codec_type"]=="video"][0]
if (stream["width"],stream["height"])!=(W,H):raise RuntimeError("Wrong output resolution")
if not any(x["codec_type"]=="audio" for x in metadata["streams"]):raise RuntimeError("No audio")
# Storyboard is created from actual video frames and labels.
positions=[1.0,3.8,5.7,8.3,10.1,11.8]
sheet=Image.new("RGB",(270*len(positions),500),(249,246,237))
dd=ImageDraw.Draw(sheet)
for i,s in enumerate(positions):
    frame=OUT/f"contact_{i}.png"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",str(s),"-i",final,"-frames:v","1",frame])
    im=Image.open(frame).convert("RGB")
    im.thumbnail((270,480))
    sheet.paste(im,(i*270,0))
    dd.text((i*270+8,482),f"{s:.1f}s",fill=(26,75,65))
sheet.save(OUT/"PAZO_Acting_Test_Storyboard.jpg",quality=87)
notes=f"""PAZO — Original animated 3D performance test.
Actual Blender geometry: 2 modeled characters, independent root/head/limb/tail controls, one ball.
Scene: dog reaches for tennis ball; cat arrives, swats ball, claims it; dog reacts and blinks.
Four motivated 3D camera angles: wide setup, reach/action, cat takeover, dog's deadpan reaction.
Original synthesized sound effects/score; pause staged for the punchline.
Endcard uses PAZO brand reference, with no actual product interaction shown.
File: {final.name} / {final.stat().st_size} bytes / {metadata["format"]["duration"]} seconds / {W}x{H} / {FPS} fps.
Rights: original procedural geometry, original synthesized soundtrack, brand supplied by product owner.
Production: 3D animated experiment, NOT filmed humans, not automatically 'professional' or conversion-proven.
TECHNICAL_RENDER_VERIFIED: YES. INDEPENDENT_CREATIVE_REVIEW: PENDING. AUDIENCE_RESPONSE: UNKNOWN.
No paid AI model, subscriptions, or ads. No modification to PAZO application or customer data.
"""
(OUT/"PRODUCTION_NOTES.txt").write_text(notes,encoding="utf-8")
print("COMPLETE",str(final),final.stat().st_size,flush=True)
