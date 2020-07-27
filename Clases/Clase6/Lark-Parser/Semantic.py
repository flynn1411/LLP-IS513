# -*- coding: utf-8 -*-

import re
from lark import Transformer, v_args

@v_args(inline=True)
class Semantic(Transformer):

    def __init__(self):
        self.variables = {}

    def sum(self, A, B):
        return float(A)+float(B)

    def sub(self, A, B):
        return float(A) - float(B)

    def assignvar(self, name, value):
        self.variables[name] = value

    def getvar(self, name):
        return self.variables[name]

    def printstatement(self, param):
        print ("%s" % self.cleanParam(param))

    def printvar(self, name):
        print("%s" % (self.getvar(name)))
    
    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            return param[1:-1]
            return param