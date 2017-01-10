### open read file in explorer
import nuke
import sys
import os

def openInExplorer(platform = sys.platform):
            
    try:
       s = nuke.selectedNode()
       path = os.path.dirname(s.knob('file').value())
    except:
       nuke.message('No read/write selected')
       return
    
    if platform == 'darwin':
       os.system('open %s' % path)
    if platform == 'linux2':
       os.system('nautilus %s' % path)
    if platform == 'win32':
       path = path.replace('/','\\')
       os.system('start %s' % path)


