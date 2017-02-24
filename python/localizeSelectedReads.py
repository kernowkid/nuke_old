import nuke

def localizeSelected():
    n = nuke.selectedNodes('Read') 
    for i in n:
        i['localizationPolicy'].setValue('on')