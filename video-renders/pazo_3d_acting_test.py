# PAZO Video Production OS — original 3D acting test.
# This is a real procedural rigged-scene render; NO still-photo zoom or stock footage.
import bpy, math, os, sys, random
from mathutils import Vector
from math import radians
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DEST=ROOT/"delivery"/"acting_3d"
DEST.mkdir(parents=True,exist_ok=True)
scene=bpy.context.scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
for m in list(bpy.data.materials): bpy.data.materials.remove(m)
random.seed(11)
FPS=20
scene.render.fps=FPS
scene.frame_start=1
scene.frame_end=220
scene.render.resolution_x=480
scene.render.resolution_y=854
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.render.filepath=str(DEST/"frame_")
scene.render.film_transparent=False
scene.view_settings.view_transform='Standard'
scene.view_settings.look='Medium High Contrast'
scene.camera=None
def mat(name, rgba, roughness=.74, metallic=0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*rgba,1)
    m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value=(*rgba,1)
    bs.inputs["Roughness"].default_value=roughness
    bs.inputs["Metallic"].default_value=metallic
    return m
cream=mat("butter-dog",(.87,.61,.37))
dogpatch=mat("deep-toffee",(.56,.31,.19))
lightmuzzle=mat("cream-muzzle",(.985,.89,.70))
paw=mat("paw-caramel",(.73,.49,.27))
dark=mat("ink",(.075,.12,.13))
white=mat("eyes white",(1.0,.96,.86))
iris=mat("eyeball teal",(.21,.49,.43))
pink=mat("warm pink",(.92,.43,.42))
char=mat("cat-coat",(.20,.28,.30))
charlight=mat("cat-chest",(.31,.43,.39))
yellow=mat("tennis ball",(.87,.93,.27),roughness=.88)
ballline=mat("seam",(.96,.99,.68))
green=mat("deep green wall",(.14,.29,.27))
floormat=mat("light oak",(.71,.57,.42))
rugmat=mat("warm rug",(.88,.79,.62))
sofacolor=mat("teal sofa",(.22,.42,.38))
sofalight=mat("sofa cushions",(.29,.50,.44))
coffee=mat("dark oak furniture",(.35,.26,.20))
plant=mat("plant",(.28,.47,.27))
potmat=mat("ceramic",(.76,.53,.39))
def sphere(name, xyz, scale, material, parent=None, subdiv=16):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=subdiv,ring_count=max(8,subdiv//2),location=xyz)
    obj=bpy.context.object;obj.name=name
    obj.scale=scale
    if material:obj.data.materials.append(material)
    if parent:obj.parent=parent;obj.matrix_parent_inverse=parent.matrix_world.inverted()
    for p in obj.data.polygons:p.use_smooth=True
    return obj
def cube(name,xyz,scale,material,bevel=.10,parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1,location=xyz)
    obj=bpy.context.object;obj.name=name
    obj.dimensions=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bevel:
        m=obj.modifiers.new("soft bevel","BEVEL");m.width=bevel;m.segments=3
        obj.modifiers.new("weighted corner normals","WEIGHTED_NORMAL")
    if material:obj.data.materials.append(material)
    if parent:obj.parent=parent;obj.matrix_parent_inverse=parent.matrix_world.inverted()
    return obj
def cone(name, xyz, rad, depth,material,parent=None,vertices=5):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices,radius1=rad,radius2=.02,depth=depth,location=xyz)
    o=bpy.context.object;o.name=name
    if material:o.data.materials.append(material)
    if parent:o.parent=parent;o.matrix_parent_inverse=parent.matrix_world.inverted()
    b=o.modifiers.new("soft shape","BEVEL");b.width=.08;b.segments=2
    for poly in o.data.polygons:poly.use_smooth=True
    return o
def empty(name, loc, parent=None):
    obj=bpy.data.objects.new(name,None)
    bpy.context.collection.objects.link(obj)
    obj.location=loc
    if parent:obj.parent=parent; obj.matrix_parent_inverse=parent.matrix_world.inverted()
    return obj
def animate(obj,prop,keys):
    for f,v in keys:
        setattr(obj,prop,v)
        obj.keyframe_insert(data_path=prop,frame=f)
    if obj.animation_data and obj.animation_data.action:
        for curve in obj.animation_data.action.fcurves:
            for kp in curve.keyframe_points: kp.interpolation="BEZIER"
def look(obj,target):
    direction=Vector(target)-obj.location
    obj.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()

