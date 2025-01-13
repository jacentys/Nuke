rootPath = nuke.toNode('Setup').knob('rootPath').getValue()
projektShort = nuke.toNode('Setup').knob('projectShort').getValue()
projektNazwa = nuke.toNode('Setup').knob('projectName').getValue()
numerUjecia = nuke.toNode('Setup').knob('shotNo').getValue()
start = nuke.toNode('Setup').knob('start').getValue()
koniec = nuke.toNode('Setup').knob('koniec').getValue()

layer = nuke.toNode('Setup').knob('layer').value()
if layer == '--':
    layer = ''

odcinek = nuke.thisNode().knob('odcinek').value()
if odcinek != '':
	odcinek = odcinek + '/'

renderNoise = nuke.thisNode().knob('renderNoise').getValue()
if renderNoise == 0:
    nuke.toNode('Write_Noise').knob('disable').setValue(True)
    nuke.toNode('Write_Proxy_Noise').knob('disable').setValue(True)
    nuke.thisNode().knob('noise').setEnabled(False)
    nuke.thisNode().knob('proksyNoise').setEnabled(False)
else:
    nuke.toNode('Write_Noise').knob('disable').setValue(False)
    nuke.toNode('Write_Proxy_Noise').knob('disable').setValue(False)
    nuke.thisNode().knob('noise').setEnabled(True)
    nuke.thisNode().knob('proksyNoise').setEnabled(True)

nazwaPliku = projektShort + '-' + numerUjecia + layer

full = rootPath +'010-Sources-Camera/' + odcinek + nazwaPliku + '/' + nazwaPliku + '.%07d.exr'
proksy = rootPath +'010-Sources-Camera/p/' + odcinek + nazwaPliku + '/' + nazwaPliku + '.%07d.exr'
noise = rootPath +'010-Sources-Camera/n/' + odcinek + nazwaPliku + '/' + nazwaPliku + '.%07d.exr'
proksyNoise = rootPath +'010-Sources-Camera/pn/' + odcinek + nazwaPliku + '/' + nazwaPliku +'.%07d.exr'

nuke.thisNode().knob('full').setValue(full)
nuke.thisNode().knob('proksy').setValue(proksy)
nuke.thisNode().knob('noise').setValue(noise)
nuke.thisNode().knob('proksyNoise').setValue(proksyNoise)

nuke.Root()['first_frame'].setValue(start)
nuke.Root()['last_frame'].setValue(koniec)

#Full
nuke.toNode('Write_Full').knob('file').setValue(full)
nuke.toNode('Write_Full').knob('first').setValue(nuke.toNode('Setup').knob('start').getValue())
nuke.toNode('Write_Full').knob('last').setValue(nuke.toNode('Setup').knob('koniec').getValue())
nuke.toNode('Write_Full').knob('create_directories').setValue(1)
nuke.toNode('Write_Full').knob('use_limit').setValue(1)
nuke.toNode('Write_Full').knob('colorspace').setValue(nuke.toNode('Setup').knob('inputColorSpace').value())
nuke.toNode('Write_Full').knob('interleave').setValue('channels')

#Proxy
nuke.toNode('Write_Proxy').knob('file').setValue(proksy)
nuke.toNode('Write_Proxy').knob('first').setValue(nuke.toNode('Setup').knob('start').getValue())
nuke.toNode('Write_Proxy').knob('last').setValue(nuke.toNode('Setup').knob('koniec').getValue())
nuke.toNode('Write_Proxy').knob('create_directories').setValue(1)
nuke.toNode('Write_Proxy').knob('use_limit').setValue(1)
nuke.toNode('Write_Proxy').knob('colorspace').setValue(nuke.toNode('Setup').knob('inputColorSpace').value())
nuke.toNode('Write_Proxy').knob('interleave').setValue('channels')

#Noise
nuke.toNode('Write_Noise').knob('file').setValue(noise)
nuke.toNode('Write_Noise').knob('first').setValue(start)
nuke.toNode('Write_Noise').knob('last').setValue(koniec)
nuke.toNode('Write_Noise').knob('create_directories').setValue(1)
nuke.toNode('Write_Noise').knob('use_limit').setValue(1)
nuke.toNode('Write_Noise').knob('colorspace').setValue(nuke.thisNode().knob('inputColorSpace').value())
nuke.toNode('Write_Noise').knob('interleave').setValue('channels')

#Proxy Noise
nuke.toNode('Write_Proxy_Noise').knob('file').setValue(proksyNoise)
nuke.toNode('Write_Proxy_Noise').knob('first').setValue(start)
nuke.toNode('Write_Proxy_Noise').knob('last').setValue(koniec)
nuke.toNode('Write_Proxy_Noise').knob('create_directories').setValue(1)
nuke.toNode('Write_Proxy_Noise').knob('use_limit').setValue(1)
nuke.toNode('Write_Proxy_Noise').knob('colorspace').setValue(nuke.thisNode().knob('inputColorSpace').value())
nuke.toNode('Write_Proxy_Noise').knob('interleave').setValue('channels')
