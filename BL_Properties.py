import bpy
from bpy.types import Panel,Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty, EnumProperty, BoolProperty, FloatVectorProperty
from . BL_Tool import *
'''
import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import *

#from bpy.types import PropertyGroup
#from bpy.props import FloatProperty, PointerProperty,StringProperty

from . BL_Panel import *
from . BL_GenLine import GenLine
from . BL_GenMech import GenMech
from . BL_EdgesGen import EdgesGen

from bpy.types import Panel,Operator,PropertyGroup
'''


class AMProperties(PropertyGroup):

    GenLineEnum: EnumProperty(
        name="GenLineEnum",
        description="GenLineEnum",
        items=[
            ('GenLineOnly', "GenLineOnly", ""),
            ('GenLineMechBody', "Custom GenLineMechBody", ""),
            ('GenLineStruct', "GenLineStruct", ""),
            ('GenLineKit', "GenLineKit", ""),
            ('GenLineWeapon', "GenLineWeapon", "")
            #('MODE_GD_MARBLE', "大理石 Marble", ""),
            #('MODE_GD_MUSGRAVE', "马斯格雷夫分形 Musgrave", "")
        ],
        default="GenLineOnly"
    )

    GenMechMirrorBoll: BoolProperty(
        name="Mirror",
        description="允许增加一个镜像修改器 Allow the addition of a mirror modifier",
        default = True
        )

    GenMechEnum: EnumProperty(
        name="GenMechEnum",
        description="Gen Mech Enum Modifier",
        items=[
            ('GenMechfy1', "GenMechfyHigh", "Higher Mesh"),
            ('GenMechfy2', "GenMechfyLow", "Lower Mesh"),#重构网格=最大50倍 0.1体素  或0.002
            ('GenMechSpike', "GenMechSpike", "Multiple Modifier reference form Spike")
            #('MODE_GD_MARBLE', "大理石 Marble", ""),
            #('MODE_GD_MUSGRAVE', "马斯格雷夫分形 Musgrave", "")
        ],
        default="GenMechSpike"
    )


    GenMechApplyBoll: BoolProperty(
        name="Apply modifiers",
        description="Aoto Apply modifiers",
        default = False
        )

    GenMechBemeshClean: BoolProperty(
        name="Bemesh Clean",
        description="Bemesh Clean1.1",
        default = False
        )

    GenMechUVPackmaster: BoolProperty(
        name="UVPackmaster",
        description="UVPackmaster2.3.2",
        default = False
        )

    GenMechRemeshEnum: EnumProperty(
        name="RemeshEnum",
        description="Gen Mech Remesh Enum Modify",
        items=[
            ('BLOCKS', 'BLOCKS', ""),
            ('SMOOTH', 'SMOOTH', ""),
            ('SHARP', 'SHARP', "")

        ],
        default='SMOOTH',
        update=RemeshEnum_update
    )


    GenMechBevel0Enum:EnumProperty(
        name="Bevel0Enum",
        description="Gen Mech Bevel0 Enum Modify",
        items=GenMechBevel0Enum_callback,
        options={'ANIMATABLE'},
        #default= bpy.context.object.modifiers["Bevel"].offset_type
        update=GenMechBevel0Enum_update

        #get=get_Bevel0Enum
        #set=set_Bevel0Enum
    )

    '''
    GenMechBevel0float:FloatProperty(
        name="width_pct",
        description="Gen Mech Bevel0 width_pct Modify",
        default=37,
        min=0,
        amx=100,
        #options={'ANIMATABLE'},
        #update=GenMechBevel0float_update
    )
    '''


    GenMechResizeBoll: BoolProperty(
        name="Resize",
        description="修改编辑模式下的大小",
        default = False
        )

    GenMechResize: FloatVectorProperty(
        name="size",
        description="修改编辑模式下的大小",
        default = (1,1,1),
        step=10,
        update=GenMechResize_update
        #set=set_GenMechResize
        )

    GenMechSkinSizeBool: BoolProperty(
        name="Skin Size",
        description="修改编辑模式下的大小",
        default = False
        )

    GenMechSkinResize: FloatVectorProperty(
        name="Skin modifier Size",
        description="修改编辑模式下蒙皮修改器的大小",
        default = (1,1,1),
        update=GenMechSkinResize_update
        )

    GenMechRemeshScale: FloatProperty(
        name="Remesh Scale",
        description="修改重构网格的缩放大小",
        default = 0.88,
        min=0,
        max=0.99,
        step=0.1,
        update=GenMechRemeshScale_update
        )

        #FloatProperty(name="width_pct", default=37, min=0, max=0.99