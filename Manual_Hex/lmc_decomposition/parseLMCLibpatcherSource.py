import javalang
import os
import re

paramsPath = 'C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Manual_Hex/lmc_decomposition/LibPatcher.java'
xmlPath = 'C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Manual_Hex/lmc_decomposition/array.xml'


f = open(paramsPath)
javaObj = f.read()

tree = javalang.parse.parse(javaObj)

for a, b in tree.filter( javalang.tree.VariableDeclarator ):  #.name = name, .initializer.value = hex
    for c, d in tree.filter( javalang.tree.MethodInvocation ): #.arguments = name and xml name
        if str(b.name) in str(d.arguments):
            val = re.findall('value="lib_(.*?)_', str(d.arguments))
            print(b.name, b.initializer.value, val)
            
