bl_info = {
    "name" : "Fast Sculpt",
    "author" : "jayanam",
    "description" : "Sculpting tools for Blender 2.8",
    "blender" : (2, 80, 0),
    "version" : (0, 3, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

import bpy
from bpy.props import *

from . fsc_panel import *
from . fsc_bool_op import *
from . fsc_mask_op import *
from . fsc_remesh_op import *

# Scene properties
bpy.types.Scene.target_object = PointerProperty(type=bpy.types.Object)

bpy.types.Scene.extract_thickness = bpy.props.FloatProperty( name="Extract thickness", 
                                      description="Thickness of the extracted mesh",
                                      default = 0.1)

bpy.types.Scene.remesh_voxel_size = bpy.props.FloatProperty( name="Remesh voxel size", 
                                      description="Voxel size of remesh",
                                      default = 0.08)

bpy.types.Scene.remesh_after_extract  = BoolProperty(name="Remesh after extract", 
                                      description="Remesh the mesh after mask extraction",
                                      default = True)

bpy.types.Scene.remesh_after_union  = BoolProperty(name="Remesh after union", 
                                      description="Remesh the mesh after union operation",
                                      default = True)


classes = ( FSC_PT_Panel, FSC_BoolOperator_Union, 
            FSC_OT_Mask_Extract_Operator, FSC_Remesh_Operator )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
