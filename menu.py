# import nuke
# import default
# import default_helper as helper
# 
# default_menu = nuke.menu("Nuke").addMenu("Scripts/default")
# default_menu.addCommand("defaults window", default.show_defaults_window, "", icon="")
# default_menu.addSeparator()
# default_menu.addCommand("about", default.show_about, icon="")
# 
# nuke.menu("Animation").addCommand("default/set as new knobDefault", "default.create_default()")
# nuke.menu("Animation").addCommand("default/show knob list", "default.show_knob_list()")
# nuke.menu("Animation").addCommand("default/reset", "default.reset_to_default()")
# 
# helper.load_knob_defaults(init=True)

# Align Node

nuke.addFormat ("2048 1152 0 0 2048 1152 1.0 2k-16x9")
nuke.addFormat ("1080 1080 0 0 1080 1080 1.0 HD-1x1")
nuke.addFormat ("864 1080 0 0 864 1080 1.0 HD-4x5")
nuke.addFormat ("608 1080 0 0 608 1080 1.0 HD-9x16")

import W_smartAlign
menuBar = nuke.menu("Nuke")
menuBar.addCommand("Edit/Node/Align/Left", 'W_smartAlign.alignNodes("left")', "Alt+left", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Right", 'W_smartAlign.alignNodes("right")', "Alt+right", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Up", 'W_smartAlign.alignNodes("up")', "Alt+up", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Down", 'W_smartAlign.alignNodes("down")', "Alt+down", shortcutContext=2)

import reformat_presets
reformat_presets.nodePresetReformat()
import cam_presets
cam_presets.nodePresetCamera()


# Shortcut Editor
try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()
