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
        #find_object('1GenLine','0AutoMech',"2GenMech")
        only_move_object('0AutoMech',"2GenMech")
        #rename_object('GenMech')
        sel = bpy.context.selected_objects
        amProperty = context.scene.amProperties

        #if 'metarig' in rig.name :请添加这个判断
        for ob in sel:
            bpy.context.view_layer.objects.active = ob
            #for mod in [m for m in ob.modifiers if m.type != 'SKIN']:
            if len(ob.data.vertices) <=2500:#防误触 顶点小于的时候才能运行

                #for m in ob.modifiers:
                    #if m.type != 'SKIN':
                #暂时切勿更改以下修改器名字
                if len(ob.material_slots) < 1:##如果没有槽，那么我们追加创建槽和分配
                    bpy.ops.object.material_slot_add()
                    bpy.ops.object.material_slot_add()
                    bpy.ops.object.material_slot_add()
                    bpy.ops.object.material_slot_add()
                    bpy.ops.object.material_slot_add()

                    if bpy.data.materials.get("0") is not None:#物体已经有材料了
                        mat0 = bpy.data.materials["0"]
                    else:#制作新材料
                        mat0 = bpy.data.materials.new(name="0")
                    #将新材质分配给选定的对象 
                    if len(ob.data.materials):#如果已经有材料的空位
                        ob.data.materials[0] = mat0
                    else:
                        ob.data.materials.append(mat0)


                    if bpy.data.materials.get("1") is not None:
                        mat1 = bpy.data.materials["1"]
                    else:
                        mat1 = bpy.data.materials.new(name="1")
                    
                    if len(ob.data.materials):
                        ob.data.materials[1] = mat1
                    else:
                        ob.data.materials.append(mat1)


                    if bpy.data.materials.get("2") is not None:
                        mat2 = bpy.data.materials["2"]
                    else:
                        mat2 = bpy.data.materials.new(name="2")
                    
                    if len(ob.data.materials):
                        ob.data.materials[2] = mat2
                    else:
                        ob.data.materials.append(mat2)

                    
                    if bpy.data.materials.get("3") is not None:
                        mat3 = bpy.data.materials["3"]
                    else:
                        mat3 = bpy.data.materials.new(name="3")
                    
                    if len(ob.data.materials):
                        ob.data.materials[3] = mat3
                    else:
                        ob.data.materials.append(mat3)


                    if bpy.data.materials.get("4") is not None:
                        mat4 = bpy.data.materials["4"]
                    else:
                        mat4 = bpy.data.materials.new(name="4")
                    
                    if len(ob.data.materials):
                        ob.data.materials[4] = mat4
                    else:
                        ob.data.materials.append(mat4)


                    mat0.diffuse_color = (0, 0.238852, 1, 1)    
                    mat0.metallic = 0.8
                    mat0.specular_intensity = 0.1
                    mat0.roughness = 0.3

                    mat1.diffuse_color = (1, 0.936776, 0.314941, 1)
                    mat1.metallic = 1
                    mat1.specular_intensity = 0.35
                    mat1.roughness = 0.15

                    mat2.diffuse_color = (0.056421, 0.104517, 0.195988, 1)
                    mat2.metallic = 0.75
                    mat2.specular_intensity = 0.45
                    mat2.roughness = 0.3

                    mat3.diffuse_color = (0.22542, 0.499922, 0.638272, 1)
                    mat3.metallic = 0.85
                    mat3.specular_intensity = 0.5
                    mat3.roughness = 0.2

                    mat4.diffuse_color = (0.0134106, 0.0134106, 0.0134106, 1)
                    mat4.metallic = 0.6
                    mat4.specular_intensity = 0
                    mat4.roughness = 0.7

                    #bpy.context.object.active_material.diffuse_color = (0.8, 0.49499, 0.655768, 1)
                    #bpy.context.object.active_material.diffuse_color = (0.112115, 0.149903, 0.28101, 1)

                #b = bpy.ops.material.new()
                #c = bpy.data.materials["1"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0753091, 0.07658, 0.0248376, 1)


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

                if amProperty.GenMechEnum =='GenMechfy1':

                    mod_Skin = ob.modifiers.new("Skin", "SKIN")

                    #bpy.ops.object.modifier_add(type='REMESH')
                    mod_Remesh = ob.modifiers.new("Remesh", "REMESH")
                    mod_Remesh.mode = 'SMOOTH'#'SMOOTH'!!!!!!!!!!amProperty.GenMechRemeshEnum


                    #bpy.context.object.modifiers["Remesh"].mode = 'SHARP'
                    mod_Remesh.octree_depth = 6 #
                    mod_Remesh.scale = 0.88 #0.75

                    mod_Bevel = ob.modifiers.new("Bevel", "BEVEL")
                    mod_Bevel.offset_type = 'PERCENT'
                    mod_Bevel.width_pct = 37 #动画
                    mod_Bevel.use_only_vertices = True
                    mod_Bevel.use_clamp_overlap = True
                    mod_Bevel.loop_slide = True
                    mod_Bevel.material = 3         #0

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
                    mod_Bevel1.material = 4         #1

                    mod_EdgeSplit = ob.modifiers.new("EdgeSplit", "EDGE_SPLIT")

                    mod_Solidify = ob.modifiers.new("Solidify", "SOLIDIFY")
                    mod_Solidify.thickness = -0.02
                    mod_Solidify.use_rim_only = True
                    mod_Solidify.material_offset_rim = 2  #1

                    mod_Bevel2 = ob.modifiers.new("Bevel.002", "BEVEL")
                    mod_Bevel2.offset_type = 'OFFSET'
                    mod_Bevel2.width = 0.05
                    mod_Bevel2.material = 1            #

                    mod_Displace = ob.modifiers.new("Displace", "DISPLACE")
                    mod_Displace.direction = 'NORMAL'
                    mod_Displace.mid_level = 0.5
                    mod_Displace.strength = 0.05

                    if amProperty.GenMechMirrorBoll == True:
                        if Mirror:
                            ob.modifiers.remove(Mirror)
                        mod_Mirror = ob.modifiers.new("Mirror", "MIRROR")
                        if '_l' in ob.name:
                            mod_Mirror.use_axis[0] = False
                            mod_Mirror.use_axis[1] = True
                            mod_Mirror.use_bisect_axis[0] = False
                            mod_Mirror.use_bisect_flip_axis[0] = False
                            if 'thigh_l' in ob.name:
                                mod_Mirror.use_axis[0] = True
                                mod_Mirror.use_axis[1] = False
                            elif 'calf_l' in ob.name:
                                mod_Mirror.use_axis[0] = True
                                mod_Mirror.use_axis[1] = False
                            elif 'foot_l' in ob.name:
                                mod_Mirror.use_axis[0] = True
                                mod_Mirror.use_axis[1] = False
                            
                    else:
                        if Mirror:
                            ob.modifiers.remove(Mirror)


                elif amProperty.GenMechEnum =='GenMechfy2':
                    mod_Skin = ob.modifiers.new("Skin", "SKIN")

                    #bpy.ops.object.modifier_add(type='REMESH')
                    mod_Remesh = ob.modifiers.new("Remesh", "REMESH")
                    mod_Remesh.mode = 'SMOOTH'
                    #bpy.context.object.modifiers["Remesh"].mode = 'SHARP'
                    mod_Remesh.octree_depth = 4 #
                    mod_Remesh.scale = 0.88 #0.75

                    mod_Bevel = ob.modifiers.new("Bevel", "BEVEL")
                    mod_Bevel.offset_type = 'PERCENT'
                    mod_Bevel.width_pct = 37 #动画
                    mod_Bevel.use_only_vertices = True
                    mod_Bevel.use_clamp_overlap = True
                    mod_Bevel.loop_slide = True
                    mod_Bevel.material = 3         #0

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
                    mod_Bevel1.material = 4         #1

                    mod_EdgeSplit = ob.modifiers.new("EdgeSplit", "EDGE_SPLIT")

                    mod_Solidify = ob.modifiers.new("Solidify", "SOLIDIFY")
                    mod_Solidify.thickness = -0.02
                    mod_Solidify.use_rim_only = True
                    mod_Solidify.material_offset_rim = 2  #1

                    mod_Bevel2 = ob.modifiers.new("Bevel.002", "BEVEL")
                    mod_Bevel2.offset_type = 'OFFSET'
                    mod_Bevel2.width = 0.05
                    mod_Bevel2.material = 1             #

                    mod_Displace = ob.modifiers.new("Displace", "DISPLACE")
                    mod_Displace.direction = 'NORMAL'
                    mod_Displace.mid_level = 0.5
                    mod_Displace.strength = 0.01#

                    if amProperty.GenMechMirrorBoll == True:
                        if Mirror:
                            ob.modifiers.remove(Mirror)
                        mod_Mirror = ob.modifiers.new("Mirror", "MIRROR")
                        if '_l' in ob.name:
                            mod_Mirror.use_axis[0] = False
                            mod_Mirror.use_axis[1] = True
                            mod_Mirror.use_bisect_axis[0] = False
                            mod_Mirror.use_bisect_flip_axis[0] = False
                            if 'thigh_l' in ob.name:
                                mod_Mirror.use_axis[0] = True
                                mod_Mirror.use_axis[1] = False
                            elif 'calf_l' in ob.name:
                                mod_Mirror.use_axis[0] = True
                                mod_Mirror.use_axis[1] = False
                            elif 'foot_l' in ob.name:
                                mod_Mirror.use_axis[0] = True
                                mod_Mirror.use_axis[1] = False
                    else:
                        if Mirror:
                            ob.modifiers.remove(Mirror)
                        


            for mod in ob.modifiers:
                mod.show_expanded = False
                mod.show_in_editmode = False

        amProperty.GenMechSkinResize =  (1,1,1)
        genLine_result = bpy.data.collections["2GenMech"]#在这个合集中找到所有物体，修改这里的合集0AutoMech
        if len(genLine_result.objects) > 12:#如果在当前Collection中有物体
            for childObject in genLine_result.objects:
        #for ob in sel:
                bpy.ops.object.select_all(action='DESELECT')
                childObject.select_set(True)
                bpy.context.view_layer.objects.active = childObject

                if 'neck_01' in childObject.name or 'hand_l' in childObject.name:
                    if bpy.context.mode =='OBJECT':
                        bpy.ops.object.mode_set(mode='EDIT')
                        #bpy.ops.mesh.select_all(action='SELECT')    
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.transform.skin_resize(value=(0.6,0.6,0.6), mirror=True, use_proportional_edit=False, proportional_edit_falloff='RANDOM', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                        bpy.ops.transform.skin_resize(value=amProperty.GenMechSkinResize, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                        #bpy.ops.transform.skin_resize(value=amProperty.GenMechSkinResize)
                        #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE', action='TOGGLE')
                        bpy.ops.object.mode_set(mode='OBJECT')
                
                elif '_l' in childObject.name or 'head' in childObject.name or 'spine_01' in childObject.name:
                    if bpy.context.mode =='OBJECT':
                        bpy.ops.object.mode_set(mode='EDIT')
                        #bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.transform.skin_resize(value=(0.8,0.8,0.8), mirror=True, use_proportional_edit=False, proportional_edit_falloff='RANDOM', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                        bpy.ops.transform.skin_resize(value=amProperty.GenMechSkinResize, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                        #bpy.ops.transform.skin_resize(value=amProperty.GenMechSkinResize, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                        #bpy.ops.transform.skin_resize(value=amProperty.GenMechSkinResize)
                        #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE', action='TOGGLE')
                        bpy.ops.object.mode_set(mode='OBJECT')
                

#bpy.ops.mesh.bisect(plane_co=(0, 0, 50), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=243, xend=243, ystart=349, yend=20)
#bpy.ops.object.editmode_toggle()
#bpy.ops.mesh.select_all(action='TOGGLE')
#bpy.ops.mesh.bisect(plane_co=(0, 0, 10), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=243, xend=243, ystart=349, yend=20)
#以下3步骤制作折痕
#精简塌陷 0.1折痕 0.01low-》精简平面5 精简平面10
#细分
#精简塌陷维持在1000面 / 精简平面5 精简平面10

#另一种方法
#bpy.ops.wm.tool_set_by_id(name="builtin.select_box")
#bpy.ops.view3d.view_orbit(angle=5.0, type='ORBITLEFT') x-bpy.ops.view3d.view_orbit(type='ORBITLEFT')
#






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
        self.report({'INFO'}, "2.Gen Mech:如果物体顶点数小于2500执行")
        return {'FINISHED'}

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