# Floor, cyc studio, living-room furniture.
cube("floor",(0,0,-.10),(20,20,.20),floormat,.02)
cube("wall",(0,4.25,2.65),(20,.20,5.5),green,.015)
cube("green side panel",(-4.5,3.95,2.3),(.12,.3,4.5),sofacolor,.015)
sphere("woven rug",(-.10,.18,.015),(2.6,1.75,.035),rugmat,subdiv=48)
# couch behind action
cube("sofa base",(1.72,2.70,.43),(2.68,1.05,.52),sofacolor,.25)
cube("sofa back",(1.72,3.11,.84),(2.62,.26,1.21),sofacolor,.20)
for x in (.58,2.86):cube("sofa side",(x,2.57,.75),(.35,1.28,.55),sofacolor,.16)
for x in (1.12,2.31):
    cube("plump cushion",(x,2.47,.68),(1.0,.80,.28),sofalight,.18)
# plant to balance scene
cube("ceramic pot",(-3.35,2.93,.39),(.45,.42,.65),potmat,.16)
for i in range(5):
    a=i*math.tau/5
    stem=sphere("leaf",(-3.35+math.cos(a)*.25,2.95+math.sin(a)*.14,1.1+.18*math.cos(i)),
               (.14,.30,.47),plant,subdiv=12)
    stem.rotation_euler=(.12*math.sin(a),.43*math.cos(a),a*.3)
# frame (wall art)
cube("wall deco",(0,4.08,2.55),(1.36,.1,.96),coffee,.06)
cube("wall deco inset",(0,3.99,2.55),(1.20,.03,.81),lightmuzzle,.03)
sphere("wall deco dot",(-.16,3.93,2.54),(.33,.02,.25),pink,subdiv=24)
# Dog root: parent all child segments by local transforms using parent inverse to preserve initial world.
dog=empty("dog_ROOT",(-1.43,-.15,0))
body=sphere("dog body",(-1.43,.32,.58),(.51,.72,.53),cream,dog,24)
chest=sphere("dog chest",(-1.44,-.10,.62),(.37,.25,.40),lightmuzzle,dog,20)
headpivot=empty("dog_head_control",(-1.43,-.30,1.22),dog)
head=sphere("dog head",(-1.43,-.30,1.22),(.54,.49,.51),cream,headpivot,24)
sphere("dog eyebrow stripe",(-1.63,-.732,1.44),(.20,.06,.11),dogpatch,headpivot)
sphere("dog muzzle",(-1.43,-.745,1.02),(.39,.25,.25),lightmuzzle,headpivot)
sphere("nose",(-1.43,-.974,1.14),(.125,.08,.09),dark,headpivot)
# eyes explicitly rigged for blink animation and glance.
dogeyes=[]
for dx in [-.235,.235]:
    e=sphere("dog eye",(-1.43+dx,-.727,1.34),(.132,.075,.162),white,headpivot,20)
    p=sphere("dog pupil",(-1.43+dx,-.803,1.33),(.063,.052,.08),dark,headpivot,16)
    dogeyes.append(e)
for dx in [-.39,.39]:
    ear=sphere("floppy dog ear",(-1.43+dx,-.13,1.57),(.19,.20,.37),dogpatch,headpivot,18)
    ear.rotation_euler[1]=(-1 if dx<0 else 1)*.3
# articulated paws/forelegs
doglegs=[]
for dx in [-.31,.31]:
    limb=empty("front-leg-pivot",(-1.43+dx,-.24,.53),dog)
    sphere("front paw",(-1.43+dx,-.35,.30),(.19,.28,.27),paw,limb)
    sphere("paw toe",(-1.43+dx,-.53,.17),(.23,.15,.13),lightmuzzle,limb)
    doglegs.append(limb)
