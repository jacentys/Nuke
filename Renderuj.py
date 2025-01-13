start = nuke.thisNode().knob('start').getValue()
koniec = nuke.thisNode().knob('koniec').getValue()
writeList =[]
writeList.append(nuke.toNode('Write_Full'))
writeList.append(nuke.toNode('Write_Proxy'))
nuke.executeMultiple(writeList, ((start,koniec,1),(start,koniec,1)))
