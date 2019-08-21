bl_info = {
    "name" : "Fast Sculpt",
    "author" : "jayanam",
    "description" : "Sculpting tools for Blender 2.8",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 0),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

import bpy
from bpy.props import *

from . fsc_panel import *
from . fsc_bool_op import *

# Scene properties
bpy.types.Scene.target_object = PointerProperty(type=bpy.types.Object)

classes = ( FSC_PT_Panel, FSC_BoolOperator_Union )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
