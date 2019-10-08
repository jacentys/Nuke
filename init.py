# Project Settings > Default format: HD 1920x1080
nuke.knobDefault("Root.format", "HD_1080")
nuke.knobDefault("Root.fps", "25")

# Write > Default for EXR files: 16bit Half, No Compression
#nuke.knobDefault("Write.exr.compression","0")

# Exposure Tool > Use stops instead of densities
nuke.knobDefault("EXPTool.mode", "0")

# Text > Default font: Helvetica Regular (in Dropbox folder)
#nuke.knobDefault("Text.font",   "/Path/to/Dropbox/fonts/HelveticaRegular.   ttf")

# StickyNote > default text size: 40pt
nuke.knobDefault("StickyNote.note_font_size", "32")

# RotoPaint > Set default tool to brush, set default lifetime for brush and clone to "all frames"
nuke.knobDefault("RotoPaint.toolbox", "brush {{brush ltt 0} {clone ltt 0}}")

# Additional Formats
nuke.addFormat("2048 1152 RED_2K 16:9")
nuke.addFormat("4096 2048 RED_4K 2:1")
nuke.addFormat("1024 576 PAL_Wide_SqPix")
nuke.addFormat("5120 2700 RED_EPIC")
nuke.addFormat("2048 858 Arri_Anamorphic 2.387")

import os
user = os.getenv("USER")
userPath = os.path.join("/Library/NukePlugins/Users", user )
if os.path.isdir(userPath):
    nuke.pluginAddPath(userPath)

nuke.pluginAddPath("./Gizmos")
nuke.pluginAddPath("./Python")
nuke.pluginAddPath("./Plugins")
nuke.pluginAddPath("./Plugins/OpticalFlares")
nuke.pluginAddPath("./Gizmos/Other")
nuke.pluginAddPath("./Gizmos/pixelfudger")
nuke.pluginAddPath("./Gizmos/V_Tools")

#
#
#  Copyright (c) 2014, 2015, 2016, 2017 Psyop Media Company, LLC
#  See license.txt
#
#

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte()

