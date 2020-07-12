#factorial en Python

"""
    Prueba para poder observar si el analizador lexico funciona
    aifnaifniaf
    sdfinianfiasa
"""

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))