
import re
import nuke
import eye

#path to nuke script
nukePath = nuke.Root().name()

##general render path
from eyeplugins import p_nukepipe
foldername = p_nukepipe.get_nuke_render_dir()





####assemble path
renderpath = '%s%s%srender/%s/v%s%s/%s/' %(server,show,vfx,dis,ver,script,layer)

###build write node
w = nuke.createNode('Write', inpanel=True)
t = nuke.Tab_Knob("create directory")
w.addKnob(t)
count = 1

while nuke.exists('AutoWrite' + str(count)):
    count += 1
w.knob('name').setValue('AutoWrite' + str(count))
w.knob('beforeRender').setValue('createWriteDir')
w.knob('file').setValue(renderpath)




def autowrite():
    #path to nuke script
    nukePath = nuke.Root().name()
    
    
    ####breadcrumbs
    bc = re.search( r'(?P<server>[a-zA-Z]:\/PROJECTS\/)(?P<show>[a-zA-Z]+\/)(?P<rpath>[a-zA-Z]+\/[a-zA-Z]+\/[a-zA-Z]+\/)(?P<version>[\da-zA-Z]+\/)(?P<dis>[a-zA-Z]+)\/([a-zA-Z]+)\/(?P<script>[a-zA-Z]+)\/', nukePath)
    
    server = bc.group('server')
    show = bc.group('show')
    vfx = bc.group('rpath')
    dis = bc.group('dis')
    ver = bc.group('version')
    script = bc.group('script')
    layer = 'out'

    
    ####assemble path
    renderpath = '%s%s%srender/%s/v%s%s/%s/' %(server,show,vfx,dis,ver,script,layer)
    
    ###build write node
    w = nuke.createNode('Write', inpanel=True)
    t = nuke.Tab_Knob("create directory")
    w.addKnob(t)
    count = 1
    
    while nuke.exists('AutoWrite' + str(count)):
        count += 1
    w.knob('name').setValue('AutoWrite' + str(count))
    w.knob('beforeRender').setValue('createWriteDir')
    w.knob('file').setValue(renderpath)

autowrite()



eye_resource = eye.get_resource_by_filename(nukePath)
facet_dict = eye_resource.get_facets()
import pprint

pprint.pprint(facet_dict)
print foldername
