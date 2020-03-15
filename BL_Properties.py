import bpy
from bpy.types import Panel,Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty, EnumProperty, BoolProperty
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
        description="Gen Mech Enum Modify",
        items=[
            ('GenMechfy1', "GenMechfy1", ""),
            ('GenMechfy2', "GenMechfyLow", ""),#重构网格=最大50倍 0.1体素  或0.002
            ('GenMechstyle2', "GenMechstyle2", "")
            #('MODE_GD_MARBLE', "大理石 Marble", ""),
            #('MODE_GD_MUSGRAVE', "马斯格雷夫分形 Musgrave", "")
        ],
        default="GenMechfy1"
    )


    GenMechApplyBoll: BoolProperty(
        name="Apply modifiers",
        description="Aoto Apply modifiers",
        default = False
        )

    GenMechResizeBoll: BoolProperty(
        name="Resize",
        description="修改编辑模式下的大小",
        default = False
        )