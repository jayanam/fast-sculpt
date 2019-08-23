import bpy

from bpy.types import Operator

from . fsc_select_mode_utils import *

class FSC_OT_Mask_Extract_Operator(Operator):
    bl_idname = "object.fsc_ot_mask_extract"
    bl_label = "Extract mask"
    bl_description = "Extract a mask as mesh" 
    bl_options = {'REGISTER'}
    
    def invoke(self, context, event):

        target_obj = context.object

        to_sculpt()

        # Invert the mask and hide the masked area
        bpy.ops.paint.mask_flood_fill(mode='INVERT')
        bpy.ops.paint.hide_show(action='HIDE', area='MASKED')

        # select the unmasked part in edit mode and duplicate it
        to_edit()
        select_mesh()
        bpy.ops.mesh.duplicate_move()

        # separate a new object from the selection
        bpy.ops.mesh.separate(type='SELECTED')
        
        # get the new created/separated object
        new_objs = [obj for obj in bpy.context.selected_objects if obj != bpy.context.object]
        new_obj = new_objs[0]

        # unhide the target and get rid of the mask
        to_sculpt()
        bpy.ops.paint.hide_show(action='SHOW', area='ALL')
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0.0)

        # make the new object the active one and extrude it with solidify
        make_active(new_obj)

        solid_mod = new_obj.modifiers.new(type="SOLIDIFY", name="FSC_SOLIDIFY")

        # TODO: Make this configurable
        solid_mod.offset = -0.001
        solid_mod.use_even_offset = True
        solid_mod.use_quality_normals = True

        # Control the thickness with a scene variable
        solid_mod.thickness = context.scene.extract_thickness
        bpy.ops.object.modifier_apply(modifier=solid_mod.name)

        to_sculpt()

        if context.scene.remesh_after_extract:
            bpy.context.object.data.remesh_voxel_size = context.scene.remesh_voxel_size
            bpy.ops.object.voxel_remesh()


        self.report({'INFO'}, "Mask extracted")
        return {'FINISHED'}