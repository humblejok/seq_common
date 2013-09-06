'''
Created on Aug 20, 2013

@author: sdejonckheere
'''

# From: http://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def my_class_import(name):
    components = name.split('.')
    module = __import__('.'.join(components[:(len(components)-1)]), fromlist=components[-1:])
    return getattr(module,components[-1])