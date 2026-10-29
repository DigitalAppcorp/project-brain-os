#!/usr/bin/env python3
"""Render an original PAZO commercial from REAL, licensed stock videos on CI."""
import json, os, re, subprocess, urllib.request, wave, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cairosvg

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"delivery"
OUT.mkdir(exist_ok=True)
W,H,FPS=720,1280,24
GREEN=(28,76,69)
CREAM=(248,246,239)
def run(c):
    subprocess.run([str(x) for x in c],check=True)
def valid(path):
    try:
        result=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","json",str(path)],capture_output=True,text=True,check=True)
        return float(json.loads(result.stdout)["format"]["duration"])>=4.1
    except Exception:return False
def download(url,path):
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 PAZO Creative Studio","Accept":"*/*"})
        with urllib.request.urlopen(req,timeout=35) as resp,open(path,"wb") as f:
            while True:
                b=resp.read(1024*1024)
                if not b:break
                f.write(b)
                if f.tell()>65000000:raise RuntimeError("source exceeds size cap")
        if valid(path):return True
    except Exception as e:print("SOURCE FAILED:",url,str(e)[:190],flush=True)
    path.unlink(missing_ok=True)
    return False
SOURCES=[
    ("Pexels Yorkshire terrier", [
        "https://videos.pexels.com/video-files/20797051/20797051-hd_1080_1920_30fps.mp4",
        "https://videos.pexels.com/video-files/20797051/20797051-hd_720_1280_30fps.mp4",
    ],"https://www.pexels.com/video/dog-20797051/", "Pexels License"),
    ("Pexels dog outside",[
        "https://videos.pexels.com/video-files/5001204/5001204-hd_1920_1080_25fps.mp4",
        "https://videos.pexels.com/video-files/5001204/5001204-hd_1280_720_25fps.mp4"
    ],"https://www.pexels.com/video/dog-chilling-on-the-outdoor-5001204/","Pexels License"),
    ("Pexels puppy in garden",[
        "https://videos.pexels.com/video-files/13588355/13588355-hd_1080_1920_25fps.mp4",
        "https://videos.pexels.com/video-files/13588355/13588355-hd_720_1280_25fps.mp4",
    ],"https://www.pexels.com/video/close-up-of-dog-13588355/","Pexels License"),
    ("Wikimedia dog POV",[
        "https://commons.wikimedia.org/wiki/Special:Redirect/file/Dog_seen_from_a_GoPro.webm",
    ],"https://commons.wikimedia.org/wiki/File:Dog_seen_from_a_GoPro.webm","CC BY 3.0 — Pablo Fuentes"),
]
videos=[]
for i,(name,urls,source,license) in enumerate(SOURCES):
    path=OUT/f"licensed_source_{i}.mp4"
    for u in urls:
        print("Trying",u,flush=True)
        if download(u,path):
            print("LOADED",name,path.stat().st_size,flush=True)
            videos.append({"path":path,"name":name,"url":source,"license":license})
            break
if len(videos)<2:
    raise RuntimeError(f"Insufficient verified real-motion stock clips: {len(videos)}. No fake slideshow or synthetic substitute.")
# permit recycling two separately trimmed excerpts of real video if only 2 downloaded
while len(videos)<3:videos.append(videos[0].copy())
fontpath="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def overlay(text,path,top=690):
    im=Image.new("RGBA",(W,H));d=ImageDraw.Draw(im)
    font=ImageFont.truetype(fontpath,49)
    words=text.split(); lines=[];line=""
    for word in words:
        trial=(line+" "+word).strip()
        if d.textbbox((0,0),trial,font=font)[2]>W-90 and line:lines.append(line);line=word
        else:line=trial
    if line:lines.append(line)
    y=top
    for line in lines:
        wd=d.textbbox((0,0),line,font=font)[2]
        d.rounded_rectangle((W/2-wd/2-22,y-10,W/2+wd/2+22,y+65),radius=18,fill=(11,41,37,215))
        d.text(((W-wd)/2,y),line,fill=CREAM,font=font)
        y+=79
    im.save(path)
texts=["They're not just pets.","They're part of our story.","Give theirs a place to live."]
parts=[]
for i in range(3):
    item=videos[i]
    png=OUT/f"text{i}.png";overlay(texts[i],png,top=730)
    out=OUT/f"part{i}.mp4"
    # Reuse excerpt at a different source moment if source repeated
    source_dur=float(json.loads(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","json",str(item["path"])],capture_output=True,text=True).stdout)["format"]["duration"])
    st=4.3 if i==2 and item["path"]==videos[0]["path"] and source_dur>9 else 0
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",st,"-i",item["path"],"-loop","1","-i",png,
         "-filter_complex",f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1[bg];[bg][1:v]overlay=0:0,format=yuv420p[out]",
         "-map","[out]","-t","4","-an","-c:v","libx264","-preset","veryfast","-crf","23","-r",str(FPS),"-pix_fmt","yuv420p",out])
    parts.append(out)
# exact geometry faithfully traced from the image supplied by the Product Owner
im=Image.new("RGB",(W,H),GREEN)
draw=ImageDraw.Draw(im)
cairosvg.svg2png(url=str(ROOT/"pazo-official-traced.svg"),write_to=str(OUT/"logo.png"),output_width=650)
logo=Image.open(OUT/"logo.png").convert("RGBA")
im.paste(logo,((W-logo.width)//2,480),logo)
f=ImageFont.truetype(fontpath,35)
for s,y in [("Your pet deserves",865),("their own space.",915)]:
    wd=draw.textbbox((0,0),s,font=f)[2];draw.text(((W-wd)//2,y),s,font=f,fill=CREAM)
f2=ImageFont.truetype(fontpath,27)
s="pazo-app.vercel.app";wd=draw.textbbox((0,0),s,font=f2)[2]
draw.text(((W-wd)//2,1030),s,font=f2,fill=(205,226,216))
im.save(OUT/"endcard.png")
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate",str(FPS),"-i",OUT/"endcard.png",
     "-t","4","-c:v","libx264","-pix_fmt","yuv420p","-r",str(FPS),OUT/"part3.mp4"])
parts.append(OUT/"part3.mp4")
(OUT/"concat.txt").write_text("".join("file '"+str(p.resolve())+"'\n" for p in parts))
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",OUT/"concat.txt","-c","copy",OUT/"silent.mp4"])
# original soundtrack from numerically synthesized chords and soft beats
sr=32000;T=16;t=np.arange(sr*T)/sr
s=np.zeros_like(t)
for freq in [146.83,185.00,220.0,293.66]:
    s+=0.014*np.sin(2*np.pi*freq*t+0.03*np.sin(2*np.pi*.14*t))
for beat in range(32):
    tau=t-beat*.5;mask=(tau>=0)&(tau<.13)
    s[mask]+=.036*np.sin(2*np.pi*90*tau[mask]*(1-2*tau[mask]))*np.exp(-30*tau[mask])
envelope=np.minimum(1,t/.4)*np.minimum(1,np.maximum(0,(16-t))/.6)
s=np.int16(np.clip(s*envelope,-1,1)*32767)
with wave.open(str(OUT/"sound.wav"),"wb") as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(s.tobytes())
video=OUT/"PAZO_The_Little_Things_Real_Footage.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",OUT/"silent.mp4","-i",OUT/"sound.wav",
     "-map","0:v","-map","1:a","-c:v","copy","-c:a","aac","-b:a","128k","-movflags","+faststart","-shortest",video])
run(["ffmpeg","-v","error","-i",video,"-f","null","-"])
(OUT/"SOURCES_AND_LICENSES.txt").write_text("\n".join(f"{x['name']} | {x['url']} | {x['license']}" for x in videos)+"\nStock footage transformed and edited for an original PAZO commercial pilot.\n")
# Evidence frames extracted from the ACTUAL rendered MP4, not mocked images.
frames=[]
for sec in (1,5,9,14):
    fn=OUT/f"frame_{sec:02}.jpg"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",str(sec),"-i",video,"-frames:v","1",fn])
    fr=Image.open(fn).convert("RGB");fr.thumbnail((360,640));frames.append(fr)
sheet=Image.new("RGB",(360*4,680),(235,234,228))
dt=ImageDraw.Draw(sheet)
for i,(sec,fr) in enumerate(zip((1,5,9,14),frames)):
    sheet.paste(fr,(i*360,0));dt.text((i*360+12,646),f"{sec:02} SEC",fill=(10,30,27))
sheet.save(OUT/"COMERCIAL_VISTA_PREVIA.jpg",quality=88)
print("SUCCESS",video,video.stat().st_size,flush=True)
