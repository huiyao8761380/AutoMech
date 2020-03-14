import bpy 

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
    bl_idname = "object.applymodify"
    bl_label = "Apply Modify"
    bl_description = "Just Apply Modify Operator" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        find_object('2GenMech','2GenMech',"3ApplyMech")
        #rename_object('GenMech')
        sel = bpy.context.selected_objects
        amProperty = context.scene.amProperties

        for ob in sel:
            bpy.context.view_layer.objects.active = ob
            #ob.convert(target='MESH')
            bpy.ops.object.convert(target='MESH')
        
        self.report({'INFO'}, "3.Apply Modify Gen Mech: bpy.ops.object.applymodify()")
        return {'FINISHED'}


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