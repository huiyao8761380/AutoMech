import bpy
#import random

from . BL_Tool import *
from . BL_EdgesGen import EdgesGen

from bpy.types import Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty,StringProperty

class GenMech(bpy.types.Operator):
    bl_idname = "object.bl_genmech"
    bl_label = "Do Mech Gen"
    bl_description = "Just do Mech Mesh generate~Operator" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        find_object('1GenLine','0AutoMech',"2GenMech")
        #rename_object('GenMech')
        sel = bpy.context.selected_objects
        amProperty = context.scene.amProperties

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

            if Remesh:
                ob.modifiers.remove(Remesh)

            if Bevel:
                ob.modifiers.remove(Bevel)

            if Decimate:
                ob.modifiers.remove(Decimate)

            if Decimate2:
                ob.modifiers.remove(Decimate2)

            if Bevel1:
                ob.modifiers.remove(Bevel1)

            if EdgeSplit:
                ob.modifiers.remove(EdgeSplit)

            if Solidify:
                ob.modifiers.remove(Solidify)

            if Bevel2:
                ob.modifiers.remove(Bevel2)

            if Displace:
                ob.modifiers.remove(Displace)



            mod_Skin = ob.modifiers.new("Skin", "SKIN")

            #bpy.ops.object.modifier_add(type='REMESH')
            mod_Remesh = ob.modifiers.new("Remesh", "REMESH")
            mod_Remesh.mode = 'SMOOTH'
            #bpy.context.object.modifiers["Remesh"].mode = 'SHARP'
            mod_Remesh.octree_depth = 6 #
            mod_Remesh.scale = 0.88 #0.75

            mod_Bevel = ob.modifiers.new("Bevel", "BEVEL")
            mod_Bevel.offset_type = 'PERCENT'
            mod_Bevel.width_pct = 37 #动画
            mod_Bevel.use_only_vertices = True
            mod_Bevel.use_clamp_overlap = True
            mod_Bevel.loop_slide = True
            mod_Bevel.material = -1         #0

            mod_Decimate = ob.modifiers.new("Decimate", "DECIMATE")
            mod_Decimate.ratio = 0.02

            mod_Decimate2 = ob.modifiers.new("Decimate.001", "DECIMATE")
            mod_Decimate2.decimate_type = 'DISSOLVE'
            mod_Decimate2.delimit = {'MATERIAL'}

            mod_Bevel1 = ob.modifiers.new("Bevel.001", "BEVEL")
            mod_Bevel1.offset_type = 'PERCENT'
            mod_Bevel1.width_pct = 33
            mod_Bevel1.use_only_vertices = True
            mod_Bevel1.use_clamp_overlap = True
            mod_Bevel1.loop_slide = True
            mod_Bevel1.material = 0         #1

            mod_EdgeSplit = ob.modifiers.new("EdgeSplit", "EDGE_SPLIT")

            mod_Solidify = ob.modifiers.new("Solidify", "SOLIDIFY")
            mod_Solidify.thickness = -0.02
            mod_Solidify.use_rim_only = True
            mod_Solidify.material_offset_rim = 0  #1

            mod_Bevel2 = ob.modifiers.new("Bevel.002", "BEVEL")
            mod_Bevel2.offset_type = 'OFFSET'
            mod_Bevel2.width = 0.05
            mod_Bevel2.material = -1             #

            if amProperty.GenMechMirrorBoll == True:
                if Mirror:
                    ob.modifiers.remove(Mirror)
                mod_Mirror = ob.modifiers.new("Mirror", "MIRROR")
            else:
                if Mirror:
                    ob.modifiers.remove(Mirror)

            mod_Displace = ob.modifiers.new("Displace", "DISPLACE")
            mod_Displace.direction = 'NORMAL'
            mod_Displace.mid_level = 0.5
            mod_Displace.strength = 0.05


            for mod in ob.modifiers:
                mod.show_expanded = False
                mod.show_in_editmode = False
            '''
            mod_Skin.show_in_editmode = True
            mod_Bevel.show_in_editmode = False
            mod_Bevel1.show_in_editmode = False
            mod_EdgeSplit.show_in_editmode = False
            mod_Solidify.show_in_editmode = False
            mod_Bevel2.show_in_editmode = False


            mod_Skin.show_expanded = False
            mod_Remesh.show_expanded = False
            mod_Bevel.show_expanded = False
            mod_Decimate.show_expanded = False
            mod_Decimate2.show_expanded = False
            mod_Bevel1.show_expanded = False
            mod_EdgeSplit.show_expanded = False
            mod_Solidify.show_expanded = False
            mod_Bevel2.show_expanded = False
            mod_Mirror.show_expanded = False
            mod_Displace.show_expanded = False
            '''




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