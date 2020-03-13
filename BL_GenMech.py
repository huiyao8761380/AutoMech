import bpy
#import random

from . BL_Tool import *
from . BL_EdgesGen import EdgesGen

class GenMech(bpy.types.Operator):
    bl_idname = "object.bl_genmech"
    bl_label = "Do Mech Gen"
    bl_description = "Just do Mech Mesh generate~Operator" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        find_object('1GenLine','0AutoMech',"2GenMech")
        #rename_object('GenMech')
        sel = bpy.context.selected_objects
        for selectobj in sel:
            bpy.ops.object.modifier_add(type='SKIN')
        self.report({'INFO'}, "2.Gen Mech:bpy.ops.object.bl_genmech()")
        return {'FINISHED'}