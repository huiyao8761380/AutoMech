import bpy
from . BL_GenLine import GenLine
from . BL_GenMech import GenMech
from bpy.types import Panel,Operator


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
        # invoke custom operator
        row.operator("object.bl_genline" , text = "1.Gen Line")

        col = layout.column(align=True)
        row = col.row(align=True)
        # invoke custom operator
        row.operator("object.bl_genmech" , text = "2.Gen Mech")
