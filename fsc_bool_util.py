import bpy
from bpy.props import *

import bmesh

from . fsc_select_mode_utils import *

def check_cutter_selected(context):
    result = len(context.selected_objects) > 0
    result = result and not bpy.context.scene.target_object is None
    result = result and not (bpy.context.scene.target_object == bpy.context.view_layer.objects.active)
    return result

def make_active(obj):

    # API change 2.8: obj.select = True
    obj.select_set(state=True)
    
    # API change 2.8: bpy.context.scene.objects.active = obj
    bpy.context.view_layer.objects.active = obj    

def select_active(obj):

    deselect_all()
    
    make_active(obj)

def recalc_normals(mesh):
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(mesh)
    bm.clear()
    mesh.update()
    bm.free()
    
def bool_mod_and_apply(obj, bool_method, allow_delete = True):
    
    active_obj = bpy.context.active_object
    
    bool_mod = active_obj.modifiers.new(type="BOOLEAN", name="FSC_BOOL")
    
    method = 'DIFFERENCE'
    
    if bool_method == 1:
        method = 'UNION'
    
    bool_mod.operation = method
    bool_mod.object = obj

    recalc_normals(obj.data)
    
    bpy.ops.object.modifier_apply(modifier=bool_mod.name)

    select_active(obj)
    bpy.ops.object.delete()


def execute_boolean_op(context, target_obj, bool_method = 0):
    
    '''
    function for bool operation
    @target_obj : target object of the bool operation
    @bool_method : 0 = difference, 1 = union, 2 = intersect  
    ''' 
    current_obj = context.object
    make_active(current_obj)
    to_object()
    bpy.ops.object.transform_apply(scale=True)

    make_active(target_obj)
    to_object()
    bpy.ops.object.transform_apply(scale=True)
  
    bool_mod_and_apply(current_obj, bool_method)

    make_active(target_obj)
    to_sculpt()

    if context.scene.remesh_after_union:
        bpy.context.object.data.remesh_voxel_size = context.scene.remesh_voxel_size
        bpy.ops.object.voxel_remesh()
