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

from . BL_Panel import *
from . BL_GenLine import GenLine
from . BL_GenMech import GenMech
from . BL_EdgesGen import EdgesGen

from bpy.types import Panel,Operator




classes = ( AutoMechPanel, GenLine, GenMech, SamplePropertyGroup)
#register, unregister = bpy.utils.register_classes_factory(classes)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.samplePropertyGroup = PointerProperty(type=SamplePropertyGroup)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.samplePropertyGroup
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