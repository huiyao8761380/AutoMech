bl_info = {
    "name" : "AutoMech",
    "author" : "Tang Hui",
    "description" : "(N key)Do as possible to Auto mechanical modeling , lowpoly and bake to game.",
    "blender" : (2, 82, 7),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
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
        "edgeLoc": IntVectorProperty(name="LocEdge", default=(0,0,0)),
        "edgeLocBool": BoolProperty(name="LocEdge", default=False),
        "LocEdit": FloatVectorProperty(name="LocEdit", default=(0,0,0)),
        "LocEditBool": BoolProperty(name="LocEdit", default=False)
    })



classes = ( SamplePropertyGroup, AMProperties, AutoMechPanel, GenLine, GenMech, EdgesGen)
#register, unregister = bpy.utils.register_classes_factory(classes)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.sampleProperty = PointerProperty(type=SamplePropertyGroup)
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