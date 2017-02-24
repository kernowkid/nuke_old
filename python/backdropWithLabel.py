import nuke
import nukescripts

def customBackdrop():
	note = nuke.getInput('Add label: ')
	col = nuke.getColor()
	bd = nukescripts.autoBackdrop()
	n = len( nuke.selectedNodes() )
	
	bd['label'].setValue(note)
	bd['tile_color'].setValue(col)
	bd['note_font'].setValue('Verdana Bold')
	
	if  n > 5:
		bd['note_font_size'].setValue(42)
		
	else:
		bd['note_font_size'].setValue(24)
		
		