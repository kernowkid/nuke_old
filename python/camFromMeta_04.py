

## original script from https://github.com/dekekincaid/nuke.env/blob/master/python/ExrToCameraRaw.py

import nuke
import os
import math
    
def getMetadataMatrix(meta_list):
    m = nuke.math.Matrix4()
    try:
        for i in range (0,16) :
            m[i] = meta_list[i]   
    except Exception as e:
        print "Unable to convert metadata to matrix, using the identity matrix"
        m.makeIdentity()
    return m    

def ExrToCamera():
    node = nuke.selectedNode()
    #nodeName = selectedNode.name()
    #node = nuke.toNode(nodeName)
    if node.Class() != 'Read':
        nuke.message('Please select a read Node')
        print 'Please select a read Node'
        return
    metaData = node.metadata()
    reqFields = ['exr/%s' % i for i in ('worldToCamera', 'worldToNDC')]
    if not set( reqFields ).issubset( metaData ):
        nuke.message('no basic matrices for camera found')
        print 'no basic matrices for camera found'
        return
    else:
        print 'found needed data'
    
    try:
        imageWidth = metaData['input/width']
        imageHeight = metaData['input/height']
        aspectRatio = float(imageWidth)/float(imageHeight)
        hAperture = metaData['exr/CameraFilmApertureHorizontal']
        vAperture = metaData['exr/CameraFilmApertureVertical']
    except Exception as e:
        nuke.message('Failed to gather all meta data')
        raise Exception('Failed to gather all meta data')
    
    # get additional stuff
    first = node.firstFrame()
    last = node.lastFrame()
    ret = nuke.getFramesAndViews( 'Create Camera from Metadata', '%s-%s' %( first, last )  )
    frameRange = nuke.FrameRange( ret[0] )
    camViews = (ret[1])
    
    #Setting up the camera
    for act in camViews:
        cam = nuke.nodes.Camera(name="Camera_%s" % act)
        #enable animated parameters
        cam['useMatrix'].setValue( True )
        cam['haperture'].setValue ( hAperture )
        cam['vaperture'].setValue ( vAperture )
    
        for k in ( 'focal', 'matrix', 'win_translate'):
            cam[k].setAnimated()
        
        task = nuke.ProgressTask( 'Baking camera from meta data in %s' % node.name() )

        for curTask, frame in enumerate( frameRange ):
            if task.isCancelled():
                break
            task.setMessage( 'processing frame %s' % frame )
            try:
                #get the data out of the exr header
                wTC = node.metadata('exr/worldToCamera',frame, act)
                #   wTN = node.metadata('exr/worldToNDC',frame, act)

                focal = node.metadata('exr/CameraFocalLength',frame, act)
            except Exception as e:
                nuke.message('meta data not found')
                raise Exception('meta data not found')
                
            cam['focal'].setValueAt(  float( focal ), frame )
        
            # do the matrix math for rotation and translation
    
            matrixList = wTC  #assign worldToCamera metadata to matrixList variable 
            camMatrix = getMetadataMatrix(wTC)  #send worldToCamera metadata to getMetadataMatrix to put data into a matrix. Then assign it to camMatrix variable   
            
            #create new matrix with inverted z 
            flipZ=nuke.math.Matrix4() #create new matrix
            flipZ.makeIdentity()  #initialise matrix
            flipZ.scale(1,1,-1)   #flip z
             

            #the camera translation should come from the inverse of the 
            #worldToCamera matrix. Translation values will be in the last row of 
            #that inverted matrix.
            #
            #For rotation, you can use the toEulerXYZ() method (or whatever rotation 
            #order you want to use) of the cgtypes matrix class.

            try:
                transposedMatrix = nuke.math.Matrix4(camMatrix) # create new matrix with the worldToCamera matrix (camMatrix) 
                transposedMatrix.transpose()# transpose the matrix (swap the rows and columns) to 
                transposedMatrix=transposedMatrix*flipZ # multiply by the flipz matrix to invert the z     
                invMatrix=transposedMatrix.inverse() # assign the flipped z matrix to the invMatrix variable

            except Exception as e:
                nuke.message('Error computing meta data for camera position')
                raise Exception('Error computing meta data for camera position')
            
            for i in range(0,16):
                matrixList[i]=invMatrix[i]
            
            for i, v in enumerate( matrixList ):
                cam[ 'matrix' ].setValueAt( v, frame, i)
            # UPDATE PROGRESS BAR
            task.setProgress( int( float(curTask) / frameRange.frames() *100) )


ExrToCamera()