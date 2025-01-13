import nuke
def nodePresetsStartup():
  nuke.setUserPreset("Group9189515164408528731", "Sara/Noc", {'Child72 label': 'RED', 'Child75 label': 'BLUE', 'Child2 channels': '-rgba.red rgba.green -rgba.blue none', 'Child12 channels': 'rgba', 'Child3 channels': 'rgba.red -rgba.green -rgba.blue none', 'Child9 to0': 'rgba.red', 'Child1 channels': '-rgba.red -rgba.green rgba.blue none', 'Child-1 selected': 'true', 'Child83 which': '{"\\[python nuke.thisNode()\\\\\\[\'switch_luminance\'\\\\].value()]" i}', 'Child50 help': 'Adds synthetic grain. Push "presets" to get predefined types of grain, these are the correct size for 2K scans.\n\nYou can also adjust the sliders to match a sample piece of grain. Find a sample with a rather constant background, blur it to remove the grain, and use as input to this. View with a wipe in the viewer so you can make a match. It helps to view and match each of the red, green, blue separately.', 'Child47 channels': 'rgba.red -rgba.green -rgba.blue none', 'Child11 box': '{Input1.bbox.x i} {Input1.bbox.y i} {Input1.bbox.r i} {Input1.bbox.t i}', 'Child6 channels': '-rgba.red -rgba.green rgba.blue none', 'Child84 switch_blur': 'true', 'Child4 channels': 'rgba.red -rgba.green -rgba.blue none', 'Child87 which': '{"\\[python nuke.thisNode()\\\\\\[\'switch_preview\'\\\\].value()]" i}', 'Child84 which': '{"\\[python -execlocal ret\\\\ =\\\\ nuke.thisNode()\\\\\\[\'switch_blur\'\\\\].value()]" i}', 'Child50 green_size': '0.4', 'Child70 channels': 'rgba.red -rgba.green -rgba.blue none', 'Child85 which': '{"\\[python nuke.thisNode()\\\\\\[\'switch_mask\'\\\\].value()]" i}', 'Child1 size': '3 1.3', 'Child86 which': '{"\\[python -execlocal ret\\\\ =\\\\ nuke.thisNode()\\\\\\[\'switch_grade\'\\\\].value()]" i}', 'Child5 channels': '-rgba.red rgba.green -rgba.blue none', 'Child77 label': 'BLUE', 'Child82 which': '{"\\[python -execlocal switch\\\\ =\\\\ nuke.thisNode()\\\\nx\\\\ =\\\\ switch\\\\\\[\'grain_list\'\\\\].values()\\\\ny\\\\ =\\\\ x.index(switch\\\\\\[\'grain_list\'\\\\].value())\\\\nret\\\\ =\\\\ y\\\\n]" i}', 'Child71 channels': '-rgba.red -rgba.green rgba.blue none', 'Child3 size': '3 1.3', 'Child64 label': 'Create Grain', 'Child80 in2': 'alpha', 'Child0 channels': 'alpha', 'Child12 label': 'Blacks', 'Child2 size': '2 1', 'Child49 channels': '-rgba.red -rgba.green rgba.blue none', 'Child9 from0': 'rgba.red', 'Child46 channels': '-rgba.red rgba.green -rgba.blue none', 'Child69 channels': '-rgba.red rgba.green -rgba.blue none', 'Child-1 note_font': 'Helvetica', 'Child50 label': 'other', 'Child74 label': 'GREEN', 'Child88 which': '{"\\[python -execlocal ret\\\\ =\\\\ nuke.thisNode()\\\\\\[\'switch_clamp\'\\\\].value()]" i}', 'Child73 label': 'GREEN', 'Child89 which': '{"\\[python -execlocal ret\\\\ =\\\\ nuke.thisNode()\\\\\\[\'switch_sharpen\'\\\\].value()]" i}', 'Child10 channels': 'rgb', 'Child78 label': 'RED', 'Child8 from0': 'rgba.green', 'Child8 to0': 'rgba.green', 'Child10 maskChannelInput': 'rgba.alpha'})
