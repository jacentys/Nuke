import re

plik = nuke.selectedNode().knob('file').getValue()
start = nuke.selectedNode().knob('first').getValue()
koniec = nuke.selectedNode().knob('last').getValue()

m = re.search('/[A-Z][A-Z][A-Z]-(\d\d\d\d).*/', plik)
if m:
    shotNum = m.group(1)

nuke.toNode('Setup').knob('zrodlo').setValue(plik)
nuke.toNode('Setup').knob('start').setValue(start)
nuke.toNode('Setup').knob('koniec').setValue(koniec)
nuke.toNode('Setup').knob('shotNo').setValue(shotNum)

nuke.selectedNode().knob('colorspace').setValue('sRGB')

full = 'P:/Marusarz_21015_Besta/010-Sources-Camera/MAR-'+shotNum+'/MAR-'+shotNum+'.%07d.exr'
proksy = 'P:/Marusarz_21015_Besta/010-Sources-Camera/p/MAR-'+shotNum+'/MAR-'+shotNum+'.%07d.exr'

nuke.thisNode().knob('full').setValue(full)
nuke.thisNode().knob('proksy').setValue(proksy)

#Full
nuke.toNode('Write_Full').knob('file').setValue(full)
nuke.toNode('Write_Full').knob('first').setValue(start)
nuke.toNode('Write_Full').knob('last').setValue(koniec)
nuke.toNode('Write_Full').knob('create_directories').setValue(1)
nuke.toNode('Write_Full').knob('use_limit').setValue(1)
nuke.toNode('Write_Full').knob('colorspace').setValue('linear')
nuke.toNode('Write_Full').knob('interleave').setValue('channels')

#Proxy
nuke.toNode('Write_Proxy').knob('file').setValue(proksy)
nuke.toNode('Write_Proxy').knob('first').setValue(start)
nuke.toNode('Write_Proxy').knob('last').setValue(koniec)
nuke.toNode('Write_Full').knob('create_directories').setValue(1)
nuke.toNode('Write_Full').knob('use_limit').setValue(1)
nuke.toNode('Write_Full').knob('colorspace').setValue('linear')
nuke.toNode('Write_Full').knob('interleave').setValue('channels')

print(full)
print(proksy)
