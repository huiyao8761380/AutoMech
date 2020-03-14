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
        sampleProperty = context.scene.samplePropertyGroup
        amProperty = context.scene.amProperties

        if amProperty.GenLineEnum =='GenLineOnly':
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

        elif amProperty.GenLineEnum =='GenLineMechBody':
            edgeName= "1GenLineBody"
            edgeMin = 0
            edgeMax = 0
            edgeVNumber = 10
            edgeLocation = (1,0,0)

            sampleProperty.edgeXYZ =True
            sampleProperty.xuMin = 0
            sampleProperty.yuMin = -0.3
            sampleProperty.zuMin = 3
            sampleProperty.xvMax = 0.2
            sampleProperty.yvMax = 0
            sampleProperty.zvMax = 3

            '''
            xu = 0
            yu = -0.4
            zu = 0

            xv = 0.1
            yv = 0
            zv = 3
            '''
            genLeg = EdgesGen(edgeName,edgeMin,edgeMax,edgeVNumber,edgeLocation)
            genLeg.add_EdgeMesh()



        if sampleProperty.LocEditBool == True:
            #bpy.ops.object.select_set(True)
            #bpy.context.active_object
            #bpy.context.selected_objects
            #sel.mode_set(mode='EDIT')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.active_object
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.transform.translate(value=sampleProperty.LocEdit)
            bpy.ops.object.mode_set(mode='OBJECT')

            #bpy.ops.transform.resize(value=(1, 1, 2.63777))


        self.report({'INFO'}, "1.Gen Line:bpy.ops.object.bl_genline()")
        return {'FINISHED'}