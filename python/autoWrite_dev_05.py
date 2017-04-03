import nuke
import eye

###Get layer name###
##layer = nuke.getInput('Layer: ')

###Get filetype###
#todo#

class PathBuilder(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Render path builder')
        self.layer = nuke.String_Knob('layer', 'Layer')
        self.filetype =  nuke.Enumeration_Knob('filetype', 'File type', ['.exr', '.jpeg']) 
        self.addKnob(self.layer)
        self.addKnob(self.filetype)


p = PathBuilder()
p.showModalDialog()


print PathBuilder
print PathBuilder.filetype

eye_resource = eye.get_resource_by_filename(nukePath)
facet_dict = eye_resource.get_facets()
shot = str(facet_dict['g3_name'])
version = 'v' + str(facet_dict['version']).zfill(3) 

##general render path###
from eyeplugins import p_nukepipe
foldername = p_nukepipe.get_nuke_render_dir() + '/' + layer + '/' + layer + '_' + shot + '_' + version + '.%04d.exr'
foldername = foldername.replace('\\','/')

###build write node###
w = nuke.createNode('Write', inpanel=True)

#increment name
count = 1
while nuke.exists('AutoWrite' + str(count)):
    count += 1

w.knob('name').setValue('AutoWrite' + str(count))
w.knob('file').setValue(foldername)





eye_resource = eye.get_resource_by_filename(nukePath)
facet_dict = eye_resource.get_facets()
import pprint

pprint.pprint(facet_dict)
print facet_dict[g3_name]

