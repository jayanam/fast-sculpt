import bpy
from bpy.types import Operator

from mathutils import Vector

from bpy_extras import view3d_utils

from . fsc_select_mode_utils import *

class FSC_OT_Add_Oject_Operator(Operator):
    bl_idname = "object.fsc_add_object"
    bl_label = "Add object"
    bl_description = "Add object in sculpt mode" 
    bl_options = {'REGISTER', 'UNDO'} 

    def invoke(self, context, event):

        scene = context.scene
        active_object = bpy.context.view_layer.objects.active

        if active_object is None or active_object.mode != "SCULPT":
            return {'FINISHED'}

        to_object()
        
        mouse_pos = [event.mouse_region_x, event.mouse_region_y]

        region = context.region
        region3D = context.space_data.region_3d

        # Get intersection and create objects at this location if possible
        view_vector = view3d_utils.region_2d_to_vector_3d(region,   region3D, mouse_pos)
        origin      = view3d_utils.region_2d_to_origin_3d(region,   region3D, mouse_pos)
        loc         = view3d_utils.region_2d_to_location_3d(region, region3D, mouse_pos, view_vector)

        hit, loc_hit, *_ = scene.ray_cast(context.view_layer, origin, view_vector)
        if hit:
            loc = loc_hit

        obj_type = context.scene.add_object_type
      
        # TODO: Add more init options here
        if obj_type == "Sphere":
            bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=loc)
        elif obj_type == "Cube":  
            bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=loc)
        elif obj_type == "Cylinder":
            bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=loc)
        elif obj_type == "Torus":
            bpy.ops.mesh.primitive_torus_add(align='WORLD', location=loc, rotation=(0, 0, 0), major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)
        
        elif obj_type == "Scene":
            custom_obj = context.scene.add_scene_object
            if custom_obj:

                deselect_all()
                make_active(custom_obj)

                bpy.ops.object.duplicate(linked=True)
                clone_custom = bpy.context.view_layer.objects.active
                bpy.ops.object.make_single_user(object=True, obdata=True)

                clone_custom.location = loc

                deselect_all()
                make_active(clone_custom)


        to_sculpt()
 
        return {'FINISHED'}