import bpy 
import sys
sys.path.append(r'C:/Users/Administrator/AppData/Roaming/Blender Foundation/Blender/2.82/scripts/addons/Bmesh clean 2_8x v1_1')
import __init__

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
                cube.name = new_col

class ApplyModify(bpy.types.Operator):
    bl_idname = "am.applymodify"
    bl_label = "Apply Modify"
    bl_description = "Just Apply Modify Operator" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        find_object('2GenMech','2GenMech',"3ApplyMech")
        #rename_object('GenMech')
        sel = bpy.context.selected_objects
        amProperty = context.scene.amProperties
        bpy.ops.object.mode_set(mode='OBJECT')
        for ob in sel:
            ob.select_set(True)
            bpy.context.view_layer.objects.active = ob
            #ob.convert(target='MESH')
            bpy.ops.object.convert(target='MESH')
            bpy.ops.object.mode_set(mode='EDIT')#！出错是因为没有返回值
            bpy.context.space_data.overlay.show_face_orientation = False# 法线
        self.report({'INFO'}, "3.Apply Modify")
        return {'FINISHED'}


class ApplyClean(bpy.types.Operator):
    bl_idname = "object.applyclean"
    bl_label = "Apply Clean"
    bl_description = "Apply Clean Operator UV，mirror" 
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
        bpy.ops.object.modifier_add(type='WELD')
        bpy.context.object.modifiers["Weld"].merge_threshold = 0.0035
        bpy.context.object.modifiers["Weld"].max_interactions = 4
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Weld")



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
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.delete_loose()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=0.0005)

        bpy.ops.object.mode_set(mode='EDIT')


        bpy.ops.mesh.select_all(action='SELECT')

        if amProperty.GenMechMirrorBoll ==True:
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
            #bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
        #else:
            #bpy.ops.mesh.select_all(action='SELECT')
            #bpy.ops.uv.smart_project()
            #bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.space_data.overlay.show_face_orientation = False# 法线



        
        #edit
        self.report({'INFO'}, "5.Apply Clean")
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

def RemeshEnum_update(self, context):#要设置回调函数才行callback
    #ob = context.object.modifiers["Remesh"]
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

        #GenMechRemeshEnum = ob.modifiers["Remesh"].mode
    #return GenMechRemeshEnum.items
    #return ob.modifiers["Remesh"].mode
        #amProperty.GenMechRemeshEnum = ob.mode
    #GenMechRemeshEnum = ob.modifiers["Remesh"].mode
    #bpy.context.object.modifiers["Remesh"].mode = 'SHARP'

'''
def UVpack():
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
'''

'''
def rename_object(new_name):
    #thisobj = bpy.context.view_layer.objects.active
    #old_name=thisobj.name
    #old_name=new_name
    genMech_result = bpy.data.collections['2GenMech']
    if len(genMech_result.objects) > 0:#如果在当前Collection中有物体
        for childObject in genMech_result.objects:
            #此处添加的代码判断它的名字来获取
            if 'EdgesGen' in childObject.name:#如果该物体的名字中出现Cube
                childObject.select_set(True)#选择所有找到有cube字符的物体
                cube = bpy.data.objects[childObject.name]
                cube.name = new_name
'''
'''
select_box_up_counter=0
select_box_left_counter = 0
select_box_down_counter = 0
select_box_right_counter = 0
'''
'''
#def select_init(context):
for area in bpy.context.screen.areas:
    if area.type == "VIEW_3D":
        break

for region in area.regions:
    if region.type == "WINDOW":
        break


space = area.spaces[0]

context = bpy.context.copy()
context['area'] = area
context['region'] = region
context['space_data'] = space
'''
'''
def select_box_up(context):
    global select_box_up_counter
    select_box_up_counter +=1
    print("select_box_up")
    #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITLEFT')
    #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

    bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
    bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
    if select_box_up_counter ==51:
        bpy.app.timers.register(select_box_left)
        select_box_up_counter =0
        return None
    return 0.1

def select_box_left():
    global select_box_left_counter
    select_box_left_counter +=1
    print("select_box_left")
    bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITLEFT')
    bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

    #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
    #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
    if select_box_left_counter ==51:
        bpy.app.timers.register(select_box_down)
        select_box_left_counter = 0
        return None
    return 0.1

def select_box_down():
    global select_box_down_counter
    select_box_down_counter +=1
    print("select_box_down")
    bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITDOWN')
    bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

    #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
    #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
    if select_box_down_counter ==51:
        bpy.app.timers.register(select_box_right)
        select_box_down_counter = 0
        return None
    return 0.1

def select_box_right():
    global select_box_right_counter
    select_box_right_counter +=1
    print("select_box_right")
    bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITRIGHT')
    bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

    #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
    #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
    if select_box_right_counter ==51:
        bpy.app.timers.unregister(select_box_up)
        bpy.app.timers.unregister(select_box_left)
        bpy.app.timers.unregister(select_box_down)
        bpy.app.timers.unregister(select_box_right)
        select_box_right_counter = 0
        return None
    return 0.1
'''
'''
bpy.app.timers.register(select_box_up)
if select_box_up_counter ==51:
    bpy.app.timers.register(select_box_left)
if select_box_left_counter ==51:
    bpy.app.timers.unregister(select_box_left)
    bpy.app.timers.unregister(select_box_up)
    bpy.app.timers.register(select_box_right)
'''