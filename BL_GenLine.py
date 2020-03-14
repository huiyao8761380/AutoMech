import bpy
from bpy.types import Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty,StringProperty

from . BL_Panel import * #
from . BL_EdgesGen import EdgesGen



class GenLine(bpy.types.Operator):
    bl_idname = "object.bl_genline"
    bl_label = "Do Edges Gen"
    bl_description = "Just do Edges line generate~Operator" 
    bl_options = {'REGISTER'}




    def execute(self, context):
        sampleProperty = context.scene.sampleProperty
        amProperty = context.scene.amProperties
        edgeName= "1GenLine" #sampleProperty.edgeName
        edgeMin = sampleProperty.edgeMin
        edgeMax = sampleProperty.edgeMax
        edgeVNumber = sampleProperty.edgeVNumber
        if sampleProperty.edgeLocBool == True:
            edgeLocation = sampleProperty.edgeLoc
        else:
            edgeLocation = (0,0,0)

        myedges = EdgesGen(edgeName,edgeMin,edgeMax,edgeVNumber,edgeLocation)
        myedges.add_EdgeMesh()#组成头部等身体各部位


        if sampleProperty.LocEditBool == True:
            #bpy.ops.object.select_set(True)
            #bpy.context.active_object
            #bpy.context.selected_objects
            #sel.mode_set(mode='EDIT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.active_object
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.transform.translate(value=sampleProperty.LocEdit)
            bpy.ops.object.mode_set(mode='OBJECT')
        #col = bpy.ops.collection.create(name="GenCol")
        #if col != bpy.data.collections.get(name="GenCol"):
            #col.objects.link(MyObject)

        #myedges.MyObject = bpy.context.object
        self.report({'INFO'}, "1.Gen Line:bpy.ops.object.bl_genline()")
        return {'FINISHED'}