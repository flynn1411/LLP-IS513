# -*- coding: utf-8 -*-
from plex import *
from tabulate import tabulate
import sys

"""
    * Generador de Analizadores Léxicos: Plex ( Lex para Python )
    ! Funciona en Python2.7
    ? Programa de ejemplo para la generación de un analiador léxico que comprende:
    ? Comentarios, Cadenas, Operador de suma y concatenación, espacios, tabulados
    ? y saltos de línea.
    @author swd
    @date 2020/07/21
    @version 0.1
"""

# sudo apt install python-pip ; sudo -H python -m pop install tabulate

class LexicalAnalysis:

    #Str, Rep, AnyBut, Any
    def __init__(self):

        #Cadena de texto: /"[^"]*"/
        stringDouble = Str("\"") + Rep(AnyBut("\"")) + Str("\"")
        stringSimple = Str("'") + Rep(AnyBut("'")) + Str("'")

        #Espacios en blanco y comentarios
        space = Any(" \t\n")
        comments = Str("{") + Rep(AnyBut("}")) + Str("}")

        #Operadores
        assignOp = Any("=")
        sumOp = Any("+") # / \+ /

        self.lexicon = Lexicon(
            [
                (stringDouble, "string"),
                (stringSimple, "string"),
                (assignOp, "assign operator"),
                (sumOp, "sum/concat operator"),
                (space | comments, IGNORE)
            ]
        )

    def parse(self):
        lexicon = self.lexicon
        lexicalTable = []

        filename = sys.argv[1:][0]
        f = open(filename, "r")
        scanner = Scanner(lexicon, f, filename)

        while True:

            try:
                token = scanner.read()

                if not token[0]: break

                desc, val = token
                lexicalTable += [[val, desc]]

            except Exception as e:
                print ("Lexical Error: %s" % (e))
                f.close()
                return False

        f.close()
        self.lexicalTable = lexicalTable
        return self

parser = (LexicalAnalysis())

if parser.parse():
    print "Analísis Léxico: "
    print tabulate(parser.lexicalTable)