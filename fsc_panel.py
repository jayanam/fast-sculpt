import bpy
from bpy.types import Panel

class FSC_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Fast Sculpt"
    bl_category = "Fast Sculpt"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Target object:")

        row = layout.row()
        layout.prop_search(context.scene, "target_object", context.scene, "objects", text="Target")

        row = layout.row()
        row.operator('object.fsc_bool_union', text='Union')

        row = layout.row()
        row.label(text="Extract thickness:")
        
        row = layout.row()
        layout.prop(context.scene, "extract_thickness", text="")

        row = layout.row()
        row.operator('object.fsc_ot_mask_extract', text="Extract Mask")

        row = layout.row()
        layout.prop(context.scene, "remesh_after_union", text="Remesh after union")

        row = layout.row()
        layout.prop(context.scene, "remesh_after_extract", text="Remesh after extract")

        row = layout.row()
        layout.prop(context.scene, "remesh_voxel_size", text="Remesh-size")

        row = layout.row()
        row.operator('object.fsc_remesh', text="Remesh")