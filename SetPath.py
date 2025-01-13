def zaznaczNodSetup():
    nukescripts.clear_selection_recursive()
    n = nuke.toNode("Setup")
    n.knob('selected').setValue(True)

def setVarReadNode(): #### readNode = pierwszy nod w układce
    readConnectedNode = nuke.selectedNode().dependencies()[0]
    readNode = readConnectedNode.name()

def setKnobColorSpace(kolor = 0): #### Odczytaj colorspace i ustaw w zapisywanych
    nuke.toNode('Write_Full').knob('colorspace').setValue(kolor)
    nuke.toNode('Write_Proxy').knob('colorspace').setValue(kolor)
    nuke.toNode('Write_Noise').knob('colorspace').setValue(kolor)
    nuke.toNode('Write_Proxy_Noise').knob('colorspace').setValue(kolor)

def calculateShotName(): #### Stworzenie nazwy pliku
    global nazwaUjecia
    nazwaUjecia = nuke.toNode('Setup').knob('projectShort').value() + '-' + nuke.toNode('Setup').knob('shotNo').getValue()

def setVariableFromSetup():
    global projectShort #### Ustalanie zmiennej projectShort
    projectShort = nuke.toNode('Setup').knob('projectShort').value()

    global episode #### Ustalanie zmiennej episode
    episode = nuke.thisNode().knob('odcinek').value()
    if episode != '':
        episode = '/' + episode

    global numerUjecia #### Ustalanie zmiennej numerUjecia
    numerUjecia = nuke.toNode('Setup').knob('shotNo').getValue()

    global layer #### Ustalanie zmiennej Layer
    layer = nuke.toNode('Setup').knob('layer').value()
    if layer == '--':
        layer = ''

    global nazwaUjecia #### Ustalanie zmiennej nazwaUjecia
    pole = nuke.toNode('Setup').knob('shotName').value()
    if pole == '':
        nazwaUjecia = projectShort + '-' + numerUjecia
        nuke.thisNode().knob('shotName').setValue(nazwaUjecia)
    else:
        nazwaUjecia = pole

    global start #### Ustalanie zmiennej start
    start = nuke.toNode('Setup').knob('start').getValue()

    global koniec #### Ustalanie zmiennej koniec
    koniec = nuke.toNode('Setup').knob('koniec').getValue()

    global nazwaPliku #### Tworzenie nazwy pliku
    nazwaPliku = '/' + nazwaUjecia + layer

    rootPath = nuke.toNode('Setup').knob('rootPath').value()

    global full #### Tworzenie zmiennej pełnej ścieżki FULL
    full = rootPath +'010-Sources-Camera' + episode + nazwaPliku + nazwaPliku + '.%07d.exr'

    global proksy #### Tworzenie zmiennej pełnej ścieżki PROKSY
    proksy = rootPath +'010-Sources-Camera/p' + episode + nazwaPliku + nazwaPliku + '.%07d.exr'

    global noise #### Tworzenie zmiennej pełnej ścieżki NOISE
    noise = rootPath +'010-Sources-Camera/n' + episode + nazwaPliku + nazwaPliku + '.%07d.exr'

    global proksyNoise #### Tworzenie zmiennej pełnej ścieżki PROKSY NOISE
    proksyNoise = rootPath +'010-Sources-Camera/pn' + episode + nazwaPliku + nazwaPliku +'.%07d.exr'

def setSetupKnobs():
    #### Wrzucenie ściezek do pola tekstowego Setup / plików
    global full
    global proksy
    global noise
    global proksyNoise
    nuke.thisNode().knob('full').setValue(full)
    nuke.thisNode().knob('proksy').setValue(proksy)
    nuke.thisNode().knob('noise').setValue(noise)
    nuke.thisNode().knob('proksyNoise').setValue(proksyNoise)

def setFrameRange(start, koniec): #### Ustawienie zakresu compo
    nuke.Root()['first_frame'].setValue(start)
    nuke.Root()['last_frame'].setValue(koniec)

def disableNoise(): #### Wyłączenie noise jeśli niepotrzebny
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

def setWriteNodes():
    #### Ustawienia Write Full
    nuke.toNode('Write_Full').knob('file').setValue(nuke.toNode('Setup').knob('full').value())
    nuke.toNode('Write_Full').knob('first').setValue(nuke.toNode('Setup').knob('start').getValue())
    nuke.toNode('Write_Full').knob('last').setValue(nuke.toNode('Setup').knob('koniec').getValue())
    nuke.toNode('Write_Full').knob('create_directories').setValue(1)
    nuke.toNode('Write_Full').knob('use_limit').setValue(1)
    nuke.toNode('Write_Full').knob('interleave').setValue('channels')

    #### Ustawienia Write Proxy
    nuke.toNode('Write_Proxy').knob('file').setValue(nuke.toNode('Setup').knob('proksy').value())
    nuke.toNode('Write_Proxy').knob('first').setValue(nuke.toNode('Setup').knob('start').getValue())
    nuke.toNode('Write_Proxy').knob('last').setValue(nuke.toNode('Setup').knob('koniec').getValue())
    nuke.toNode('Write_Proxy').knob('create_directories').setValue(1)
    nuke.toNode('Write_Proxy').knob('use_limit').setValue(1)
    nuke.toNode('Write_Proxy').knob('interleave').setValue('channels')

    #### Ustawienia Write Noise
    nuke.toNode('Write_Noise').knob('file').setValue(nuke.toNode('Setup').knob('noise').value())
    nuke.toNode('Write_Noise').knob('first').setValue(start)
    nuke.toNode('Write_Noise').knob('last').setValue(koniec)
    nuke.toNode('Write_Noise').knob('create_directories').setValue(1)
    nuke.toNode('Write_Noise').knob('use_limit').setValue(1)
    nuke.toNode('Write_Noise').knob('interleave').setValue('channels')

    #### Ustawienia Write Proxy Noise
    nuke.toNode('Write_Proxy_Noise').knob('file').setValue(nuke.toNode('Setup').knob('proksyNoise').value())
    nuke.toNode('Write_Proxy_Noise').knob('first').setValue(start)
    nuke.toNode('Write_Proxy_Noise').knob('last').setValue(koniec)
    nuke.toNode('Write_Proxy_Noise').knob('create_directories').setValue(1)
    nuke.toNode('Write_Proxy_Noise').knob('use_limit').setValue(1)
    nuke.toNode('Write_Proxy_Noise').knob('interleave').setValue('channels')

zaznaczNodSetup()
setVarReadNode()
setKnobColorSpace(int(nuke.toNode(readNode).knob('colorspace').getValue()))
setVariableFromSetup()
setSetupKnobs()
setFrameRange(start, koniec)
disableNoise()
setWriteNodes()
