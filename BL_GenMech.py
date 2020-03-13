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
        for ob in sel:
            bpy.context.view_layer.objects.active = ob
            #for mod in [m for m in ob.modifiers if m.type != 'SKIN']:

            #for m in ob.modifiers:
                #if m.type != 'SKIN':
            objmod = ob.modifiers.get("Skin")
            if objmod:
                ob.modifiers.remove(objmod)
            bpy.ops.object.modifier_add(type='SKIN')

            #for mod in [m for m in ob.modifiers if m.type != 'SKIN']:
                #bpy.ops.object.modifier_add(modifier = mod.name)


            #for mod in [m for m in ob.modifiers if m.type == 'ARMATURE']:
                #bpy.ops.object.modifier_apply( modifier = mod.name )#应用修改器

        '''
        #act = bpy.context.active_object
        genMech_result = bpy.data.collections['2GenMech']
        if len(genMech_result.objects) > 0:
            for childObject in genMech_result.objects:
                if '2GenMech' in childObject.name:
                    childObject.select_set(True)
                    bpy.ops.object.modifier_add(type='SKIN')

        #for selectobj in sel:
            #selectobj=bpy.ops.object.modifier_add(type='SKIN')
        '''
        self.report({'INFO'}, "2.Gen Mech:bpy.ops.object.bl_genmech()")
        return {'FINISHED'}