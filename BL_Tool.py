import bpy
from . easybpy import *
#import sys
#sys.path.append(r'C:/Users/Administrator/AppData/Roaming/Blender Foundation/Blender/2.82/scripts/addons/Bmesh clean 2_8x v1_1')
#import __init__

def find_collection(context, item):
    collections = item.users_collection
    if len(collections) > 0:
        return collections[0]
    return context.scene.collection

def make_collection(collection_name, parent_collection):
    if collection_name in bpy.data.collections:
        return bpy.data.collections[collection_name]
    else:
        new_collection = bpy.data.collections.new(collection_name)
        parent_collection.children.link(new_collection)
        return new_collection

def find_object(find_name,old_col,new_col):#是调用上面两个函数的函数，所有输入都为’‘ 或“”
    genLine_result = bpy.data.collections[old_col]#在这个合集中找到所有物体，修改这里的合集0AutoMech
    if len(genLine_result.objects) > 0:#如果在当前Collection中有物体
        for childObject in genLine_result.objects:
            #此处添加的代码判断它的名字来获取
            if find_name in childObject.name:#如果该物体的名字中出现Cube
                childObject.select_set(True)#选择所有找到有cube字符的物体
                cube = bpy.data.objects[childObject.name]#选择这些物体并赋值给cube
        #cube = bpy.data.objects["Cube.001"]
                cube_collection = find_collection(bpy.context, cube)#通过函数find_collection制作合集
                new_collection = make_collection(new_col, cube_collection)#NEW col 将合集交给1GenLine
                # Step 2
                #if aready in coll
                new_collection.objects.link(cube)  # put the cube in the new collection 从新合集中添加物体
                cube_collection.objects.unlink(cube)  # remove it from the old collection 从旧合集中删除物体
                #cube.name = new_col

def only_move_object(old_col,new_col):#是调用上面两个函数的函数，所有输入都为’‘ 或“”
    genLine_result = bpy.data.collections[old_col]#在这个合集中找到所有物体，修改这里的合集0AutoMech
    if len(genLine_result.objects) > 0:#如果在当前Collection中有物体
        for childObject in genLine_result.objects:
            #此处添加的代码判断它的名字来获取
            #if len(childObject.data.vertices) <=2500:
            #if find_name in childObject.name:#如果该物体的名字中出现Cube
            childObject.select_set(True)#选择所有找到有cube字符的物体
            cube = bpy.data.objects[childObject.name]#选择这些物体并赋值给cube
            cube_collection = find_collection(bpy.context, cube)#通过函数find_collection制作合集
            new_collection = make_collection(new_col, cube_collection)#NEW col 将合集交给1GenLine
            new_collection.objects.link(cube)  # put the cube in the new collection 从新合集中添加物体
            cube_collection.objects.unlink(cube)  # remove it from the old collection 从旧合集中删除物体

class ApplyModify(bpy.types.Operator):
    bl_idname = "am.applymodify"
    bl_label = "Apply Modify"
    bl_description = "Apply Modify,ctrl+J you like,then check name not have '.001' etc,before step 9. need to do" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        #find_object('1GenLine','2GenMech',"3ApplyMech")#这里需要改命名
        only_move_object('2GenMech',"3ApplyMech")
        #rename_object('GenMech')
        sel = bpy.context.selected_objects
        amProperty = context.scene.amProperties
        bpy.ops.object.mode_set(mode='OBJECT')
        for ob in sel:
            ob.select_set(True)
            bpy.context.view_layer.objects.active = ob
            #ob.convert(target='MESH') bpy.ops.object.convert(target='MESH')
            bpy.ops.object.convert(target='MESH')
            bpy.ops.object.mode_set(mode='EDIT')#todo ！出错是因为没有返回值
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE', action='TOGGLE')#
            bpy.context.space_data.overlay.show_face_orientation = False# 法线
        self.report({'INFO'}, "3.Apply Modify")
        return {'FINISHED'}


