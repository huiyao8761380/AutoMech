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

        #初始化生成位置
        if sampleProperty.edgeLocBool == True:
            edgeLocation = sampleProperty.edgeLoc
        else:
            sampleProperty.edgeLoc = (0,0,0)
            edgeLocation = sampleProperty.edgeLoc
        
        if amProperty.GenLineEnum =='GenLineOnly':
            '''
            sampleProperty.edgeMin = 0
            sampleProperty.edgeMax = 0
            sampleProperty.edgeVNumber = 8
            sampleProperty.edgeLoc = (0,0,0)
            '''

            edgeName= "1GenLine" #sampleProperty.edgeName
            edgeMin = sampleProperty.edgeMin
            edgeMax = sampleProperty.edgeMax
            edgeVNumber = sampleProperty.edgeVNumber


            myedges = EdgesGen(edgeName,edgeMin,edgeMax,edgeVNumber,edgeLocation)
            myedges.add_EdgeMesh()#组成头部等身体各部位

        elif amProperty.GenLineEnum =='GenLineMechBody':
            edgeName= "1GenLineLeg"
            
            sampleProperty.edgeMin = 0
            sampleProperty.edgeMax = 0
            sampleProperty.edgeVNumber = 10
            sampleProperty.edgeLoc = (1,0,0)
            

            edgeMin = sampleProperty.edgeMin
            edgeMax = sampleProperty.edgeMax
            edgeVNumber = sampleProperty.edgeVNumber
            edgeLocation = sampleProperty.edgeLoc

            sampleProperty.edgeXYZ =True
            sampleProperty.xuMin = 0
            sampleProperty.yuMin = -0.3
            sampleProperty.zuMin = 3
            sampleProperty.xvMax = 0.2
            sampleProperty.yvMax = 0
            sampleProperty.zvMax = 3

            genLeg = EdgesGen(edgeName,edgeMin,edgeMax,edgeVNumber,edgeLocation)
            genLeg.add_EdgeMesh()

        elif amProperty.GenLineEnum =='GenLineStruct':
            edgeName= "1GenLineStruct"
            sampleProperty.edgeMin = -5
            sampleProperty.edgeMax = 5
            sampleProperty.edgeVNumber = 10
            sampleProperty.edgeLoc = (0,0,0)

            edgeMin = sampleProperty.edgeMin
            edgeMax = sampleProperty.edgeMax
            edgeVNumber = sampleProperty.edgeVNumber
            edgeLocation = sampleProperty.edgeLoc

            genStruct = EdgesGen(edgeName,edgeMin,edgeMax,edgeVNumber,edgeLocation)
            genStruct.add_EdgeMesh()
        
        elif amProperty.GenLineEnum =='GenLineKit':
            edgeName= "1GenLineKit"
            sampleProperty.edgeMin = 0
            sampleProperty.edgeMax = 0
            sampleProperty.edgeVNumber = 8
            sampleProperty.edgeLoc = (0,0,0)

            edgeMin = sampleProperty.edgeMin
            edgeMax = sampleProperty.edgeMax
            edgeVNumber = sampleProperty.edgeVNumber
            edgeLocation = sampleProperty.edgeLoc

            sampleProperty.edgeXYZ =True
            sampleProperty.xuMin = -0.3
            sampleProperty.yuMin = -1
            sampleProperty.zuMin = 0.2
            sampleProperty.xvMax = 0.3
            sampleProperty.yvMax = 1
            sampleProperty.zvMax = 0.55

            genKit = EdgesGen(edgeName,edgeMin,edgeMax,edgeVNumber,edgeLocation)
            genKit.add_EdgeMesh()

        elif amProperty.GenLineEnum =='GenLineWeapon':
            edgeName= "1GenLineWeapon"
            sampleProperty.edgeMin = 0
            sampleProperty.edgeMax = 0
            sampleProperty.edgeVNumber = 20
            sampleProperty.edgeLoc = (0,0,0)

            edgeMin = sampleProperty.edgeMin
            edgeMax = sampleProperty.edgeMax
            edgeVNumber = sampleProperty.edgeVNumber
            edgeLocation = sampleProperty.edgeLoc

            sampleProperty.edgeXYZ =True
            sampleProperty.xuMin = -0.1
            sampleProperty.yuMin = -15
            sampleProperty.zuMin = -1
            sampleProperty.xvMax = 0.1
            sampleProperty.yvMax = 30
            sampleProperty.zvMax = 3

            genWeapon = EdgesGen(edgeName,edgeMin,edgeMax,edgeVNumber,edgeLocation)
            genWeapon.add_EdgeMesh()


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

            #已空物体为中心的镜像
            #bpy.ops.transform.resize(value=(1, 1, 2.63777))


        self.report({'INFO'}, "1.Gen Line:bpy.ops.object.bl_genline()")
        return {'FINISHED'}