for dx in [-.32,.32]:sphere("back haunch",(-1.43+dx,.76,.29),(.26,.26,.27),cream,dog)
tail=empty("dog_tail_control",(-1.43,.86,.82),dog)
sphere("dog wag tail",(-1.43,1.06,.91),(.13,.31,.18),dogpatch,tail)
# Cat root.
cat=empty("cat_ROOT",(2.35,.01,0))
catbody=sphere("cat body",(2.35,.24,.50),(.40,.48,.49),char,cat,24)
sphere("cat bib",(2.35,-.115,.46),(.26,.18,.35),charlight,cat)
catheadpivot=empty("cat_head_control",(2.35,-.11,1.02),cat)
sphere("cat head",(2.35,-.12,1.04),(.44,.35,.37),char,catheadpivot,24)
for dx in [-.30,.30]:
    cone("cat triangular ear",(2.35+dx,-.045,1.41),.215,.41,char,catheadpivot)
    sphere("cat cheek",(2.35+dx*.65,-.38,.94),(.21,.14,.13),char,catheadpivot,20)
    sphere("cat eye white",(2.35+dx*.72,-.417,1.15),(.108,.05,.12),white,catheadpivot,18)
    sphere("cat pupil",(2.35+dx*.72,-.465,1.15),(.046,.028,.078),dark,catheadpivot,16)
sphere("cat nose",(2.35,-.487,1.015),(.070,.041,.048),pink,catheadpivot)
for dx in [-.28,.28]:sphere("cat hind foot",(2.35+dx,-.08,.14),(.14,.22,.17),char,cat)
leftpaw=empty("cat_LEFT_paw_CONTROL",(2.35-.31,-.27,.56),cat)
sphere("cat paw upper",(2.35-.31,-.30,.37),(.135,.14,.22),char,leftpaw,18)
sphere("cat paw tip",(2.35-.34,-.42,.23),(.14,.16,.11),charlight,leftpaw,16)
rightpaw=empty("cat_RIGHT_paw_CONTROL",(2.35+.28,-.27,.56),cat)
sphere("cat paw right",(2.35+.28,-.34,.37),(.13,.18,.22),char,rightpaw,18)
cattail=empty("CAT_TAIL_CTRL",(2.60,.69,.69),cat)
for step in range(4):
    b=sphere("cat tail segment",(2.59+step*.10,.73+step*.085,.66+step*.16),
             (.10,.16,.16),char,cattail,14)
# ball is independent, with geometric equator seam.
ball=sphere("tennis ball",(-.40,-.61,.20),(.205,.205,.205),yellow,subdiv=24)
seam=sphere("ball seam",(-.40,-.61,.20),(.213,.213,.213),ballline,subdiv=24)
# show yellow ball with surface line via two small arcs not needed full seam sphere opaque:
seam.hide_render=True
ball.location=(-.40,-.61,.20)
# cat actually swats same ball toward itself. Dog responds to visible action.
animate(cat,'location',[
    (1,(2.35,.01,0)),(46,(2.35,.01,0)),(82,(.95,-.04,0)),
    (118,(.78,-.04,0)),(161,(.78,-.04,0)),(220,(.78,-.04,0))
])
animate(catheadpivot,'rotation_euler',[
    (1,(0,0,0)),(54,(0,0,0)),(86,(.12,0,-.09)),(110,(-.04,0,.09)),
    (150,(0,0,0)),(220,(0,0,0))
])
animate(leftpaw,'rotation_euler',[
    (1,(0,0,0)),(79,(0,0,0)),(94,(-.65,0,-.18)),(104,(1.3,0,.24)),
    (113,(-.05,0,0)),(220,(0,0,0))
])
animate(cattail,'rotation_euler',[(1,(0,-.1,0)),(65,(0,.28,0)),(108,(0,-.43,0)),(146,(0,.25,0)),(220,(0,-.2,0))])
animate(ball,'location',[
    (1,(-.40,-.61,.20)),(94,(-.40,-.61,.20)),
    (106,(.20,-.49,.31)),(119,(.63,-.37,.20)),
    (137,(.68,-.39,.20)),(220,(.68,-.39,.20))
])
animate(ball,'rotation_euler',[(1,(0,0,0)),(94,(0,0,0)),(137,(0,4.4,0)),(220,(0,4.4,0))])
# dog attempts to reach then freezes; pauses are deliberate.
animate(headpivot,'rotation_euler',[
    (1,(0,0,0)),(32,(-.18,0,0)),(76,(-.36,0,0)),
    (96,(-.46,0,0)),(112,(.13,0,-.05)),(130,(.12,0,.10)),
    (166,(.10,0,.10)),(181,(.02,0,0)),(220,(.02,0,0))
])
animate(dog,'location',[(1,(-1.43,-.15,0)),(36,(-1.43,-.15,0)),(80,(-1.27,-.26,0)),(116,(-1.27,-.26,0)),(220,(-1.27,-.26,0))])
animate(tail,'rotation_euler',[
    (1,(0,0,-.24)),(16,(0,0,.28)),(34,(0,0,-.2)),(55,(0,0,.29)),
    (87,(0,0,-.20)),(102,(0,0,.13)),(110,(0,0,0)),(220,(0,0,0))
])
for i,leg in enumerate(doglegs):
    animate(leg,'rotation_euler',[(1,(0,0,0)),(57,(0,0,0)),(80,(-.45,0,0)),(110,(0,0,0)),(220,(0,0,0))])