class ApplyClean(bpy.types.Operator):
    bl_idname = "object.applyclean"
    bl_label = "Apply Clean"
    bl_description = "Only One direction now,apply Clean Operator UV，mirror" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        #find_object('4MechClean','4MechClean',"5ApplyClean")
        #rename_object('GenMech')
        #sel = bpy.context.selected_objects
        #amProperty = context.scene.amProperties
        
        #for ob in sel:
            #ob.select_set(True)
            #bpy.context.view_layer.objects.active = ob
            #ob.convert(target='MESH')
        
        bpy.ops.mesh.hide(unselected=False)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.delete(type='ONLY_FACE')
        bpy.ops.mesh.reveal()
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
        bpy.ops.mesh.select_all(action='INVERT')
        bpy.ops.mesh.delete(type='EDGE_FACE')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE', action='TOGGLE')
        amProperty = context.scene.amProperties



        bpy.ops.object.mode_set(mode='OBJECT')

        sel = bpy.context.selected_objects
        for ob in sel:
            bpy.context.view_layer.objects.active = ob

            add_weld(ob,'WELD')#bpy.ops.object.modifier_add(type='WELD')  add_weld(bpy.context.object,'WELD')
            ob.modifiers["WELD"].merge_threshold = 0.0035   
            ob.modifiers["WELD"].max_interactions = 4
            bpy.ops.object.modifier_apply(modifier="WELD")#bpy.ops.object.modifier_apply(modifier="WELD")


        '''绝对路径问题
        if amProperty.GenMechBemeshClean ==True:
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.scene.scene_check_set.preset_list = '2 - Blender Default'
            #bpy.context.scene.scene_check_set.in_out_menu = 'OUT'
            __init__.bmesh_clean()
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.scene.scene_check_set.preset_list = '1 - Import clean'
            #bpy.context.scene.scene_check_set.in_out_menu = 'OUT'
            __init__.bmesh_clean()
            bpy.ops.object.mode_set(mode='OBJECT')
            #bpy.ops.object.mode_set(mode='EDIT')
        '''

        bpy.ops.object.mode_set(mode='EDIT')
        
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.delete_loose()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=0.0005)

        bpy.ops.object.mode_set(mode='EDIT')


        bpy.ops.mesh.select_all(action='SELECT')

        if amProperty.GenMechMirrorBoll ==True:
            if "_l" in bpy.context.object.data.name or "_r" in bpy.context.object.data.name :
                if "clavicle" in bpy.context.object.data.name:
                    bpy.ops.mesh.bisect(plane_co=(-1, 0.2, -10), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=204, xend=713, ystart=198, yend=196)
                elif "upperarm" in bpy.context.object.data.name:
                    bpy.ops.mesh.bisect(plane_co=(-1, 0.15, -10), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=204, xend=713, ystart=198, yend=196)
                elif "lowerarm" in bpy.context.object.data.name:
                    bpy.ops.mesh.bisect(plane_co=(-1, 0.2, -10), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=204, xend=713, ystart=198, yend=196)
                elif "hand" in bpy.context.object.data.name:
                    bpy.ops.mesh.bisect(plane_co=(-1, 0.2, -10), plane_no=(0, 1, 0), use_fill=False, clear_inner=False, clear_outer=True, xstart=204, xend=713, ystart=198, yend=196)
                else:
                    bpy.ops.mesh.bisect(plane_co=(0.5, 0, 50), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=243, xend=243, ystart=349, yend=20)
            else:
                bpy.ops.mesh.bisect(plane_co=(0, 0, 50), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=243, xend=243, ystart=349, yend=20)



        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.uv.smart_project()
        
        if amProperty.GenMechUVPackmaster ==True:
            try:
                bpy.context.scene.tool_settings.use_uv_select_sync = True
                bpy.context.space_data.uv_editor.show_stretch = True
                bpy.ops.uv.pack_islands(margin=0)
                
                bpy.ops.uvpackmaster2.uv_overlap_check() 
                bpy.ops.uvpackmaster2.uv_measure_area()
                bpy.ops.uvpackmaster2.uv_validate()
                
                bpy.context.scene.uvp2_props.margin = 0.002
                bpy.context.scene.uvp2_props.precision = 1000
                bpy.context.scene.uvp2_props.prerot_disable = False
                bpy.context.scene.uvp2_props.rot_step = 90
                bpy.context.scene.uvp2_props.island_rot_step_enable = True
                
                bpy.context.scene.uvp2_props.pre_validate = False
                bpy.context.scene.uvp2_props.pack_to_others = False
                bpy.context.scene.uvp2_props.lock_overlapping = True#重叠

            except:
                print("problem")
            finally:
                #bpy.ops.mesh.mark_seam(clear=False) #
                bpy.ops.uvpackmaster2.uv_pack()
                
                #bpy.app.timers.register(UVpack)
                
                #bpy.ops.object.mode_set(mode='OBJECT')
        #bpy.ops.object.mode_set(mode='OBJECT')

        if amProperty.GenMechMirrorBoll ==True:
            #bpy.ops.mesh.bisect(plane_co=(0, 0, 50), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=243, xend=243, ystart=349, yend=20)
            #bpy.ops.mesh.select_all(action='SELECT')
            #bpy.ops.uv.smart_project()
            #bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.modifier_add(type='MIRROR')
            if "clavicle" in bpy.context.object.data.name:
                bpy.context.object.modifiers["Mirror"].use_axis[0] = False
                bpy.context.object.modifiers["Mirror"].use_axis[1] = True
            elif "upperarm" in bpy.context.object.data.name:
                bpy.context.object.modifiers["Mirror"].use_axis[0] = False
                bpy.context.object.modifiers["Mirror"].use_axis[1] = True
            elif "lowerarm" in bpy.context.object.data.name:
                bpy.context.object.modifiers["Mirror"].use_axis[0] = False
                bpy.context.object.modifiers["Mirror"].use_axis[1] = True
            elif "hand" in bpy.context.object.data.name:
                bpy.context.object.modifiers["Mirror"].use_axis[0] = False
                bpy.context.object.modifiers["Mirror"].use_axis[1] = True       
            #bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
        #else:
            #bpy.ops.mesh.select_all(action='SELECT')
            #bpy.ops.uv.smart_project()
            #bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.space_data.overlay.show_face_orientation = False# 法线
        #bpy.ops.object.make_links_data(type='MODIFIERS')




        
        #edit
        self.report({'INFO'}, "5.Apply Clean")
        return {'FINISHED'}

