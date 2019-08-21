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

        # row = layout.row()
        # row.prop(context.scene, "export_folder", text="")

        # row = layout.row()
        # row.prop(context.scene, "center_transform", text="Center transform")

        # row = layout.row()
        # row.operator('object.bex_ot_operator', text='Export')

        # row = layout.row()
        # row.operator('object.bex_ot_openfolder', text='Open export folder')
