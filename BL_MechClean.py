import bpy
#bpy.ops.view3d.view_orbit(context,angle=5.0, type='ORBITLEFT')

#bpy.ops.object.editmode_toggle()
#bpy.ops.mesh.select_all(action='TOGGLE')
#bpy.ops.mesh.bisect(plane_co=(0, 0, 10), plane_no=(1, 0, 0), use_fill=False, clear_inner=True, clear_outer=False, xstart=243, xend=243, ystart=349, yend=20)

class MechClean(bpy.types.Operator):
    bl_idname = "object.MechClean"
    bl_label = "Do Mech Clean"
    bl_description = "Just do Mech Clean~Operator" 
    bl_options = {'REGISTER'}

    def __init__(self):
        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D":
                break

        for region in area.regions:
            if region.type == "WINDOW":
                break
        
        self.select_box_up_counter=0
        self.select_box_left_counter = 0
        self.select_box_down_counter = 0
        self.select_box_right_counter = 0

        space = area.spaces[0]

        self.context = bpy.context.copy()
        self.context['area'] = area
        self.context['region'] = region
        self.context['space_data'] = space

    def select_box_up(self):
        self.select_box_up_counter +=1
        print("select_box_up")
        #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITLEFT')
        #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

        bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
        bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
        if self.select_box_up_counter ==51:
            bpy.app.timers.register(select_box_left)
            select_box_up_counter =0
            return None
        return 0.1

    def select_box_left(self):
        self.select_box_left_counter +=1
        print("select_box_left")
        bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITLEFT')
        bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

        #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
        #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
        if self.select_box_left_counter ==51:
            bpy.app.timers.register(select_box_down)
            select_box_left_counter = 0
            return None
        return 0.1

    def select_box_down(self):
        
        self.select_box_down_counter +=1
        print("select_box_down")
        bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITDOWN')
        bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

        #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
        #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
        if self.select_box_down_counter ==51:
            bpy.app.timers.register(select_box_right)
            self.select_box_down_counter = 0
            return None
        return 0.1

    def select_box_right(self):
        
        self.select_box_right_counter +=1
        print("select_box_right")
        bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITRIGHT')
        bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

        #bpy.ops.view3d.view_orbit(context,angle=0.2, type='ORBITUP')
        #bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')
        if self.select_box_right_counter ==51:
            bpy.app.timers.unregister(select_box_up)
            bpy.app.timers.unregister(select_box_left)
            bpy.app.timers.unregister(select_box_down)
            bpy.app.timers.unregister(select_box_right)
            select_box_right_counter = 0
            return None
        return 0.1

    def execute(self, context):


        bpy.ops.view3d.select_box(context,xmin=0, xmax=600, ymin=0, ymax=600, wait_for_input=True, mode='ADD')

        select_box_up_counter = 0
        select_box_left_counter = 0
        select_box_right_counter = 0
        select_box_down_counter = 0

        bpy.app.timers.register(select_box_up)
        if select_box_up_counter ==51:
            bpy.app.timers.register(select_box_left)
        if select_box_left_counter ==51:
            bpy.app.timers.unregister(select_box_left)
            bpy.app.timers.unregister(select_box_up)
            bpy.app.timers.register(select_box_right)
        self.report({'INFO'}, "2.Gen Mech:bpy.ops.object.bl_genmech()")
        return {'FINISHED'}
