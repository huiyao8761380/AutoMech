import bpy
from . BL_Tool import *


class AddRig(bpy.types.Operator):
    bl_idname = "aw.addrig"
    bl_label = "Add Rig"
    bl_description = "AddRig,please append the rigify add-on at first"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if "metarig" not in bpy.data.objects:
            bpy.ops.object.armature_basic_human_metarig_add()
            bpy.ops.transform.resize(value=(5.5, 3.5, 3.5), orient_type='CURSOR', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            for rig in bpy.data.objects:
                #if "metarig" in bpy.data.objects:
                if rig.name =='metarig':
                    rig.select_set(True)
                    col_name="6AddRig"
                    addrig = bpy.data.objects[rig.name]
                    cube_collection = find_collection(bpy.context, addrig)#2通过函数find_collection制作合集
                    new_collection = make_collection(col_name,cube_collection)
                    col = bpy.data.collections.get(col_name)#4
                    col.objects.link(addrig)
                    cube_collection.objects.unlink(addrig)
                    addrig.name = col_name



        #for rig in bpy.data.objects:
            #if "metarig" in bpy.data.objects:
                #make_collection("6AddRig","0AutoMech")
                #bpy.data.collections["6AddRig"].objects.link(rig)

        #bpy.data.collections["0AutoMech"].objects.unlink(rig) 
        #make_collection("6AddRig","0AutoMech")
        #bpy.data.collections["4MechClean"].objects.link(rig)
        #only_find_object("metarig","6AddRig")
        return {"FINISHED"}


