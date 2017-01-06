node = nuke.selectedNode()

con = node['path_context'].value()
rp = node['path_render'].value()
pfn = node['path_filename'].value()

path =con + '/' + rp + '/' + pfn

n = nuke.createNode('Read')
n['file'].setValue(path)





k=nuke.toNode( 'Read1' )['file']
k.fromUserText( '/tmp/test.%04.exr 1-10')

allNodes = nuke.allNodes()
writeNodes = []
for node in allNodes:
    if node.Class() == 'RenderFarmWrite':
        writeNodes.append(node)

for test in writeNodes:
    if test.name() == 'DPX':
        print test

node = writeNodes[0]
print node['path_context'].value()
print node['path_render'].value()
print node['path_filename'].value()
