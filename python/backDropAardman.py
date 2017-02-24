#Create Backdrop and open panel

B = nukescripts.autoBackdrop()
B.knob('selected').setValue(True)
nuke.show(B)

#Create Pulldown Choice

S = nuke.Enumeration_Knob('type', 'Type', ["Grade","Keying","Output","Custom"])
B.addKnob(S)

#Create Custom Label and Custom Color knobs

CL = nuke.String_Knob('customLabel','Custom Label','')
CC = nuke.ColorChip_Knob( 'customColor' , 'Custom Color', 4294967295 )
B.addKnob(CL)
B.addKnob(CC)
CL.setEnabled(False)
CC.setEnabled(False)

#Callback

A= nuke.PyCustom_Knob('PC', 'PC', "nuke.thisNode().knob('knobChanged').setValue('''\nB=nuke.thisNode()\nI=B.knob('label')\nT=B.knob('type').value()\nTC=B.knob('tile_color')\nCL=B.knob('customLabel').value()\nM = B.knob('customLabel')\nCC = B.knob('customColor')\nCCI = B.knob('customColor').value()\nprint CL\nprint T\nprint TC\nif T=='Keying':\n    TC.setValue(6577175178)\n    I.setValue(\"<center><img source='Keyer.png'> Keying\")\n    M.setEnabled(False)\n    CC.setEnabled(False)\n    \nelif T=='Grade':\n    TC.setValue(7856567176)\n    I.setValue(\"<center><img source='Grade.png'> Grade\")\n    M.setEnabled(False)\n    CC.setEnabled(False)\n    \nelif T=='Output':\n    TC.setValue(2435535171)\n    I.setValue(\"<center><img source='Output.png'> Output\")\n    M.setEnabled(False)\n    CC.setEnabled(False)\n    \nelif T=='Custom':\n    TC.setValue(CCI)\n    I.setValue('<center>'+CL)\n    M.setEnabled(True)\n    CC.setEnabled(True)\n    print CC\n\nB.knob(\"note_font_size\").setValue(60)\nB.knob(\"note_font_color\").setValue(4294967295)\nB.knob(\"note_font\").setValue(\"Verdana Bold\")\n    \n''')")
B.addKnob(A)