start = nuke.thisNode().knob('start').getValue()
koniec = nuke.thisNode().knob('koniec').getValue()

renderNoise = nuke.thisNode().knob('renderNoise').getValue()
if renderNoise == 0:
  writeList =[]
  writeList.append(nuke.toNode('Write_Full'))
  writeList.append(nuke.toNode('Write_Proxy'))
  nuke.executeMultiple(writeList, ((start,koniec,1),(start,koniec,1)))
else:
  writeList =[]
  writeList.append(nuke.toNode('Write_Full'))
  writeList.append(nuke.toNode('Write_Proxy'))
  writeList.append(nuke.toNode('Write_Noise'))
  writeList.append(nuke.toNode('Write_Proxy_Noise'))
  nuke.executeMultiple(writeList, ((start,koniec,1),(start,koniec,1)))
