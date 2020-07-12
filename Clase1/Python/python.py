# -*- coding: utf-8 -*-
"""
    Conforman la Gramática: Léxico, Sintaxis, Semántica.

    E.g.:
        Cuidado. !ladrón.
        Cuidado ladrón.

    Manejo de errores en todo lenguaje de programación,
    Existen errores léxicos, gramáticales y semánticos en la generación código.
    El manejo de errores identifica:
        El número de línea donde ocurre el error.
        El tipo de error.
        El carácter donde ocurre el error.
"""

def factorial(n):
    if n<2: return 1
    return n*factorial(n-1)

print(factorial(5))