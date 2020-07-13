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

x = 5
print("El factorial de %d es %d"%(x,factorial(5)))