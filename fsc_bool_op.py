import bpy
from bpy.types import Operator

from . fsc_bool_util import *

class FSC_OT_BoolOperator_Union(Operator):
    bl_idname = "object.fsc_bool_union"
    bl_label = "Bool union"
    bl_description = "Union for 2 selected objects" 
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(cls, context):
        return check_cutter_selected(context)

    def invoke(self, context, event):

        target_obj = bpy.context.scene.target_object

        execute_boolean_op(context, target_obj, 1)
 
        return {'FINISHED'}