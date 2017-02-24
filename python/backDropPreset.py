import nuke
import nukescripts
def createBackdrop():
    backDrop = nukescripts.autoBackdrop()
    nuke.show(backDrop)
    
    #Create Pulldown Choice
    
    bdType = nuke.Enumeration_Knob('type', 'Type', ["Clean Up","Grading","Keying","Input","Input Reference","Merge","Output","Post Effects","Reference","Particles","Tracking","Reformat","Transform","Projection","Custom"])
    backDrop.addKnob(bdType)
    
    #Create Custom Label and Custom Color knobs
    
    customLbl = nuke.String_Knob('customLabel','Custom Label','')
    color = nuke.ColorChip_Knob( 'customColor' , 'Custom Color', 339694593 )
    backDrop.addKnob(customLbl)
    backDrop.addKnob(color)
    color.setEnabled(False)
    
    colorChange(backDrop)
    
def colorChange(bdNode):
    lbl=bdNode.knob('label')
    typ=bdNode.knob('type').value()
    tileColour=bdNode.knob('tile_color')
    cusLbl = bdNode.knob('customLabel').value()
    cusColor = bdNode.knob('customColor')
    cusColorVal = bdNode.knob('customColor').value()
    width=bdNode.knob('bdwidth').value()

    if typ=='Output':
        tileColour.setValue(2165841665)
        lbl.setValue("<center><img source='Output.png'><center>%s  Output"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Particles':
        tileColour.setValue(2524487681)
        lbl.setValue("<center><img source='ParticleEmitter.png'><center>%s  Particles"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Tracking':
        tileColour.setValue(2141222913)
        lbl.setValue("<center><img source='Tracker.png'><center>%s  Tracking"%cusLbl)
        cusColor.setEnabled(False) 
    elif typ=='Reformat':
        tileColour.setValue(2206576385)
        lbl.setValue("<center><img source='Reformat.png'><center>%s  Reformat"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Transform':
        tileColour.setValue(3161419521)
        lbl.setValue("<center><img source='Transform.png'><center>%s  Transform"%cusLbl)
        cusColor.setEnabled(False) 
    elif typ=='Projection':
        tileColour.setValue(1773117185)
        lbl.setValue("<center><img source='Camera.png'><center>%s  Projection"%cusLbl)
        cusColor.setEnabled(False)     
    elif typ=='Reference':
        tileColour.setValue(2335271425)
        lbl.setValue("<center><img source='Viewer.png'><center>%s  Reference"%cusLbl)
        cusColor.setEnabled(False) 
    elif typ=='Input':
        tileColour.setValue(123079425)
        lbl.setValue("<center><img source='Input.png'><center>%s  Input"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Input Reference':
        tileColour.setValue(1746094081)
        lbl.setValue("<center><img source='OCIO.png'><center>%s  Input Reference"%cusLbl)
        cusColor.setEnabled(False) 
    elif typ=='Clean Up':
        tileColour.setValue(1753980673)
        lbl.setValue("<center><img source='MarkerRemoval.png'><center>%s  Clean Up"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Keying':
        tileColour.setValue(864761601)
        lbl.setValue("<center><img source='Keyer.png'><center>%s  Keying"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Grading':
        tileColour.setValue(744124417)
        lbl.setValue("<center><img source='ColorCorrect.png'><center>%s  Grading"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Merge':
        tileColour.setValue(3311810561)
        lbl.setValue("<center><img source='Merge.png'><center>%s  Merge"%cusLbl)
        cusColor.setEnabled(False)
    elif typ=='Post Effects':
        tileColour.setValue(2996584193)
        lbl.setValue("<center><img source='Glow.png'><center>%s  Post Effects"%cusLbl)
        cusColor.setEnabled(False) 
    elif typ=='Custom':
        tileColour.setValue(cusColorVal)
        lbl.setValue('<center>'+cusLbl)
        cusColor.setEnabled(True)
		
    if bdNode.knob('bdwidth').value()<=700:
        bdNode.knob("note_font_size").setValue(width/10)
    else:
        bdNode.knob("note_font_size").setValue(70)
    bdNode.knob("note_font_color").setValue(4294967295)
    bdNode.knob("note_font").setValue("Verdana Bold")
		
def change():
    knob = nuke.thisKnob()
    node = nuke.thisNode()
    
    if node.knob('type') and (knob.name() == 'type' or knob.name('bdwidth') or knob.name('bdheight')):
        colorChange(node)
    
nuke.addKnobChanged(change,nodeClass='BackdropNode')
#Icons location: C:\mnt\software\apps\win32\thefoundry\Nuke10.0v5\plugins\icons
