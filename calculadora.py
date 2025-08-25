"""
Librería para operaciones con números complejos
Implementa operaciones básicas usando tuplas para representar números complejos.
"""

import math

def suma(z1, z2):
    """Suma dos números complejos"""
    return (z1[0] + z2[0], z1[1] + z2[1])

def resta(z1, z2):
    """Resta dos números complejos"""
    return (z1[0] - z2[0], z1[1] - z2[1])

def producto(z1, z2):
    """Multiplica dos números complejos"""
    a, b = z1
    c, d = z2
    return (a*c - b*d, a*d + b*c)

def division(z1, z2):
    """Divide dos números complejos"""
    a, b = z1
    c, d = z2
    denominador = c**2 + d**2
    if denominador == 0:
        raise ZeroDivisionError("División por cero")
    real = (a*c + b*d) / denominador
    imag = (b*c - a*d) / denominador
    return (real, imag)

def conjugado(z):
    """Calcula el conjugado de un número complejo"""
    a, b = z
    return (a, -b)

def modulo(z):
    """Calcula el módulo de un número complejo"""
    a, b = z
    return math.sqrt(a**2 + b**2)

def conversion1(z):
    """Convierte de cartesiano a polar (magnitud, fase)"""
    a, b = z
    r = math.sqrt(a**2 + b**2)
    theta = math.atan2(b, a)
    return (r, theta)

def conversion2(r, theta):
    """Convierte de polar a cartesiano"""
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

def fase(z):
    """Calcula la fase de un número complejo"""
    a, b = z
    return math.atan2(b, a)

