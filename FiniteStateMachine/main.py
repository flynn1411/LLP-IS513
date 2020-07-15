# -*- coding:utf-8 -*-

from fsm import FiniteStateMachine
from tabulate import tabulate
import re, sys

def analyze(userString = ""):
    results = []

    fsm = FiniteStateMachine()
    
    fsm.runMachine()

    for char in userString:

        #if re.match(r"[\+\*\(\)\{\}\[\]]+", char):
         #   char = "\\%s" % char

        result = fsm.checkChar(char)
        if result is not None:
            results.append(result)
            fsm.runMachine()

    return results

param = sys.argv[1:]

if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")

fileName = param[0]
f = open(fileName,"r")
text = f.read() #Lee la completidud del programa
f.close()

output = analyze(text)

print("El resultado es:\n")
print("%s"%tabulate(output))