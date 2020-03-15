import bpy
from . BL_GenLine import GenLine 
from . BL_GenMech import GenMech
from . BL_EdgesGen import EdgesGen
from . BL_Properties import AMProperties
from . BL_Tool import ApplyModify
from bpy.types import Panel,Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty


class AutoMechPanel(bpy.types.Panel):
    bl_label = "Auto Mech"
    bl_idname = "Auto_Mech_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AutoMech'

    def draw(self, context):
        sampleProperty = context.scene.samplePropertyGroup
        amProperty = context.scene.amProperties

        layout = self.layout
        col = layout.column(align=True)

        row = col.row(align=True)
        row5 = layout.row(align=True)
        col2 = layout.column(align=True)
        row2 = col2.row(align=True)
        col3 = layout.column(align=True)
        row3 = col3.row(align=True)
        col4 = layout.column(align=True)
        row4 = col4.row(align=True)
        col5 = layout.column(align=True)
        col5.prop(amProperty, "GenLineEnum")
        col5.operator("object.bl_genline" , text = "1.Gen Line")

        #if amProperty.GenLineEnum =='GenLineOnly':
            
            #col.prop(sampleProperty, "edgeName")
        row.prop(sampleProperty, "edgeMin")
        row.prop(sampleProperty, "edgeMax")
        row.prop(sampleProperty, "edgeVNumber")

            #col5 = layout.column(align=True)


        row5.prop(sampleProperty, "edgeXYZ")
        row5.prop(sampleProperty, "edgeLocBool")
        row5.prop(sampleProperty, "LocEditBool")



        if sampleProperty.edgeXYZ == True:
            row2.prop(sampleProperty, "xuMin")
            row2.prop(sampleProperty, "yuMin")
            row2.prop(sampleProperty, "zuMin")

            row3.prop(sampleProperty, "xvMax")
            row3.prop(sampleProperty, "yvMax")
            row3.prop(sampleProperty, "zvMax")



        if sampleProperty.edgeLocBool == True:
            col4.prop(sampleProperty, "edgeLoc")
            
                #sampleProperty.edgeLoc = (0,0,0)

        if sampleProperty.LocEditBool == True:
            col4.prop(sampleProperty, "LocEdit")

        # invoke custom operator


        col6 = layout.column(align=True)
        row6 = col6.row(align=True)

        # invoke custom operator
        col6.prop(amProperty, "GenMechEnum")
        row6.prop(amProperty, "GenMechMirrorBoll")
        row6.prop(amProperty, "GenMechResizeBoll")
        #row6.prop(amProperty, "GenMechApplyBoll")
        


        col6.operator("object.bl_genmech" , text = "2.Gen Mech")
        col6.operator("object.applymodify" , text = "3.ApplyMechModifiers")
        

