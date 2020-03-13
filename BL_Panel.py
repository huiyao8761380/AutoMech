import bpy
from . BL_GenLine import GenLine 
from . BL_GenMech import GenMech
from . BL_EdgesGen import EdgesGen

from bpy.types import Panel,Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty


'''
SamplePropertyGroup = type(
    "SamplePropertyGroup",
    (PropertyGroup,),
    {
        "sigma": FloatProperty(name="σ", default=10.0),
        "x": FloatProperty(name="scale_X", default=1.0),
        "y": FloatProperty(name="scale_Y", default=1.0),
        "z": FloatProperty(name="scale_Z", default=1.0)
    })
'''

class AutoMechPanel(bpy.types.Panel):
    bl_label = "Auto Mech"
    bl_idname = "Auto_Mech_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AutoMech'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=True)

        sampleProperty = context.scene.samplePropertyGroup

        col.prop(sampleProperty, "edgeName")
        col.prop(sampleProperty, "edgeMin")
        col.prop(sampleProperty, "edgeMax")
        col.prop(sampleProperty, "edgeVNumber")
        # invoke custom operator
        col = layout.column(align=True)
        row.operator("object.bl_genline" , text = "1.Gen Line")


        row = col.row(align=True)
        # invoke custom operator
        row.operator("object.bl_genmech" , text = "2.Gen Mech")

        

