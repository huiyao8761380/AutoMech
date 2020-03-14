import bpy
from . BL_GenLine import GenLine 
from . BL_GenMech import GenMech
from . BL_EdgesGen import EdgesGen
from bpy.types import Panel,Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty
from . BL_Properties import AMProperties


class AutoMechPanel(bpy.types.Panel):
    bl_label = "Auto Mech"
    bl_idname = "Auto_Mech_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AutoMech'

    def draw(self, context):
        layout = self.layout
        #col = layout.column(align=True)
        row = layout.row(align=True)

        sampleProperty = bpy.context.scene.sampleProperty
        amProperty = context.scene.amProperties

        #col.prop(sampleProperty, "edgeName")
        row.prop(sampleProperty, "edgeMin")
        row.prop(sampleProperty, "edgeMax")
        row.prop(sampleProperty, "edgeVNumber")

        #col5 = layout.column(align=True)
        row5 = layout.row(align=True)

        row5.prop(sampleProperty, "edgeXYZ")
        row5.prop(sampleProperty, "edgeLocBool")
        row5.prop(sampleProperty, "LocEditBool")

        #col2 = layout.column(align=True)
        row2 = layout.row(align=True)
        #col3 = layout.column(align=True)
        row3 = layout.row(align=True)

        if sampleProperty.edgeXYZ == True:
            row2.prop(sampleProperty, "xuMin")
            row2.prop(sampleProperty, "yuMin")
            row2.prop(sampleProperty, "zuMin")

            row3.prop(sampleProperty, "xvMax")
            row3.prop(sampleProperty, "yvMax")
            row3.prop(sampleProperty, "zvMax")

        col4 = layout.column()
        #row4 = col4.row(align=True)

        if sampleProperty.edgeLocBool == True:
            col4.prop(sampleProperty, "edgeLoc")#row4
        
            #sampleProperty.edgeLoc = (0,0,0)

        if sampleProperty.LocEditBool == True:
            col4.prop(sampleProperty, "LocEdit")

        # invoke custom operator
        #col = layout.column(align=True)
        col4.operator("object.bl_genline" , text = "1.Gen Line")

        col6 = layout.column(align=True)
        row6 = col6.row(align=True)

        #row6.prop(amProperty, "GenMechMirrorBoll")
        
        col6.operator("object.bl_genmech" , text = "2.Gen Mech")

