#!/usr/bin/env python3
"""Edit live Playwright capture into a demo-led commercial. No fake screens."""
from pathlib import Path
import json, math, subprocess, wave
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import cairosvg

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"delivery"/"real_demo"
OUT.mkdir(parents=True,exist_ok=True)
W,H,FPS=720,1280,24
INK=(25,75,68);CREAM=(250,249,240);SUN=(230,233,63)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTREG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def run(cmd):
    subprocess.run([str(x) for x in cmd],check=True)
def probe(path):
    return json.loads(subprocess.run(["ffprobe","-v","error","-show_format","-show_streams","-of","json",str(path)],capture_output=True,text=True,check=True).stdout)
def render_text_center(d,s,y,font,color):
    width=d.textbbox((0,0),s,font=font)[2]
    d.text(((W-width)//2,y),s,font=font,fill=color)
logo_svg=ROOT/"pazo-official-traced.svg"
cairosvg.svg2png(url=str(logo_svg),write_to=str(OUT/"pazo_logo_verified.png"),output_width=600)
logo=Image.open(OUT/"pazo_logo_verified.png").convert("RGBA")
def logo_on(im,y):
    im.paste(logo,((W-logo.width)//2,y),logo)
def card(path,title_lines,footer,duration=2):
    im=Image.new("RGB",(W,H),INK)
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((60,202,660,210),radius=4,fill=SUN)
    logo_on(im,340)
    font=ImageFont.truetype(FONT,47)
    y=700
    for line in title_lines:
        render_text_center(d,line,y,font,CREAM);y+=66
    render_text_center(d,footer,1020,ImageFont.truetype(FONTREG,27),(214,231,217))
    im.save(path)
    out=path.with_suffix(".mp4")
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate",str(FPS),"-i",path,"-t",str(duration),
         "-c:v","libx264","-crf","20","-preset","veryfast","-pix_fmt","yuv420p","-r",str(FPS),out])
    return out
opening=card(OUT/"intro.png",["What does PAZO","actually do?"],"See it in action · Real app demo",1.8)
ending=card(OUT/"outro.png",["Their world.","Their own space."],"pazo-app.vercel.app",3)
bg=Image.new("RGB",(W,H),CREAM);d=ImageDraw.Draw(bg)
d.rectangle((0,0,W,75),fill=INK)
render_text_center(d,"PAZO  /  INTERACTIVE DEMO",20,ImageFont.truetype(FONT,29),CREAM)
d.rounded_rectangle((95,88,625,1210),radius=29,fill=(224,226,218))
d.rounded_rectangle((99,92,621,1206),radius=26,fill=(255,255,255))
render_text_center(d,"SAMPLE CONTENT  ·  NO REAL USER DATA",1233,ImageFont.truetype(FONTREG,20),INK)
bg.save(OUT/"frame.png")
source=OUT/"browser_real_demo.webm"
if not source.is_file():raise RuntimeError("No captured browser motion exists. Do not fabricate screenshots.")
metadata=probe(source)
duration=float(metadata["format"]["duration"])
if duration<10 or duration>60:raise RuntimeError(f"Unexpected browser capture duration {duration}")
main=OUT/"demo_captured.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-i",OUT/"frame.png","-i",source,
     "-filter_complex","[1:v]fps=24,scale=508:1099,setsar=1,format=yuva420p[ui];[0:v][ui]overlay=106:98:shortest=1,format=yuv420p[video]",
     "-map","[video]","-t",str(duration),"-c:v","libx264","-crf","20","-preset","veryfast","-pix_fmt","yuv420p","-r",str(FPS),main])
# Concatenate segments, preserving exact original browser interaction footage.
segments=[opening,main,ending]
(OUT/"edits.txt").write_text("".join("file '"+str(p.resolve())+"'\n" for p in segments))
silent=OUT/"PAZO_Demo_Actual_Complete_silent.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",OUT/"edits.txt","-c","copy",silent])
seconds=float(probe(silent)["format"]["duration"])
# Editorial ambient pulse with subtle click sounds, fully synthesized in this project.
sr=32000;t=np.arange(int(sr*seconds))/sr
audio=np.zeros_like(t)
for note in [164.81,196,246.94]:
    audio+=.008*np.sin(2*np.pi*note*t)
for at in [2.8,5.6,8.9,12.2,15.3]:
    tau=t-at
    mask=(tau>=0)&(tau<.12)
    audio[mask]+=.045*np.sin(2*np.pi*(870-250*tau[mask])*tau[mask])*np.exp(-28*tau[mask])
env=np.minimum(1,t/.4)*np.minimum(1,(seconds-t)/.6)
pcm=np.int16(np.clip(audio*env,-1,1)*32767)
with wave.open(str(OUT/"original_demo_audio.wav"),"wb") as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(pcm.tobytes())
final=OUT/"PAZO_Real_Interactive_Demo_Commercial.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",silent,"-i",OUT/"original_demo_audio.wav",
     "-c:v","copy","-c:a","aac","-b:a","128k","-map","0:v:0","-map","1:a:0","-shortest","-movflags","+faststart",final])
run(["ffmpeg","-v","error","-i",final,"-f","null","-"])
meta=probe(final)
assert meta["streams"][0]["width"]==720 and meta["streams"][0]["height"]==1280
assert any(s["codec_type"]=="audio" for s in meta["streams"])
# Frame evidence at real browser moments, not isolated screenshots.
positions=[1.0,3.8,7.2,11.0,min(seconds-3.5,16),seconds-1.0]
sheet=Image.new("RGB",(360*len(positions),680),(228,228,224))
sd=ImageDraw.Draw(sheet)
for i,sec in enumerate(positions):
    frame=OUT/f"evidence_final_{i+1}.jpg"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",str(sec),"-i",final,"-frames:v","1",frame])
    im=Image.open(frame).convert("RGB");im.thumbnail((360,640))
    sheet.paste(im,(360*i,0))
    sd.text((i*360+12,647),f"{sec:.1f} SEC",fill=INK)
sheet.save(OUT/"PAZO_Real_Demo_Storyboard.jpg",quality=88)
(OUT/"RELEASE_NOTES.txt").write_text(
    "PAZO video experiment: REAL SCREEN RECORDING of actual app Demo mode on a locally run Vite build.\\n"
    "No signup, no live Supabase writes or paid customer activity.\\n"
    "Demo content is sample-only; this is not evidence of real user engagement.\\n"
    "Scripted clicks on authentic buttons performed by Playwright. UI unchanged except recorded editorial click rings.\\n"
    "Production method: screen walkthrough from real browser recording; not stock montage and not cinematic acting.\\n"
    "Quality: technical verification and evidence frames. Independent audience response remains unknown.\\n")
print("DELIVERED",str(final),final.stat().st_size,"duration",seconds,flush=True)
