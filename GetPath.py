import re

def selectSetupNode():
    nukescripts.clear_selection_recursive()
    n = nuke.toNode("Setup")
    n.knob('selected').setValue(True)

def setReadToVarreadNode(): #### readNode = pierwszy nod w układce
    global readNode
    readConnectedNode = nuke.selectedNode().dependencies()[0]
    readNode = readConnectedNode.name()


def findShotNumber(projectShort, file): #### Szukaj numeru ujęcia w nazwie pliku
    n = re.search('([A-Z][0-9][0-9][0-9][A-Z][0-9][0-9][0-9])', file)
    if n:
        shotNo = n.group(1)
        fileName = shotNo
    else: #Jesli ujecie jest w formacie AAA-1234
        n = re.search('([A-Z][A-Z][A-Z]-)(\d+)', file)
        if n:
            shotNo = n.group(2)
            fileName = projectShort + '-' + shotNo
        else:
            shotNo = file
            fileName = file
    return [shotNo, fileName]

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

def getVarFromRead(): #### Odczytaj dane o sekwencji z Read
    global knobVariable
    filePath = nuke.toNode(readNode).knob('file').getValue()
    filePathSplitted = filePath.split('/')
    fileName = filePathSplitted[len(filePathSplitted)-2]
    fileStart = int(nuke.toNode(readNode).knob('first').getValue())
    fileEnd = int(nuke.toNode(readNode).knob('last').getValue())
    fileLength = fileEnd - fileStart + 1

    if filePathSplitted[1] == "Volumes": #### Sprawdzanie jaka ścieżka dostępu.
        os = 0 # MacOS, Lunux
    else:
        os = 1 # Winda

    if os == 0: #### Inaczej dla macos, inaczej dla windy - ścieżki dostępu
        dysk = filePathSplitted[2]
        projectName = filePathSplitted[3]
        rootPath = '/Volumes/' + dysk + '/' + projectName + '/'
    else:
        dysk = filePathSplitted[0]
        projectName = filePathSplitted[1]
        rootPath = dysk + '/' + projectName + '/'
    projectShort = projectName.upper()[:3]

    shotNo = findShotNumber(projectShort, fileName)[0]
    fileName =  findShotNumber(projectShort, fileName)[1]

    #### Odczytaj colorspace i ustaw w zapisywanych
    fileColorSpace = int(nuke.toNode(readNode).knob('colorspace').getValue())
    nuke.toNode('Write_Full').knob('colorspace').setValue(fileColorSpace)
    nuke.toNode('Write_Proxy').knob('colorspace').setValue(fileColorSpace)
    nuke.toNode('Write_Noise').knob('colorspace').setValue(fileColorSpace)
    nuke.toNode('Write_Proxy_Noise').knob('colorspace').setValue(fileColorSpace)

    #### Ustaw początek i koniec globalny
    nuke.Root()['first_frame'].setValue(fileStart)
    nuke.Root()['last_frame'].setValue(fileEnd)

    knobVariable = [filePath, fileName, fileStart, fileEnd, fileLength, fileColorSpace, dysk, rootPath, projectName, projectShort, shotNo]
    #, pathFull, pathNoise, pathProxy, pathProxyNoise]

    print(knobVariable)


def setSetupKnobsValue(): #### Wprowadź w pola dane
    nuke.thisNode().knob('zrodlo').setValue(knobVariable[0])

    nuke.thisNode().knob('start').setValue(knobVariable[2])
    nuke.thisNode().knob('koniec').setValue(knobVariable[3])
    nuke.thisNode().knob('dlugosc').setValue(knobVariable[4])

    nuke.thisNode().knob('dysk').setValue(knobVariable[6])
    nuke.thisNode().knob('rootPath').setValue(knobVariable[7])
    nuke.thisNode().knob('projectName').setValue(knobVariable[8])
    nuke.thisNode().knob('projectShort').setValue(knobVariable[9])
    nuke.thisNode().knob('shotNo').setValue(knobVariable[10])

    episode = nuke.thisNode().knob('odcinek').value()
    if episode != '':
        episode = '/' + episode

    layer = nuke.toNode('Setup').knob('layer').value()
    if layer == '--':
        layer = ''

    rootPath = nuke.toNode('Setup').knob('rootPath').value()
    shotName = nuke.toNode('Setup').knob('projectShort').value() + '-' + nuke.toNode('Setup').knob('shotNo').value()
    nuke.thisNode().knob('shotName').setValue(shotName)

    pathFull = rootPath +'010-Sources-Camera' + episode + '/' + shotName + layer + '/' + shotName + layer + '.%07d.exr'
    nuke.thisNode().knob('full').setValue(pathFull)
    pathProxy = rootPath +'010-Sources-Camera/p' + episode + '/' + shotName + layer + '/' + shotName + layer + '.%07d.exr'
    nuke.thisNode().knob('proksy').setValue(pathProxy)
    pathNoise = rootPath +'010-Sources-Camera/n' + episode + '/' + shotName + layer + '/' + shotName + layer + '.%07d.exr'
    nuke.thisNode().knob('noise').setValue(pathNoise)
    pathProxyNoise = rootPath +'010-Sources-Camera/pn' + episode + '/' + shotName + layer + '/' + shotName + layer +'.%07d.exr'
    nuke.thisNode().knob('proksyNoise').setValue(pathProxyNoise)

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
    nuke.toNode('Write_Noise').knob('first').setValue(nuke.toNode('Setup').knob('start').getValue())
    nuke.toNode('Write_Noise').knob('last').setValue(nuke.toNode('Setup').knob('koniec').getValue())
    nuke.toNode('Write_Noise').knob('create_directories').setValue(1)
    nuke.toNode('Write_Noise').knob('use_limit').setValue(1)
    nuke.toNode('Write_Noise').knob('interleave').setValue('channels')

    #### Ustawienia Write Proxy Noise
    nuke.toNode('Write_Proxy_Noise').knob('file').setValue(nuke.toNode('Setup').knob('proksyNoise').value())
    nuke.toNode('Write_Proxy_Noise').knob('first').setValue(nuke.toNode('Setup').knob('start').getValue())
    nuke.toNode('Write_Proxy_Noise').knob('last').setValue(nuke.toNode('Setup').knob('koniec').getValue())
    nuke.toNode('Write_Proxy_Noise').knob('create_directories').setValue(1)
    nuke.toNode('Write_Proxy_Noise').knob('use_limit').setValue(1)
    nuke.toNode('Write_Proxy_Noise').knob('interleave').setValue('channels')

selectSetupNode()
setReadToVarreadNode()
getVarFromRead()
disableNoise()
setSetupKnobsValue()
setWriteNodes()
