import bpy

def to_object():
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

def to_sculpt():
    bpy.ops.object.mode_set(mode='SCULPT', toggle=False)

def to_edit():
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)

def select_all():
    bpy.ops.object.select_all(action='SELECT')

def deselect_all():
    bpy.ops.object.select_all(action='DESELECT')

def select_mesh():
    bpy.ops.mesh.select_all(action='SELECT')

def deselect_mesh():
    bpy.ops.mesh.select_all(action='DESELECT')

def get_active():
    return bpy.context.view_layer.objects.active

def make_active(obj):

    # API change 2.8: obj.select = True
    obj.select_set(state=True)
    
    # API change 2.8: bpy.context.scene.objects.active = obj
    bpy.context.view_layer.objects.active = obj   

