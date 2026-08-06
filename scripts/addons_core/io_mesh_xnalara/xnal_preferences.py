import bpy


class XNAlaraMesh4X_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context: bpy.types.Context):
        layout = self.layout