class ReName(bpy.types.Operator):
    bl_idname = "am.rename"
    bl_label = "ReName"
    bl_description = "Jast ReName" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        for reobj in bpy.context.selected_objects:
            if '.' in reobj.name:#
                reobj.name = reobj.name[:-4]
                reobj.data.name = reobj.name

        self.report({'INFO'}, "ReName: delete '.001' ")
        return {'FINISHED'}



class MirrorSelect(bpy.types.Operator):
    bl_idname = "am.mirrorselect"
    bl_label = "Mirror Select"
    bl_description = "Mirror Select form _l to _r" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        #if bpy.context.mode !='OBJECT':
        #bpy.ops.object.mode_set(mode='OBJECT')
        sel = bpy.context.selected_objects
        amProperty = context.scene.amProperties
        #bpy.ops.object.mode_set(mode='OBJECT')
        if '_l' in bpy.context.object.name:
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
            bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
            bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)



        for rob in bpy.data.objects:
            if '_l' in rob.name:
                if '.' in rob.name:#
                    rob.name = rob.name[:-6] + "_r"
                    rob.data.name = rob.name
            #if rob.name.endswith("_l"):
                #rob.name = rob.name[:-2] + "_r"
                #rob.data.name = rob.name

                #bpy.context.object.data.name = "upperarm_r"
        '''
        for ob in sel:
            if '_l' in ob.name:
                ob.select_set(True)
                #bpy.context.view_layer.objects.active = ob
                bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

                #bpy.context.view_layer.objects.active = ob
                if '.' in bpy.context.object.name:
                    bpy.context.object.name = bpy.context.object.name[:-4]
                if bpy.context.object.name.endswith("_l"):
                    bpy.context.object.name = bpy.context.object.name[:-2] + "_r"
                    bpy.context.object.data.name = bpy.context.object.name
                #bpy.context.object.data.name = "upperarm_r"

                #bpy.context.object.select_set(False)


        for rob in bpy.data.objects:
            if '_r' in rob.name:
                ob.select_set(True)
                bpy.context.view_layer.objects.active = rob
                bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
                bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            '''


                #bpy.context.object.location[0] = 0 - bpy.context.object.location[0]
                #bpy.ops.transform.mirror(orient_type='GLOBAL', constraint_axis=(True, False, False), use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        
        self.report({'INFO'}, "6.Mirror Select form _l to _r")
        return {'FINISHED'}



def edgeLoc_update(self, context):
    ob = context.object
    sampleProperty = context.scene.samplePropertyGroup
    edgeLoc = sampleProperty.edgeLoc
    if sampleProperty.edgeLocBool == True:
        ob.location = edgeLoc
    else:
        edgeLoc= (0, 0, 0)#sampleProperty.edgeLocBool = (0, 0, 0)
        #ob.location = edgeLoc

