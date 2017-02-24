def matchABCGeoFRtoShot():
    f = nuke.Root()['fps'].value()
    n = nuke.thisNode()
    ext = n['file'].value()[-3:]
    if ext == 'abc':
        n['frame_rate'].setValue(f)

nuke.addOnUserCreate('matchABCGeoFRtoShot()', nodeClass='ReadGeo2')
nuke.addOnUserCreate('matchABCGeoFRtoShot()', nodeClass='Camera2')






f = nuke.Root()['fps'].value()
n = [ i for i in nuke.allNodes() if i.Class() == 'ReadGeo2' or i.Class() == 'Camera2']

for i in n:
    ext = i['file'].value()[-3:]
    if ext == 'abc':
        i['frame_rate'].setValue(f)
    print
    print i['frame_rate'].value()
    print i.name()
    print ext
    print