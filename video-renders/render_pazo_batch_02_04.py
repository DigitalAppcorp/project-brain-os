#!/usr/bin/env python3
"""Produce 3 original PAZO social pilots from licensed REAL animal motion and real PAZO screenshots.
Video 04 is filmed-pet dialogue, explicitly NOT 3D.
"""
import json, math, subprocess, urllib.request, wave
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import cairosvg

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"delivery"/"batch_02_04"
OUT.mkdir(parents=True,exist_ok=True)
W,H,FPS=720,1280,24
GREEN=(26,77,69)
CREAM=(252,250,241)
YELLOW=(225,229,63)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def run(cmd):
    subprocess.run([str(x) for x in cmd],check=True)
def probe(path):
    return json.loads(subprocess.run(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(path)],capture_output=True,text=True,check=True).stdout)
def get(url,path):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 PAZO-original-commercial-creative","Accept":"*/*"})
    try:
        with urllib.request.urlopen(req,timeout=33) as response,open(path,"wb") as f:
            while True:
                z=response.read(1024*1024)
                if not z:break
                f.write(z)
                if f.tell()>75000000:raise ValueError("media size limit")
        if float(probe(path)["format"]["duration"])<3.2:raise ValueError("short source")
        return True
    except Exception as ex:
        print("DOWNLOAD_FAIL",url,str(ex)[:130],flush=True)
        path.unlink(missing_ok=True);return False
def load_media(key,id,variants,src):
    path=OUT/f"stock_{key}.mp4"
    for v in variants:
        u=f"https://videos.pexels.com/video-files/{id}/{id}-{v}.mp4"
        if get(u,path):
            print("LICENSED_SOURCE",key,u,flush=True)
            SOURCES[key]={"url":src,"file_url":u,"license":"Pexels License, commercial use permitted","video_id":id}
            return path
    return None

SOURCES={}
# Use verified sources whenever a new location-specific stock download fails.
stock={}
stock["terrier"]=load_media("terrier",20797051,["hd_1080_1920_30fps","hd_720_1280_30fps"],"https://www.pexels.com/video/dog-20797051/")
stock["outdoor"]=load_media("outdoor",5001204,["hd_1920_1080_25fps","hd_1280_720_25fps"],"https://www.pexels.com/video/dog-chilling-on-the-outdoor-5001204/")
stock["garden"]=load_media("garden",13588355,["hd_1080_1920_25fps","hd_720_1280_25fps"],"https://www.pexels.com/video/close-up-of-dog-13588355/")
stock["sofa"]=load_media("sofa",5384799,["hd_1920_1080_25fps","hd_1280_720_25fps","hd_1920_1080_30fps"],"https://www.pexels.com/video/dog-sitting-on-the-sofa-5384799/")
stock["puppy"]=load_media("puppy",5877815,["hd_1080_1920_25fps","hd_720_1280_25fps","hd_1080_1920_30fps"],"https://www.pexels.com/video/puppy-running-on-the-grass-5877815/")
stock["cat"]=load_media("cat",6578983,["hd_1920_1080_25fps","hd_1280_720_25fps","hd_1920_1080_30fps"],"https://www.pexels.com/video/video-of-a-cat-looking-at-camera-6578983/")
stock["cat2"]=load_media("cat2",17029770,["hd_1080_1920_30fps","hd_1920_1080_30fps","hd_1280_720_25fps"],"https://www.pexels.com/video/a-cat-is-looking-at-the-camera-17029770/")
for key in ("terrier","outdoor","garden"):
    if stock[key] is None:raise RuntimeError("Base licensed footage disappeared: "+key)
def choose(*keys):
    for k in keys:
        if stock.get(k) is not None:return k
    return None

# Source screens: real committed UI snapshots. Do not alter component graphics or create fake UI.
BASE="https://raw.githubusercontent.com/DigitalAppcorp/pazo-app/main/"
def fetch_ui(key,path):
    target=OUT/f"actual_{key}.png"
    u=BASE+path
    request=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request,timeout=20) as response:target.write_bytes(response.read())
        im=Image.open(target);im.verify()
        return target
    except Exception as e:
        target.unlink(missing_ok=True);print("UI_ERROR",str(e)[:150]);return None
welcome=fetch_ui("welcome","docs/evidence/issue147-release-20261028/canonical/mobile_en-welcome.png")
my_pet=fetch_ui("features","docs/evidence/issue147-release-20261028/navigation/en-390-My-Pet.png")
if not (welcome and my_pet):raise RuntimeError("Cannot build product commercial without REAL Pazo screenshots")

def text_layer(text,idx,kind="caption",y=790):
    layer=Image.new("RGBA",(W,H));d=ImageDraw.Draw(layer)
    if kind=="dialogue":
        font=ImageFont.truetype(FONT,52);y=780
        bubble=(248,247,239,241);fg=(20,66,58)
    else:
        font=ImageFont.truetype(FONT,49)
        bubble=(13,51,45,221);fg=(255,255,250)
    words=text.split();lines=[];cur=""
    for word in words:
        trial=(cur+" "+word).strip()
        if d.textbbox((0,0),trial,font=font)[2]>W-110 and cur:
            lines.append(cur);cur=word
        else:cur=trial
    if cur:lines.append(cur)
    h=74*len(lines)+32;box=(31,y-20,W-31,y-20+h)
    d.rounded_rectangle(box,radius=24,fill=bubble)
    for line in lines:
        wd=d.textbbox((0,0),line,font=font)[2]
        d.text(((W-wd)/2,y),line,font=font,fill=fg)
        y+=74
    path=OUT/f"overlay_{idx}.png";layer.save(path)
    return path

def clip(key,text,idx,dur=3.5,start=0,style="caption"):
    if key is None:raise RuntimeError("Missing licensed footage required for "+idx)
    src=stock[key];dest=OUT/f"{idx}.mp4";lay=text_layer(text,idx,style)
    md=probe(src);srcdur=float(md["format"]["duration"])
    start=min(start,max(0,srcdur-dur-.3))
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",f"{start:.2f}","-i",src,"-loop","1","-i",lay,
         "-filter_complex",f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1[bg];[bg][1:v]overlay=0:0:shortest=1,format=yuv420p[vid]",
         "-map","[vid]","-t",str(dur),"-an","-c:v","libx264","-preset","veryfast","-crf","23","-r",str(FPS),"-pix_fmt","yuv420p",dest])
    return dest

def screen(source,text,idx,dur=3.5,features=False):
    base=Image.new("RGB",(W,H),CREAM)
    d=ImageDraw.Draw(base)
    if features:
        im=Image.open(source).convert("RGB")
        # Exact, unmodified part of a real interface; crop OUT the QA pet identity in header.
        im=im.crop((0,389,im.width,580))
        im.thumbnail((652,920))
        base.paste(im,((W-im.width)//2,202))
    else:
        im=Image.open(source).convert("RGB")
        im.thumbnail((640,1060))
        base.paste(im,((W-im.width)//2,(H-im.height)//2))
    bg=OUT/f"{idx}_screen.png";base.save(bg)
    lay=text_layer(text,idx,y=1030 if not features else 960)
    dest=OUT/f"{idx}.mp4"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate",str(FPS),"-i",bg,"-loop","1","-i",lay,
         "-filter_complex","[0:v][1:v]overlay=0:0,format=yuv420p[vid]","-map","[vid]",
         "-t",str(dur),"-an","-c:v","libx264","-preset","veryfast","-crf","22","-r",str(FPS),dest])
    return dest

cairosvg.svg2png(url=str(ROOT/"pazo-official-traced.svg"),write_to=str(OUT/"official_logo.png"),output_width=630)
logo=Image.open(OUT/"official_logo.png").convert("RGBA")
def end_card(idx,line1,line2):
    im=Image.new("RGB",(W,H),GREEN)
    im.paste(logo,((W-logo.width)//2,430),logo)
    d=ImageDraw.Draw(im)
    ft=ImageFont.truetype(FONT,33)
    y=850
    for line in [line1,line2]:
        wd=d.textbbox((0,0),line,font=ft)[2]
        d.text(((W-wd)/2,y),line,font=ft,fill=CREAM);y+=53
    u="pazo-app.vercel.app"
    fr=ImageFont.truetype(FONTR,29);wd=d.textbbox((0,0),u,font=fr)[2]
    d.text(((W-wd)//2,1030),u,font=fr,fill=(205,227,215))
    path=OUT/f"{idx}_end.png";im.save(path)
    out=OUT/f"{idx}_end.mp4"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate",str(FPS),"-i",path,"-t","3.5",
         "-an","-c:v","libx264","-preset","veryfast","-crf","22","-pix_fmt","yuv420p",out])
    return out

def soundtrack(idx,n_seconds):
    sr=32000;t=np.arange(int(sr*n_seconds))/sr
    waves=np.zeros_like(t)
    if idx==2:
        notes=[164.81,196.0,246.94];bpm=122
    elif idx==3:
        notes=[146.83,185,220];bpm=92
    else:
        notes=[196,246.94,293.66];bpm=116
    for freq in notes:
        waves+=0.012*np.sin(2*np.pi*freq*t+.018*np.sin(2*np.pi*.11*t))
    interval=60/bpm
    for step in range(int(n_seconds/interval)):
        tau=t-step*interval;mask=(tau>=0)&(tau<.16)
        waves[mask]+=.05*np.sin(2*np.pi*(160-(80*tau[mask]))*tau[mask])*np.exp(-27*tau[mask])
    env=np.minimum(1,t/.3)*np.minimum(1,(n_seconds-t)/.55)
    x=np.int16(np.clip(waves*env,-1,1)*32767)
    path=OUT/f"sound_{idx}.wav"
    with wave.open(str(path),"wb") as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(x.tobytes())
    return path

RENDERED=[]
def assemble(idx,name,clips):
    concat=OUT/f"concat_{idx}.txt"
    concat.write_text("".join("file '"+str(p.resolve())+"'\n" for p in clips))
    merged=OUT/f"silent_{idx}.mp4"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",concat,"-c","copy",merged])
    seconds=float(probe(merged)["format"]["duration"]);audio=soundtrack(idx,seconds)
    final=OUT/f"PAZO_{idx:02}_{name}.mp4"
    run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",merged,"-i",audio,"-map","0:v","-map","1:a",
         "-c:v","copy","-c:a","aac","-b:a","128k","-movflags","+faststart","-shortest",final])
    run(["ffmpeg","-v","error","-i",final,"-f","null","-"])
    metadata=probe(final)
    if len([s for s in metadata["streams"] if s["codec_type"]=="video"])!=1 or not any(s["codec_type"]=="audio" for s in metadata["streams"]):
        raise RuntimeError("A/V stream invalid")
    frames=[]
    for sec in [1,4.8,8.7,seconds-2]:
        fn=OUT/f"{idx}_frame_{int(sec*10)}.jpg"
        run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",str(sec),"-i",final,"-frames:v","1",fn])
        fr=Image.open(fn).convert("RGB");fr.thumbnail((360,640));frames.append(fr)
    sheet=Image.new("RGB",(1440,680),(230,230,224));dt=ImageDraw.Draw(sheet)
    for i,fr in enumerate(frames):
        sheet.paste(fr,(i*360,0));dt.text((i*360+15,646),f"SHOT {i+1}",fill=(20,45,39))
    sh=OUT/f"PAZO_{idx:02}_{name}_PREVIEW.jpg";sheet.save(sh,quality=89)
    RENDERED.append({"id":idx,"title":name,"file":final.name,"preview":sh.name,"duration":seconds,"bytes":final.stat().st_size})
    print("DELIVERED",final.name,final.stat().st_size,flush=True)

# 02 Comedy — real dog footage, humor conveyed by original on-screen copy.
sofa=choose("sofa","terrier")
puppy=choose("puppy","garden")
assemble(2,"He_Doesnt_Pay_Rent",[
    clip(sofa,"Pays no rent.", "02a",3.3),
    clip(puppy,"Zero responsibilities.","02b",3.3),
    clip("outdoor","Still runs the house.","02c",4.0),
    end_card("02","Every pet has a story.","PAZO")
])
# 03 Product: authentic live-product screenshots, QA name intentionally cropped.
assemble(3,"Their_Own_Space",[
    clip("garden","They're one of a kind.","03a",4.0),
    screen(welcome,"Meet their own space.","03b",3.5),
    screen(my_pet,"Profiles. QR passport. More.","03c",4.0,features=True),
    end_card("03","Made with love for pets.","Meet PAZO")
])
# 04 Story dialogue — REAL animal footage, NOT 3D and not claimed as such.
cat=choose("cat","cat2")
assemble(4,"The_Pet_CEO",[
    clip("outdoor","I have fans.","04a",3.3,style="dialogue"),
    clip(cat if cat else "terrier","You have a food bowl.","04b",3.7,style="dialogue"),
    clip("sofa" if stock["sofa"] is not None else "garden","It's called a personal brand.","04c",4.0,style="dialogue"),
    end_card("04","Every pet has a personality.","PAZO")
])
if not cat:print("VIDEO_04_FORMAT: real-dog-to-dog dialogue (NOT 3D and NO cat)",flush=True)

(OUT/"PROVENANCE_AND_QA.json").write_text(json.dumps({
    "status":"TECHNICAL_RENDER_VERIFIED__CREATIVE_REVIEW_REQUIRED",
    "source_license":"https://www.pexels.com/license/",
    "stock_assets":SOURCES,
    "real_pazo_screenshots":[
        "docs/evidence/issue147-release-20261028/canonical/mobile_en-welcome.png",
        "docs/evidence/issue147-release-20261028/navigation/en-390-My-Pet.png (QA identity cropped)"],
    "video_04_animation_status":"real-pet dialogue footage, NOT 3D; cat if verified otherwise dog-to-dog",
    "music":"new synthesized instrumental tracks, original generated by this script",
    "reused_branding":"official PAZO wordmark traced from owner supplied brand reference",
    "files":RENDERED},indent=2)+"\n")
print("DONE_BATCH",len(RENDERED),flush=True)
