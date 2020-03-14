#import bpy
#from bpy.types import Panel,Operator,PropertyGroup
#from bpy.props import FloatProperty, PointerProperty, EnumProperty, BoolProperty

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



class AMProperties(PropertyGroup):

    GenLineEnum: EnumProperty(
        name="GenLineEnum",
        description="GenLineEnum",
        items=[
            ('GenLineOnly', "GenLineOnly", ""),
            ('GenLineMechBody', "GenLineMechBody", "")
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
            ('GenMechfy1', "Gen Mechfy style 1", ""),
            ('GenLineMechBody', "GenLineMechBody", "")
            #('MODE_GD_MARBLE', "大理石 Marble", ""),
            #('MODE_GD_MUSGRAVE', "马斯格雷夫分形 Musgrave", "")
        ],
        default="GenMechfy1"
    )