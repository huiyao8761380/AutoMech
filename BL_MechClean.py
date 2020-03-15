import bpy
from bpy.types import Operator,PropertyGroup
from bpy.props import FloatProperty, PointerProperty,StringProperty
#from . BL_Tool import *
from . BL_Panel import * #
#bpy.ops.view3d.view_orbit(context,angle=5.0, type='ORBITLEFT')

#bpy.ops.object.editmode_toggle()
#bpy.ops.mesh.select_all(action='TOGGLE')
#bpy.ops.mesh.bisect(plane_co=(0, 0, 10), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=243, xend=243, ystart=349, yend=20)

class MechClean(bpy.types.Operator):
    bl_idname = "object.mechclean"
    bl_label = "Do Mech Clean"
    bl_description = "Just do Mech Clean~Operator" 
    bl_options = {'REGISTER'}

    
    def __init__(self):

        
        self.select_box_up_counter=0
        self.select_box_left_counter = 0
        self.select_box_down_counter = 0
        self.select_box_right_counter = 0

        self.context = bpy.context.copy()

    def select_box_up(self):
        self.select_box_up_counter +=1
        print("select_box_up")
        bpy.ops.view3d.view_orbit(self.context,angle=0.2, type='ORBITUP')
        bpy.ops.view3d.select_box(self.context,xmin=0, xmax=1080, ymin=0, ymax=1080, wait_for_input=True, mode='ADD')
        if self.select_box_up_counter ==31:
            bpy.app.timers.register(self.select_box_left)
            #select_box_up_counter =0
            return None
        return 0.1

    def select_box_left(self):
        self.select_box_left_counter +=1
        print("select_box_left")
        bpy.ops.view3d.view_orbit(self.context,angle=0.2, type='ORBITLEFT')
        bpy.ops.view3d.select_box(self.context,xmin=0, xmax=1080, ymin=0, ymax=1080, wait_for_input=True, mode='ADD')
        if self.select_box_left_counter ==31:
            bpy.app.timers.register(self.select_box_down)
            #select_box_left_counter = 0
            return None
        return 0.1

    def select_box_down(self):
        self.select_box_down_counter +=1
        print("select_box_down")
        bpy.ops.view3d.view_orbit(self.context,angle=0.2, type='ORBITDOWN')
        bpy.ops.view3d.select_box(self.context,xmin=0, xmax=1080, ymin=0, ymax=1080, wait_for_input=True, mode='ADD')
        if self.select_box_down_counter ==31:
            bpy.app.timers.register(self.select_box_right)
            #self.select_box_down_counter = 0
            return None
        return 0.1

    def select_box_right(self):
        self.select_box_right_counter +=1
        print("select_box_right")
        bpy.ops.view3d.view_orbit(self.context,angle=0.2, type='ORBITRIGHT')
        bpy.ops.view3d.select_box(self.context,xmin=0, xmax=1080, ymin=0, ymax=1080, wait_for_input=True, mode='ADD')
        if self.select_box_right_counter ==31:
            bpy.ops.mesh.hide(unselected=False)
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete(type='ONLY_FACE')
            bpy.ops.mesh.reveal()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.delete(type='EDGE_FACE')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.app.timers.unregister(self.select_box_up)
            bpy.app.timers.unregister(self.select_box_left)
            bpy.app.timers.unregister(self.select_box_down)
            bpy.app.timers.unregister(self.select_box_right)
            #select_box_right_counter = 0
            return None
        return 0.1
    

    def execute(self, context):

        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D":
                break

        for region in area.regions:
            if region.type == "WINDOW":
                break

        space = area.spaces[0]

        context = bpy.context.copy()
        context['area'] = area
        context['region'] = region
        context['space_data'] = space

        sel = bpy.context.selected_objects
        for ob in sel:
            bpy.context.view_layer.objects.active = ob
            #bpy.ops.view3d.localview(context)
            #ob.mode_set(mode='EDIT')
            #bpy.ops.mesh.select_all(action='DESELECT')

            self.select_box_up_counter = 0
            self.select_box_left_counter = 0
            self.select_box_right_counter = 0
            self.select_box_down_counter = 0
            #MechClean = MechClean()
            bpy.app.timers.register(self.select_box_up)
            if self.select_box_right_counter == 31:
                bpy.app.timers.unregister(self.select_box_right)
                #ob.mode_set(mode='OBJECT')
                '''
                bpy.ops.mesh.hide(unselected=False)
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.delete(type='ONLY_FACE')
                bpy.ops.mesh.reveal()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT', action='TOGGLE')
                bpy.ops.mesh.select_all(action='INVERT')
                bpy.ops.mesh.delete(type='EDGE_FACE')
                bpy.ops.object.mode_set(mode='OBJECT')
                '''
            #bpy.ops.view3d.localview(context)
            
        '''if self.select_box_up_counter ==51:
            bpy.app.timers.register(self.select_box_left)
        if self.select_box_left_counter ==51:
            bpy.app.timers.unregister(self.select_box_left)
            bpy.app.timers.unregister(self.select_box_up)
            bpy.app.timers.register(self.select_box_right)
        
        bpy.app.timers.register(select_box_up)
        if select_box_up_counter ==51:
            bpy.app.timers.register(select_box_left)
        if select_box_left_counter ==51:
            bpy.app.timers.unregister(select_box_left)
            bpy.app.timers.unregister(select_box_up)
            bpy.app.timers.register(select_box_right)
        '''
        self.report({'INFO'}, "2.Gen Mech:bpy.ops.object.bl_genmech()")
        return {'FINISHED'}


        #bpy.ops.view3d.select_box(context,xmin=0, xmax=1080, ymin=0, ymax=1080, wait_for_input=True, mode='ADD')


