bl_info = {
    "name" : "AutoMech", "AutoMech-2_90"
    "author" : "透过现象看本质(Tang Hui)",
    "description" : "(N key)Do as possible to Auto mechanical modeling , lowpoly and bake to game.",
    "blender" : (2, 90, 1),
    "version" : (0, 0, 2),
    "location" : "View3D",
    "warning" : "If it can't use,please rename addon folder to AutoMech.",
    "category" : "Object"
}

import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import *

#from bpy.types import PropertyGroup
#from bpy.props import FloatProperty, PointerProperty,StringProperty

from . BL_Panel import *
from . BL_GenLine import GenLine
from . BL_GenMech import GenMech
from . BL_EdgesGen import EdgesGen
from . BL_Properties import AMProperties
from . BL_Tool import *
from . BL_MechClean import MechClean
from . BL_AddRig import AddRig
from . BL_BindRig import BindRig
from . BL_WeightRig import WeightRig

from bpy.types import Panel,Operator,PropertyGroup

SamplePropertyGroup = type(
    "SamplePropertyGroup",
    (PropertyGroup,),
    {
        "edgeName": StringProperty(name="NameEdge", default='1GenLine'),
        "edgeMin": IntProperty(name="MinEdge", default=-5),
        "edgeMax": IntProperty(name="MaxEdge", default=5),
        "edgeVNumber": IntProperty(name="VNumberedge", default=10),
        "edgeXYZ": BoolProperty(name="edgeXYZ", default=False),
        "xuMin": FloatProperty(name="xuMin", default=-1),
        "yuMin": FloatProperty(name="yuMin", default=-1),
        "zuMin": FloatProperty(name="zuMin", default=-1),
        "xvMax": FloatProperty(name="xvMax", default=1),
        "yvMax": FloatProperty(name="yvMax", default=1),
        "zvMax": FloatProperty(name="zvMax", default=1),
        "edgeLoc": FloatVectorProperty(name="LocEdge", default=(0,0,0),step=10, update=edgeLoc_update),
        "edgeLocBool": BoolProperty(name="LocEdge", default=False),
        "LocEdit": FloatVectorProperty(name="LocEdit", default=(0,0,0),step=10, update=LocEdit_update),#
        "LocEditBool": BoolProperty(name="LocEdit", default=False),
        "Bevel0float": FloatProperty(name="width_pct", default=37, min=0, max=100, update=GenMechBevel0float_update)
    })


classes = ( AutoMechPanel, GenLine, GenMech, SamplePropertyGroup, AMProperties, ApplyModify, MechClean, ApplyClean, AddRig, BindRig, WeightRig, MirrorSelect, ReName)
#register, unregister = bpy.utils.register_classes_factory(classes)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.samplePropertyGroup = PointerProperty(type=SamplePropertyGroup)
    bpy.types.Scene.amProperties = PointerProperty(type=AMProperties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.samplePropertyGroup
    del bpy.types.Scene.amProperties
#bpy.types.Scene.samplePropertyGroup = PointerProperty(type=SamplePropertyGroup)
#def register():
    #bpy.utils.register_class(AutoMechPanel)
    #bpy.utils.register_class(GenLine)

#def unregister():
    #bpy.utils.unregister_class(AutoMechPanel)
    #bpy.utils.unregister_class(GenLine)

if __name__ == "__main__":
    register()
    #bpy.ops.object.GenLine()