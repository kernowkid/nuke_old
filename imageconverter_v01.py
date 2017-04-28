#converts image sequence in to .mov file
#in shell use 'nuke -t --safe /c/Users/user/.nuke/python/imageconverter_v01.py [path to img seq directory]'
# or use the alias 'converttomov  [path to img seq directory]

#todo -  add error checks


import nuke
import os
import re
import sys

#get path from terminal
path = sys.argv[1]

#get img seq in path folder 
seq = sorted(os.listdir(path))
firstFile = seq[0]
fileExt = str(os.path.splitext(firstFile)[1])

#calculate frame padding
padExt = re.search(r'([0-9]+)(\.[a-z]+)', firstFile)
padLen = len(padExt.group(1))
pad = '#'*padLen

#assemble path for read node
readPath = path + '/' + str( re.sub(r'[0-9]+\.[a-z]+',pad,firstFile) ) + str(fileExt)

#create dir path to render to 
movDir = str(path) + '_mov'

#create path and file name for Write node
writePath = str(movDir)+'/'+ str( re.sub(r'[0-9]+\.[a-z]+',pad,firstFile) ) + '.jpeg'
seqLen = len(seq)-1

lastFile = seq[-1]
#renderDir = str(path)+'/mov'

#if os.path.exists(path):
    #nuke.tprint('path is: ' + str(path))
#else:
#    nuke.tprint('booooo')
    
#create render folder if it doesn't exist
if os.path.isdir(movDir):
    nuke.tprint(str(movDir) + ' already exists!')
else:
    os.mkdir(movDir)
    nuke.tprint(str(movDir) + ' created!')

#put nuke script together and render
r = nuke.nodes.Read(file = readPath)
w = nuke.nodes.Write(file = writePath)

w.setInput(0, r) #connect the Write with the read
w['file_type'].setValue('mov')
#w['meta_codec'].setValue('apch') ##ProRes not supported :( 

nuke.execute("Write1", 0, seqLen)




