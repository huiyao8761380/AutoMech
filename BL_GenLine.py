import bpy
from bpy.types import Operator

from . BL_EdgesGen import EdgesGen


class GenLine(bpy.types.Operator):
    bl_idname = "object.bl_genline"
    bl_label = "Do Edges Gen"
    bl_description = "Just do Edges line generate~Operator" 
    bl_options = {'REGISTER'}

    def execute(self, context):
        myedges = EdgesGen('1GenLine',-5,5,10,(0,0,0))
        myedges.add_EdgeMesh()#组成头部等身体各部位
        #col = bpy.ops.collection.create(name="GenCol")
        #if col != bpy.data.collections.get(name="GenCol"):
            #col.objects.link(MyObject)

        #myedges.MyObject = bpy.context.object
        self.report({'INFO'}, "1.Gen Line:bpy.ops.object.bl_genline()")
        return {'FINISHED'}