import nuke
import re

def versionUp():
	n = nuke.selectedNode()
	path = n["file"].value()
	ver = re.search(r"(_[vV])(\d+)", path).group(2)
    newVer = str(int(ver)+1).zfill(len(ver))
    newPath = re.sub(ver, newVer, path)
    n["file"].setValue(newPath)
    print  "versioned up to v%s:" %newVer

def versionDown():
	n = nuke.selectedNode()
	path = n["file"].value()
	ver = re.search(r"(_[vV])(\d+)", path).group(2)
    newVer = str(int(ver)-1).zfill(len(ver))
    newPath = re.sub(ver, newVer, path)
    n["file"].setValue(newPath)
    print  "versioned down to v%s:" %newVer	