# Eye blink payoff on reaction close-up.
for e in dogeyes:
    animate(e,'scale',[(1,(.132,.075,.162)),(162,(.132,.075,.162)),(166,(.132,.075,.015)),
                         (171,(.132,.075,.162)),(220,(.132,.075,.162))])
# small extra gesture cat sits smugly once ball is under paw
animate(catbody,'scale',[(1,(.40,.48,.49)),(126,(.40,.48,.49)),(145,(.47,.53,.39)),(220,(.47,.53,.39))])
# camera and shot boundaries. Cuts motivated: setup > movement > cat claims > reaction
def camera(name,position,target,orthoscale):
    bpy.ops.object.camera_add(location=position)
    c=bpy.context.object;c.name=name;c.data.type="ORTHO";c.data.ortho_scale=orthoscale
    look(c,target)
    return c
cam1=camera("01_WIDE_look_at_ball",(0,-8,3.7),(0,.36,1.0),5.6)
cam2=camera("02_LOW_ACTION",(.12,-5.6,2.05),(.05,-.05,.70),4.0)
cam3=camera("03_CAT_TAKES_BALL",(.7,-4.6,2.12),(.33,-.02,.65),3.0)
cam4=camera("04_DOG_REACTION",(-1.1,-4.7,2.09),(-1.27,-.25,1.25),2.25)
markers=[(1,cam1,"setup: dog sees ball"),(64,cam2,"dog approaches cat enters"),
         (103,cam3,"cat swats ball"),(151,cam4,"reaction pause")]
for f,c,name in markers:
    marker=scene.timeline_markers.new(name,frame=f);marker.camera=c
scene.camera=cam1
# lighting. CPU cycles for consistent 3D rendered geometry.
def area(name, loc, energy, size, color):
    data=bpy.data.lights.new(name,"AREA");data.energy=energy;data.shape="DISK";data.size=size;data.color=color
    o=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(o)
    o.location=loc;look(o,(0,0,1))
area("softbox upper left",(-3.5,-4.7,6.8),670,6,(1,.91,.79))
area("fill front right",(4,-2.7,4.0),420,5,(.77,.93,1.0))
area("rim above",(0,2.8,5.0),500,4,(1,.95,.85))
scene.world.color=(.36,.36,.36)
scene.render.engine="CYCLES"
scene.cycles.samples=8
scene.cycles.use_denoising=False
for layer in scene.view_layers:
    layer.cycles.use_denoising=False
scene.render.image_settings.color_mode="RGB"
scene.render.image_settings.color_depth="8"
scene.render.image_settings.file_format="PNG"
scene.render.filepath=str(DEST/"shot_")
scene.render.use_file_extension=True
scene.camera=cam1
# save editable Blender source for reproducibility
bpy.ops.wm.save_as_mainfile(filepath=str(DEST/"PAZO_3D_acting_test.blend"))
print("SCENE_MODEL_PASS: procedural two character scene / rigs / 4 cameras / ball animation / staged reaction",flush=True)
# Render frame samples first to verify visual framing cheaply, then render animation.
samples=[20,86,118,163]
for i,f in enumerate(samples):
    scene.frame_set(f)
    # timeline markers drive animation cameras via frame change at render
    for ff,cam,nm in reversed(markers):
        if f>=ff:scene.camera=cam;break
    scene.render.filepath=str(DEST/f"check_{i+1:02}.png")
    bpy.ops.render.render(write_still=True)
print("KEYFRAME_PREVIEW_PASS",flush=True)
# Frame sequence; render only if requested by workflow.
if "--full" in sys.argv:
    for f in range(scene.frame_start,scene.frame_end+1):
        scene.frame_set(f)
        for ff,cam,nm in reversed(markers):
            if f>=ff:scene.camera=cam;break
        scene.render.filepath=str(DEST/f"frame_{f:04d}.png")
        bpy.ops.render.render(write_still=True)
        if f%25==0:print("FRAME",f,"/",scene.frame_end,flush=True)
    print("ANIMATION_RENDER_PASS",flush=True)
