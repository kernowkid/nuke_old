import re


#path to nuke script
nukePath = nuke.Root().name()


####breadcrumbs
bc = re.findall( r'([a-zA-Z]:\/PROJECTS\/)([a-zA-Z]+\/)([a-zA-Z]+\/[a-zA-Z]+\/[a-zA-Z]+\/)([\da-zA-Z]+\/)', nukePath)
server = bc[0][0]
show = bc[0][1]
vfx = bc[0][2]
layer = 'out'


####assemble path
renderpath = '%s%s%srender/%s' %(server,show,vfx,layer)

print
print 
print '.nk path: '+str(nukePath)
print 'server:   '+str(server)
print 'show:     '+str(show)
print 'relative path to renders: '+str(vfx)
print
print renderpath
print