def LocEdit_update(self, context):
    ob = context.object
    sampleProperty = context.scene.samplePropertyGroup
    LocEdit = sampleProperty.LocEdit
    if sampleProperty.LocEditBool == True:
        bpy.ops.object.mode_set(mode='OBJECT')
        #bpy.ops.object.select_all(action='DESELECT')
        bpy.context.active_object
        #bpy.ops.object.mode_set(mode='EDIT')
        #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
        
        #bpy.ops.mesh.select_all(action='SELECT')
        bpy.context.scene.cursor.location = sampleProperty.LocEdit
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        #bpy.ops.transform.translate(value=sampleProperty.LocEdit)
        #bpy.ops.object.mode_set(mode='OBJECT')

        #
        #
    else:
        edgeLoc= (0, 0, 0)
    '''
    if sampleProperty.LocEditBool == True:
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.active_object
        bpy.ops.object.mode_set(mode='EDIT')
        #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
        #bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.translate(value=sampleProperty.LocEdit)
        bpy.ops.object.mode_set(mode='OBJECT')

        #bpy.context.scene.cursor.location = (0,0,0)
        #bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    else:
        edgeLoc= (0, 0, 0)
    '''
def RemeshEnum_update(self, context):#要设置回调函数才行callback
    '''
    items=[
        ('BLOCKS', 'BLOCKS', ""),
        ('SMOOTH', 'SMOOTH', ""),
        ('SHARP', 'SHARP', "")
    ]
    '''
    amProperty = context.scene.amProperties
    GenMechRemeshEnum=amProperty.GenMechRemeshEnum
    sel = bpy.context.selected_objects
    for ob in sel:
        bpy.context.view_layer.objects.active = ob
        #GenMechRemeshEnum = ob.modifiers["Remesh"].mode
    #if GenMechRemeshEnum == '':
        #ob.mode = 'SHARP'
        if ob.modifiers["Remesh"].mode != GenMechRemeshEnum:
            ob.modifiers["Remesh"].mode = GenMechRemeshEnum
    #return items
        #GenMechRemeshEnum = ob.modifiers["Remesh"].mode
    #return GenMechRemeshEnum.items
    #return ob.modifiers["Remesh"].mode
        #amProperty.GenMechRemeshEnum = ob.mode
    #GenMechRemeshEnum = ob.modifiers["Remesh"].mode
    #bpy.context.object.modifiers["Remesh"].mode = 'SHARP'

def GenMechBevel0Enum_callback(self, context):
    #amProperty = context.scene.amProperties
    items = [
            ('OFFSET', 'OFFSET', "", 0),
            ('WIDTH', 'WIDTH', "", 1),
            ('DEPTH', 'DEPTH', "", 2),
            ('PERCENT', 'PERCENT', "", 3)
            #('None', 'None', "", 5)
        ]
    #ob = context.object
    #if ob is not None:
        #items.valus = int(ob.modifiers["Bevel"].offset_type)
    return items

def GenMechBevel0Enum_update(self, context):
    amProperty = context.scene.amProperties
    sel = bpy.context.selected_objects
    if sel is not None:
        for ob in sel:
            if ob.modifiers.get("Bevel"):
                bpy.context.view_layer.objects.active = ob
                ob.modifiers["Bevel"].offset_type = amProperty.GenMechBevel0Enum
            #b = ob.modifiers["Bevel"].offset_type
            #amProperty.GenMechBevel0Enum = b
            #get_Bevel0Enum()
    '''
    for ob in sel:
        if ob.modifiers.get("Bevel"):
            bpy.context.view_layer.objects.active = ob
            ob.modifiers["Bevel"].offset_type = amProperty.GenMechBevel0Enum
    '''

def GenMechBevel0float_update(self, context):
    #amProperty = context.scene.amProperties
    sampleProperty = context.scene.samplePropertyGroup
    sel = bpy.context.selected_objects
    for ob in sel:
        if ob.modifiers.get("Bevel"):
            bpy.context.view_layer.objects.active = ob
            ob.modifiers["Bevel"].width_pct = sampleProperty.Bevel0float

