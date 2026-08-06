from . import xps_tools
from .modules.ALXModuleManager.ALX_ModuleManager import (
    Alx_Module_Manager,
)

bl_info = {
    "name": "XNALara-io-Tools",
    "author": "Valerie Bosco[Valy Arhal], johnzero7[Original Developer]",
    "description": "Import-Export for XNALara/XPS files",
    "version": (1, 3, 4),
    "blender": (3, 6, 0),
    "category": "Import-Export",
    "location": "File > Import-Export > XNALara/XPS",
    "doc_url": "https://github.com/Valerie-Bosco/XNALara-io-Tools/wiki",
    "tracker_url": "https://github.com/Valerie-Bosco/XNALara-io-Tools/issues",
}

module_manager = Alx_Module_Manager(path=__path__, globals=globals(), mute=True)


def register():
    module_manager.developer_register_modules()

    xps_tools.register()


def unregister():
    module_manager.developer_unregister_modules()

    xps_tools.unregister()


if __name__ == "__main__":
    register()
