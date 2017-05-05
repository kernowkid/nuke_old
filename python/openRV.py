### open read file in rv
import nuke
import sys
import os

def openReadInRV():           
    try:
        s = nuke.selectedNodes()
        paths=[]
        file = ''
        exists = True

        for p in s:
            
            p1 = os.path.dirname(p.knob('file').value())
            
            ##Check if file exists
            if os.path.exists(p1)== False:
                exists = False
                nuke.message('The file "%s" does not exist' % p1)
            else:
                paths.append(p1)
                
            file = ' '.join(paths)
        
        if exists == True:
            ##open one read rv 
            if len(s) == 1:
                print 'Opening single Read/Write in RV'
                os.system('start rv %s' % file)
            
            ##open multiple reads in rv in a stack in over mode
            elif len(s) > 1:
                print 'Opening multiple Reads/Writes in RV'
                os.system('start rv -over %s' % file)
        
    except:
        nuke.message('No read/write selected')   
    return