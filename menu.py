
### import Python scripts and/or Python Modules - i.e.:    import myPythonScript
import nuke
import opendir
import Victor_Toolset
import camFromMeta_05



### add format resolutions presets - i.e.:    nuke.addFormat ('1920 797 0 0 1920 797 1.0 FullHD_Widescreen')



### add LUT to the Root - i.e.:    nuke.root().knob('luts').addCurve('nameOfTheLUT', 'formula')    # sLOG formula example: '{pow(10.0, ((t - 0.616596 - 0.03) /0.432699)) - 0.037584}'



### customise menu items from Nodes toolbar - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'j', icon='Shuffle.png')
### set hotkey for an existing menu item - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').findItem('Channel').findItem('Shuffle').setShortcut('j')
menubar = nuke.menu('Nuke')
toolbar = nuke.menu('Nodes')

m = menubar.addMenu('Plugs')
m.addCommand('python/Create Camera From Meta ','camFromMeta_05.ExrToCamera()', 'alt+c', icon='Camera.png')
m.addCommand('python/Open Selected Read in OS File Browser', 'opendir.openInExplorer()', 'shift+alt+e', icon='Read.png')
m.addCommand('Backdrop Presets', 'Victor_Toolset.presetBackdrop()', 'ctrl+alt+b')


toolbar.addCommand('Other/Backdrop', 'nukescripts.autoBackdrop()', 'alt+b', icon='Backdrop.png')
toolbar.findItem('Channel').findItem('Shuffle').setShortcut('j')



### customise node default value - i.e.:    nuke.knobDefault('myNode.myKnob', 'myDefaultValue' )
nuke.knobDefault('RotoPaint.cliptype', '0' )
nuke.knobDefault('Blur.channels', 'rgba' )


### add menu item to existing Nuke menu - i.e.:    nodeMenu = nuke.menu('Nuke').findItem('Edit/Node').addCommand('myMenuElement', 'myPythonScript.myFunction()', 'myHotkey')    # Modifiers: Shift= shift+, Alt/Option = alt+, Control/Command = ctrl+



### Create a custom menu - i.e.:
# you need a gizmo to be placed in your '.nuke' folder structure
# toolbar = nuke.menu('Nodes')
# myMenu = toolbar.addMenu('myMenuElement', icon='myMenuIcon.png')
# myMenu.addCommand('myElement', 'nuke.createNode("myGizmo")', icon='myGizmoIcon.png', index=0) #the index argument (optional) indicates the position of the item within the menu