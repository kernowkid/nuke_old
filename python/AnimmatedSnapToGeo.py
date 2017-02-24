import nuke

n = nuke.thisNode()

 # Check if there's any vertices selected
 try:
   nukescripts.snap3d.selectedPoints().next()
 except:
   nuke.message("Select one or more vertices first!")
   return

 # Set framerange from root
 start = int(nuke.numvalue('root.first_frame'))
 end = int(nuke.numvalue('root.last_frame'))
 _range = str(nuke.FrameRange(start,end,1))
 r = nuke.getInput('Enter Frame Range:', _range)

 # Check the framerange is valid
 if not r:
   return
 try:
   f = nuke.FrameRange(r)
 except:
   nuke.message('Invalid frame range')
   return

 # Add a CurveTool for the forced-evaluation hack
 temp = nuke.nodes.CurveTool()
 n['translate'].setAnimated()

 # Loop through the framerange 
 for frame in f:
   nuke.execute(temp, frame, frame)
   pos = nukescripts.snap3d.centroid(nukescripts.snap3d.selectedPoints()) 
   n['translate'].setValue(pos)
 
 # delete the temp CurveTool node
 nuke.delete(temp)



# Add a new entry to the snap_menu (will show up on Axis nodes, Camera nodes, etc)
m = nuke.menu('Axis').findItem('Snap')
m.addCommand('Translate to (animated)', 'snapAnimated()')