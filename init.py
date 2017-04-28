## init.py
## loaded by nuke before menu.py

import nuke
import os
import re

if not nuke.GUI:
    nuke.tprint('terminal mode!!')
        
    
# to add a folder inside the '.nuke' folder -> nuke.pluginAddPath('./myFolder')

nuke.pluginAddPath('./python')
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./scripts/rvnuke')

####    LUTS
# add arri viewer LUT process for Vax to viewer LUT dropdown
#nuke.ViewerProcess.register("Vax", nuke.Node, ("VaxVP","")) 



## create autowrite directories 
def createWriteDir():
    import nuke, os, errno
    file = nuke.filename(nuke.thisNode())
    dir = os.path.dirname( file )
    osdir = nuke.callbacks.filenameFilter( dir )
    # cope with the directory existing already by ignoring that exception
    try:
      os.makedirs( osdir )
    except OSError, e:
      if e.errno != errno.EEXIST:
        raise
nuke.addBeforeRender(createWriteDir)


# auto write path and dir
def createWritePath(node):
    
    import nuke
    import eye
    
    #node = nuke.thisNode()
    nukePath = nuke.scriptName()
    
    ### Get filename and filetype  ###
    filename =  node.name()
    
    if 'Write' not in filename: 
        
        ### test if file type is set. if not set filetype to 'exr' ###
        filetype = ''
        exttest = node['file_type'].getValue()
        if exttest == 0:
            filetype = '.exr'
        else:
            filetype = '.' + str(node['file_type'].value())
    
    
        ### Get shot and version from eye  ###
        try:
            eye_resource = eye.get_resource_by_filename(nukePath)
        except eye.EyeNotFoundError:
            nuke.message("You need to have an open file")
            return      
       
        facet_dict = eye_resource.get_facets()
        shot = str(facet_dict['g3_name'])
        version = 'v' + str(facet_dict['version']).zfill(3) 
        
        ## build render path ###
        from eyeplugins import p_nukepipe
        renderdir = p_nukepipe.get_nuke_render_dir() 
        
        renderpath = ''
        
        if filetype == '.mov':
            renderpath =  renderdir + '/' + filename + '/' + filename + '_' + shot + '_' + version  + filetype
        else:
            renderpath =  renderdir + '/' + filename + '/' + filename + '_' + shot + '_' + version + '.%04d' + filetype    
        
        renderpath = renderpath.replace('\\','/')
        
        
        ### set write nodes file knob
        node.knob('file').setValue(renderpath)
    
def createWritePathFeedAll():
    nodes = [n for n in nuke.allNodes() if n.Class()=='Write']
    for node in nodes:
        if 'Write' not in node.name():
            createWritePath(node)
        
def createWritePathFeedCurrent():
    node = nuke.thisNode()
    nn = node.name()
    tk = nuke.thisKnob().name()
    if 'Write' not in nn:
        if tk == 'name':
            createWritePath(node)



nuke.addKnobChanged(createWritePathFeedCurrent, nodeClass = 'Write')
nuke.addOnScriptSave(createWritePathFeedAll)



