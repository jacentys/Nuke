import re

readConnectedNode = nuke.selectedNode().dependencies()[0]
readNode = readConnectedNode.name()

def kc_func():
     n = nuke.thisNode()
     k = nuke.thisKnob()
     if k.name() == "inputColorSpace":
          nuke.toNode('Write_Full').knob('colorspace').setValue(thisNode().knob('inputColorSpace').value())
          nuke.toNode('Write_Proxy').knob('colorspace').setValue(nuke.thisNode().knob('inputColorSpace').value())
          nuke.toNode(readNode).knob('colorspace').setValue(nuke.thisNode().knob('inputColorSpace').value())

sel = nuke.selectedNode()
sel.knob('knobChanged').setValue('kc_func()')

plik = nuke.toNode(readNode).knob('file').getValue()
splitted = plik.split('/')
start = nuke.toNode(readNode).knob('first').getValue()
koniec = nuke.toNode(readNode).knob('last').getValue()
dlugosc = koniec - start + 1

nuke.Root()['first_frame'].setValue(start)
nuke.Root()['last_frame'].setValue(koniec)

#Inaczej dla macos, inaczej dla windy
if splitted[1] == "Volumes":
    dysk = splitted[2]
    projektNazwa = splitted[3]
else:
    dysk = splitted[0]
    projektNazwa = splitted[1]

projektShort = projektNazwa.upper()[:3]
ujecie = splitted[len(splitted)-2]

print(projektNazwa)
print(projektShort)
print(ujecie)

layer = nuke.thisNode().knob('layer').value()
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

#Jesli ujecie jest w formacie A000B000
n = re.search('([A-Z][0-9][0-9][0-9][A-Z][0-9][0-9][0-9])', plik)
if n:
    numerUjecia = n.group(1)
    nazwaPliku = numerUjecia + layer
else: #Jesli ujecie jest w formacie AAA-1234
    n = re.search('([A-Z][A-Z][A-Z]-)(\d+)', ujecie)
    if n:
        numerUjecia = n.group(2)
        nazwaPliku = projektShort + '-' + numerUjecia + layer
    else:
        numerUjecia = ujecie
        nazwaPliku = ujecie + layer

#Stworzenie sciezki
if splitted[1] == "Volumes":
    rootPath = '/Volumes/' + dysk + '/' + projektNazwa + '/'
else:
    rootPath = dysk + '/' + projektNazwa + '/'

print(rootPath)

nuke.thisNode().knob('zrodlo').setValue(plik)
nuke.thisNode().knob('dysk').setValue(dysk)
nuke.thisNode().knob('rootPath').setValue(rootPath)
nuke.thisNode().knob('projectName').setValue(projektNazwa)
nuke.thisNode().knob('projectShort').setValue(projektShort)
nuke.thisNode().knob('shotNo').setValue(numerUjecia)
nuke.thisNode().knob('start').setValue(start)
nuke.thisNode().knob('koniec').setValue(koniec)
nuke.thisNode().knob('dlugosc').setValue(dlugosc)

nuke.toNode(readNode).knob('colorspace').setValue(nuke.thisNode().knob('inputColorSpace').value())

full = rootPath +'010-Sources-Camera/' + odcinek + nazwaPliku + '/' + nazwaPliku + '.%07d.exr'
proksy = rootPath +'010-Sources-Camera/p/' + odcinek + nazwaPliku + '/' + nazwaPliku + '.%07d.exr'
noise = rootPath +'010-Sources-Camera/n/' + odcinek + nazwaPliku + '/' + nazwaPliku + '.%07d.exr'
proksyNoise = rootPath +'010-Sources-Camera/pn/' + odcinek + nazwaPliku + '/' + nazwaPliku +'.%07d.exr'

nuke.thisNode().knob('full').setValue(full)
nuke.thisNode().knob('proksy').setValue(proksy)
nuke.thisNode().knob('noise').setValue(noise)
nuke.thisNode().knob('proksyNoise').setValue(proksyNoise)

#Full
nuke.toNode('Write_Full').knob('file').setValue(full)
nuke.toNode('Write_Full').knob('first').setValue(start)
nuke.toNode('Write_Full').knob('last').setValue(koniec)
nuke.toNode('Write_Full').knob('create_directories').setValue(1)
nuke.toNode('Write_Full').knob('use_limit').setValue(1)
nuke.toNode('Write_Full').knob('colorspace').setValue(nuke.thisNode().knob('inputColorSpace').value())
nuke.toNode('Write_Full').knob('interleave').setValue('channels')

#Proxy
nuke.toNode('Write_Proxy').knob('file').setValue(proksy)
nuke.toNode('Write_Proxy').knob('first').setValue(start)
nuke.toNode('Write_Proxy').knob('last').setValue(koniec)
nuke.toNode('Write_Proxy').knob('create_directories').setValue(1)
nuke.toNode('Write_Proxy').knob('use_limit').setValue(1)
nuke.toNode('Write_Proxy').knob('colorspace').setValue(nuke.thisNode().knob('inputColorSpace').value())
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
