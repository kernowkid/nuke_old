
# import Python scripts and/or Python Modules - i.e.:    import myPythonScript
import nuke
import opendir
import Victor_Toolset
import camFromMeta_05
import animatedSnap3D
import backdropWithLabel
import localizeSelectedReads
#import changeVersion


# add format resolutions presets - i.e.:    nuke.addFormat ('1920 797 0 0 1920 797 1.0 FullHD_Widescreen')



# add LUT to the Root - i.e.:    nuke.root().knob('luts').addCurve('nameOfTheLUT', 'formula')    # sLOG formula example: '{pow(10.0, ((t - 0.616596 - 0.03) /0.432699)) - 0.037584}'



# customise menu items from Nodes toolbar - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'j', icon='Shuffle.png')
# set hotkey for an existing menu item - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').findItem('Channel').findItem('Shuffle').setShortcut('j')
menubar = nuke.menu('Nuke')
toolbar = nuke.menu('Nodes')

m = menubar.addMenu('Plugs')
m.addCommand('Python/Create Camera From Meta ','camFromMeta_05.ExrToCamera()', 'alt+c', icon='Camera.png')
m.addCommand('Python/Open Selected Read in OS File Browser', 'opendir.openInExplorer()', 'shift+alt+e', icon='Read.png')
m.addCommand('Python/Version up', 'changeVersion.versionUp()', 'alt+]')
m.addCommand('Python/Version  down', 'changeVersion.versionDown()', 'alt+[')
m.addCommand('Python/localize selected', 'localizeSelectedReads.localizeSelected()',  icon='Read.png')
m.addCommand('Backdrop With Label', 'backdropWithLabel.customBackdrop()', 'alt+b', icon='Backdrop.png')
m.addCommand('Backdrop Presets', 'Victor_Toolset.presetBackdrop()', 'ctrl+alt+b', icon='Backdrop.png')
m.addCommand('PworldToTrack', 'nuke.createNode("PworldToTrack.gizmo")')
m.addCommand('V_EdgeMatte', 'nuke.createNode("V_EdgeMatte.gizmo")')
m.addCommand('V_EdgeMatte', 'nuke.createNode("V_EdgeMatte.gizmo")')

 
#added shorcuts
toolbar.findItem('Channel').findItem('Shuffle').setShortcut('alt+j')


# customise node default value - i.e.:    nuke.knobDefault('myNode.myKnob', 'myDefaultValue' )
nuke.knobDefault('RotoPaint.cliptype', '0' )
nuke.knobDefault('Blur.channels', 'rgba' )


# add menu item to existing Nuke menu - i.e.:    nodeMenu = nuke.menu('Nuke').findItem('Edit/Node').addCommand('myMenuElement', 'myPythonScript.myFunction()', 'myHotkey')    # Modifiers: Shift= shift+, Alt/Option = alt+, Control/Command = ctrl+


# callbacks
def sb_lensReflections_callbacks():

	n = nuke.thisNode()
	k = nuke.thisKnob()

	if k.name() in ["selected", "xpos", "ypos"]:
		return

	if k.name() == "method":
		noiseKnobs = ["noise_controls_text", "random_seed", "aspect_ratio", "mix", "noise_controls"]
		plateKnobs = ["dirtPlate_text", "blackpoint_1", "whitepoint_1", "gamma_5", "saturation_1"]

		if n["method"].value() == "generated noise":
			for i in noiseKnobs:
				n.knobs()[i].setVisible(True)
			for i in plateKnobs:
				n.knobs()[i].setVisible(False)

		elif n["method"].value() == "dirt plate":
			for i in noiseKnobs:
				n.knobs()[i].setVisible(False)
			for i in plateKnobs:
				n.knobs()[i].setVisible(True)

nuke.addKnobChanged(sb_lensReflections_callbacks, nodeClass="sb_lensReflections")

#def matchABCGeoFRtoShot():
 #   f = nuke.Root()['fps'].value()
 #   n = nuke.thisNode()
 #   ext = n['file'].value()[-3:]
 #   if ext == 'abc':
 #       n['frame_rate'].setValue(f)
#	print 'knob changed'
#	print nuke.thisKnob().name()

		
#nuke.addKnobChanged(matchABCGeoFRtoShot, nodeClass="ReadGeo2")
#nuke.addKnobChanged(matchABCGeoFRtoShot, nodeClass="Camera2")
#nuke.addKnobChanged(matchABCGeoFRtoShot, nodeClass="Axis2")



### Create a custom menu - i.e.:
# you need a gizmo to be placed in your '.nuke' folder structure
# toolbar = nuke.menu('Nodes')
# myMenu = toolbar.addMenu('myMenuElement', icon='myMenuIcon.png')
# myMenu.addCommand('myElement', 'nuke.createNode("myGizmo")', icon='myGizmoIcon.png', index=0) #the index argument (optional) indicates the position of the item within the menu