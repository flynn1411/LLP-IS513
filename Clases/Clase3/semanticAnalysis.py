# -*- coding: utf-8 -*-

from tabulate import tabulate
import sys, re

class SemanticAnalysis:

    def __init__(self): pass

    def help(self):

        print("")
        print("*"*80)
        print("*"*80)
        print("\tSemantic Analysis (Analizador Semántico Demostrativo) ")
        print("""
\tPermite el reconocimiento de distintos significados de instrucción

\t@author swd
\t@date 2020/07/10
\t@version 0.1""")
        print("*"*80)
        print("*"*80)
        print("")

    def clean(self, text):
        return ("%s".strip() % text).strip()

    def read(self):
        self.text = input()
        return self

    def jsonToMatrix(self, json):
        result = []
        header = []

        count = 0

        for k,v in json.items():
            row = [k]

            for k1,v1 in v.items():
                count += 1

                if count<3:
                    header += [self.clean(k1)]

                row += [v1]
            result += [row]

        return [["Name"]+header] + [["-"*5,"-"*5,"-"*5]] + result

    def splitInstruction(self, line):
        var,val = re.split(r"=", line)
        var = self.clean(var)
        val = self.clean(val)
        return (var,val)

    def UDV(self):
        #User Defined Variables
        result = {}

        text = self.text
        lines = re.split(r";", text)

        for i in range(len(lines)):

            line = self.clean(lines[i])
            if len(line)>0:
                if re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*\d+$", line):
                    var,val = self.splitInstruction(line)
                    result[var] = {"type":"int", "value":val}

                elif re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*\d+(\.\d+)?$", line):
                    var,val = self.splitInstruction(line)
                    result[var] = {"type":"float", "value":val}

                elif re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*[a-zA-Z][a-zA-Z\d_]*$", line):
                    var,val = self.splitInstruction(line)
                    result[var] = {"type":result[val]["type"], "value":val}

                else:
                    quit("Error Semántico: no se ha encontrado la definición '%s'." % line)

        return result

parser = (SemanticAnalysis()).read()
UDV = parser.UDV()
print (tabulate(parser.jsonToMatrix(UDV)))