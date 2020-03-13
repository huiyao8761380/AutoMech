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
            #暂时切勿更改以下修改器名字
            Skin = ob.modifiers.get("Skin")
            Remesh = ob.modifiers.get("Remesh")
            Bevel = ob.modifiers.get("Bevel")
            Decimate = ob.modifiers.get("Decimate")
            Decimate2 = ob.modifiers.get("Decimate.001")
            Bevel1 = ob.modifiers.get("Bevel.001")
            EdgeSplit = ob.modifiers.get("EdgeSplit")
            Solidify = ob.modifiers.get("Solidify")
            Bevel2 = ob.modifiers.get("Bevel.002")
            Mirror = ob.modifiers.get("Mirror")
            Displace = ob.modifiers.get("Displace")

            if Skin:
                ob.modifiers.remove(Skin)
            bpy.ops.object.modifier_add(type='SKIN')

            if Remesh:
                ob.modifiers.remove(Remesh)
            bpy.ops.object.modifier_add(type='REMESH')
            bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
            #bpy.context.object.modifiers["Remesh"].mode = 'SHARP'
            bpy.context.object.modifiers["Remesh"].octree_depth = 6 #
            bpy.context.object.modifiers["Remesh"].scale = 0.88 #0.75

            if Bevel:
                ob.modifiers.remove(Bevel)
            bpy.ops.object.modifier_add(type='BEVEL')
            bpy.context.object.modifiers["Bevel"].offset_type = 'PERCENT'
            bpy.context.object.modifiers["Bevel"].width_pct = 37 #动画
            bpy.context.object.modifiers["Bevel"].use_only_vertices = True
            bpy.context.object.modifiers["Bevel"].use_clamp_overlap = True
            bpy.context.object.modifiers["Bevel"].loop_slide = True
            bpy.context.object.modifiers["Bevel"].material = -1         #0
                

            if Decimate:
                ob.modifiers.remove(Decimate)
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.02

            if Decimate2:
                ob.modifiers.remove(Decimate2)
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate.001"].decimate_type = 'DISSOLVE'
            bpy.context.object.modifiers["Decimate.001"].delimit = {'MATERIAL'}

            if Bevel1:
                ob.modifiers.remove(Bevel1)
            bpy.ops.object.modifier_add(type='BEVEL')
            bpy.context.object.modifiers["Bevel.001"].offset_type = 'PERCENT'
            bpy.context.object.modifiers["Bevel.001"].width_pct = 33
            bpy.context.object.modifiers["Bevel.001"].use_only_vertices = True
            bpy.context.object.modifiers["Bevel.001"].use_clamp_overlap = True
            bpy.context.object.modifiers["Bevel.001"].loop_slide = True
            bpy.context.object.modifiers["Bevel.001"].material = 0         #1

            if EdgeSplit:
                ob.modifiers.remove(EdgeSplit)
            bpy.ops.object.modifier_add(type='EDGE_SPLIT')

            if Solidify:
                ob.modifiers.remove(Solidify)
            bpy.ops.object.modifier_add(type='SOLIDIFY')
            bpy.context.object.modifiers["Solidify"].thickness = -0.02
            bpy.context.object.modifiers["Solidify"].use_rim_only = True
            bpy.context.object.modifiers["Solidify"].material_offset_rim = 0  #1


            if Bevel2:
                ob.modifiers.remove(Bevel2)
            bpy.ops.object.modifier_add(type='BEVEL')
            bpy.context.object.modifiers["Bevel.002"].offset_type = 'OFFSET'
            bpy.context.object.modifiers["Bevel.002"].width = 0.05
            bpy.context.object.modifiers["Bevel.002"].material = -1             #

            if Mirror:
                ob.modifiers.remove(Mirror)
            bpy.ops.object.modifier_add(type='MIRROR')

            if Displace:
                ob.modifiers.remove(Displace)
            bpy.ops.object.modifier_add(type='DISPLACE')
            bpy.context.object.modifiers["Displace"].direction = 'NORMAL'
            bpy.context.object.modifiers["Displace"].mid_level = 0.5
            bpy.context.object.modifiers["Displace"].strength = 0.05

            bpy.context.object.modifiers["Skin"].show_expanded = True
            bpy.context.object.modifiers["Bevel"].show_in_editmode = False
            bpy.context.object.modifiers["Bevel.001"].show_in_editmode = False
            bpy.context.object.modifiers["EdgeSplit"].show_in_editmode = False
            bpy.context.object.modifiers["Solidify"].show_in_editmode = False
            bpy.context.object.modifiers["Bevel.002"].show_in_editmode = False


            bpy.context.object.modifiers["Skin"].show_expanded = False
            bpy.context.object.modifiers["Remesh"].show_expanded = False
            bpy.context.object.modifiers["Bevel"].show_expanded = False
            bpy.context.object.modifiers["Decimate"].show_expanded = False
            bpy.context.object.modifiers["Decimate.001"].show_expanded = False
            bpy.context.object.modifiers["Bevel.001"].show_expanded = False
            bpy.context.object.modifiers["EdgeSplit"].show_expanded = False
            bpy.context.object.modifiers["Solidify"].show_expanded = False
            bpy.context.object.modifiers["Bevel.002"].show_expanded = False
            bpy.context.object.modifiers["Mirror"].show_expanded = False
            bpy.context.object.modifiers["Displace"].show_expanded = False




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