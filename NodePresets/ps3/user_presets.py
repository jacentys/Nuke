import nuke
def nodePresetsStartup():
  nuke.setUserPreset("Defocus", "ps3/back", {'defocus': '30', 'ratio': '0.5'})
  nuke.setUserPreset("Defocus", "ps3/na_niego", {'defocus': '40', 'selected': 'true', 'ratio': '0.5'})
  nuke.setUserPreset("Defocus", "ps3/na_przod", {'defocus': '25', 'selected': 'true', 'ratio': '0.5'})
  nuke.setUserPreset("Group15052241136777928917", "ps3/na_tyl", {'Child-1 indicators': '3', 'Child-1 frequency': '0.1', 'Child2 shutter': '0.3', 'Child-1 label': '[value amplitude] px at [value frequency]', 'Child-1 scale': '1.03', 'Child-1 help': 'Add random camera shake, including motion blur.', 'Child-1 amplitude': '40 {amplitude.w*2}', 'Child2 center': '{parent.cs_center} {parent.cs_center}', 'Child-1 cs_center': '{"\\[value input.width 0]/2" 1262} {"\\[value input.height 0]/2" 768}', 'Child2 translate': '{fBm((seed+frame)*frequency,2.5,3.5,octaves,2,.5)*amplitude.w} {fBm((seed+frame)*frequency+100,10.5,11.5,octaves,2,.5)*amplitude.h}', 'Child2 scale': '{(fBm((seed+frame)*frequency,30.5,31.5,octaves,2,.5)*parent.scaling+parent.scale)}', 'Child-1 seed': '12727', 'Child2 rotate': '{fBm((seed+frame)*frequency,20.5,21.5,octaves,2,.5)*parent.rotation}'})
