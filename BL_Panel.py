import bpy
from . BL_GenLine import GenLine 
from . BL_GenMech import GenMech
from . BL_EdgesGen import EdgesGen
from . BL_Properties import AMProperties
from . BL_Tool import *
from . BL_MechClean import MechClean
from . BL_AddRig import AddRig
from . BL_BindRig import BindRig
from . BL_WeightRig import WeightRig

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
        obj = context.object

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

        
        col6.prop(amProperty, "GenMechEnum")
        row6.prop(amProperty, "GenMechMirrorBoll")
        row6.prop(amProperty, "GenMechResizeBoll")

        if amProperty.GenMechResizeBoll == True:
            col6.prop(amProperty, "GenMechResize")
            
        row6.prop(amProperty, "GenMechSkinSizeBool")

        if amProperty.GenMechSkinSizeBool == True:
            col6.prop(amProperty, "GenMechSkinResize")
        


        #GenMechRemeshEnum
        #row8.prop(amProperty, "GenMechRemeshEnum")

        #row6.prop(amProperty, "GenMechApplyBoll")
        
        col7 = layout.column(align=True)
        row7 = col7.row(align=True)

        col8 = layout.column(align=True)
        row8 = col8.row(align=True)
        col6.prop(amProperty, "GenMechRemeshEnum")
        col6.prop(amProperty, "GenMechRemeshScale")#
        col6.prop(amProperty, "GenMechBevel0Enum")
        if amProperty.GenMechBevel0Enum =='PERCENT':
            col6.prop(sampleProperty, "Bevel0float")

        col6.operator("object.bl_genmech" , text = "2.Gen Mech")
        col7.operator("am.applymodify" , text = "3.ApplyMechModifiers")
        col7.operator("object.mechclean" , text = "4.MechClean(Edit)")

        row7.prop(amProperty, "GenMechBemeshClean")
        row7.prop(amProperty, "GenMechUVPackmaster")
        row7.operator("am.rename" , text = "ReName")

        col7.operator("object.applyclean" , text = "5.ApplyClean(Edit)")
        col7.operator("am.mirrorselect" , text = "6.MirrorSelect")
        
        col8.operator("aw.addrig" , text = "7.AddRig(Rigify)")
        col8.operator("aw.bindrig" , text = "8.BindAllRig")
        col8.operator("aw.weightrig" , text = "9.WeightRig")

