import nuke
t=nuke.menu("Nodes")
u=t.addMenu("Post", icon="Post_Menu.png")
t.addCommand( "Post/ColourEdge", "nuke.createNode('ColourEdge')", icon="Post_Menu.png" )
t.addCommand( "Post/Fizzle", "nuke.createNode('fizzle')", icon="Post_Menu.png")
t.addCommand( "Post/FlareFactory", "nuke.createNode('FlareFactory')", icon="Post_Menu.png")
t.addCommand( "Post/iFilter", "nuke.createNode('iFilter')", icon="Post_Menu.png")
t.addCommand( "Post/L_Fuse_v06", "nuke.createNode('L_Fuse_v06')", icon="Post_Menu.png")
t.addCommand( "Post/FibonacciGlow", "nuke.createNode('FibonacciGlow')", icon="FibonacciGlow.png")
t.addCommand( "Post/DespillMadness", "nuke.createNode('DespillMadness')", icon="Post_Menu.png" )
t.addCommand( "Post/GrainMaster", "nuke.createNode('GrainMaster')", icon="Post_Menu.png" )
t.addCommand( "Post/P_Bird", "nuke.createNode('P_Bird')", icon="Post_Menu.png" )
t.addCommand( "Post/HeatWave", "nuke.createNode('HeatWave')", icon="HeatWave_Icon.png")
t.addCommand( "Post/HeatWave", "nuke.createNode('HeatWave')", icon="HeatWave_Icon.png")
t.addCommand( "Post/MatchRackFocus", "nuke.createNode('MatchRackFocus')", icon="Post_Menu.png" )

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui() 