def GenMechResize_update(self, context):
    amProperty = context.scene.amProperties
    sel = bpy.context.selected_objects
    if amProperty.GenMechResizeBoll == True:
        bpy.ops.object.mode_set(mode='OBJECT')
            #   bpy.ops.object.select_all(action='DESELECT')
            #bpy.context.active_object
            #bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.resize(value=(1,1,1))
        bpy.ops.transform.resize(value=amProperty.GenMechResize)
        #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE', action='TOGGLE')
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        bpy.ops.transform.resize(value=(1,1,1))

def GenMechSkinResize_update(self, context):
    amProperty = context.scene.amProperties
    sel = bpy.context.selected_objects
    if sel is not None:
        if amProperty.GenMechSkinSizeBool == True:
            bpy.ops.object.mode_set(mode='OBJECT')
                #   bpy.ops.object.select_all(action='DESELECT')
                #bpy.context.active_object
                #bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')    
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.transform.skin_resize(value=(amProperty.GenMechSkinResize), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            #bpy.ops.transform.skin_resize(value=amProperty.GenMechSkinResize)
            #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE', action='TOGGLE')
            bpy.ops.object.mode_set(mode='OBJECT')
    else:
            #amProperty.GenMechSkinResize = (1,1,1)
            #bpy.ops.transform.skin_resize(value=amProperty.GenMechSkinResize)
        bpy.ops.transform.skin_resize(value=(1,1,1))


def GenMechRemeshScale_update(self, context):
    amProperty = context.scene.amProperties
    #sampleProperty = context.scene.samplePropertyGroup
    sel = bpy.context.selected_objects
    for ob in sel:
        if ob.modifiers.get("Remesh"):
            bpy.context.view_layer.objects.active = ob
            ob.modifiers["Remesh"].scale = amProperty.GenMechRemeshScale







def set_GenMechResize(self, value):
    #x=0.1
    self["Bevel0Enum"] = (1,1,1)

def get_Bevel0Enum(self):
    ob = bpy.context.selected_objects
    #bpy.context.view_layer.objects.active = ob
    amProperty = bpy.context.scene.amProperties
    
    if bpy.context.object.modifiers.get("Bevel"):
        if ob is not None:
            amProperty.GenMechBevel0Enum = bpy.context.object.modifiers["Bevel"].offset_type
        #self["Bevel0Enum"] = amProperty.GenMechBevel0Enum
    #bpy.context.object.modifiers["Bevel"].offset_type =
            return self.get("Bevel0Enum")
    else:
        self["Bevel0Enum"] = 5
    
    return self["Bevel0Enum"]
    

    
    '''
    if bpy.context.object.modifiers["Bevel"].offset_type == 'OFFSET':
        return 1
    elif bpy.context.object.modifiers["Bevel"].offset_type == 'WIDTH':
        return 2
    elif bpy.context.object.modifiers["Bevel"].offset_type == 'DEPTH':
        return 3
    elif bpy.context.object.modifiers["Bevel"].offset_type == 'PERCENT':
        return 4
    #return ob.modifiers["Bevel"].offset_type
    '''

def set_Bevel0Enum(self, value):
    #print("setting value", value)
    amProperty = bpy.context.scene.amProperties
    #bpy.context.object.modifiers["Bevel"].offset_type = amProperty.GenMechBevel0Enum
    #value = amProperty.GenMechBevel0Enum
    #amProperty.GenMechBevel0Enum = bpy.context.object.modifiers["Bevel"].offset_type
    '''
    amProperty = bpy.context.scene.amProperties
    sel = bpy.context.selected_objects
    for ob in sel:
        bpy.context.view_layer.objects.active = ob
        ob.modifiers["Bevel"].offset_type = amProperty.GenMechBevel0Enum
        value = amProperty.GenMechBevel0Enum
        #return amProperty.GenMechBevel0Enum
    '''
    '''
    ob = bpy.context.selected_objects
    value = amProperty.GenMechBevel0Enum
    if ob is not None:
        if self["Bevel0Enum"] == 1:
            bpy.context.object.modifiers["Bevel"].offset_type = 'OFFSET'
        elif self["Bevel0Enum"] == 2:
            bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        elif self["Bevel0Enum"] == 3:
            bpy.context.object.modifiers["Bevel"].offset_type = 'DEPTH'
        elif self["Bevel0Enum"] == 4:
            bpy.context.object.modifiers["Bevel"].offset_type = 'PERCENT'
        else:
            self["Bevel0Enum"] = value
        '''
    self["Bevel0Enum"] = value

def RemoveAllModifier():
    ob = bpy.context.object
    bpy.context.object.modifiers.clear()
