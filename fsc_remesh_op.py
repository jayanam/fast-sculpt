import bpy
from bpy.types import Operator

from . fsc_bool_util import *

class FSC_OT_Remesh_Operator(Operator):
    bl_idname = "object.fsc_remesh"
    bl_label = "Remesh"
    bl_description = "Voxel remesh operator" 
    bl_options = {'REGISTER', 'UNDO'} 

    def invoke(self, context, event):

        bpy.context.object.data.use_remesh_preserve_volume = context.scene.remesh_preserve_volume
        bpy.context.object.data.use_remesh_smooth_normals = context.scene.remesh_smooth_normals
        bpy.context.object.data.use_remesh_fix_poles = context.scene.remesh_fix_poles
        bpy.context.object.data.remesh_voxel_size = context.scene.remesh_voxel_size
        bpy.ops.object.voxel_remesh()
 
        return {'FINISHED'}