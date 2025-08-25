"""
Pruebas unitarias para la calculadora de números complejos
"""

import unittest
import math
from calculadora import *

class TestComplejos(unittest.TestCase):
    
    def test_suma(self):
        """Pruebas para la función suma"""
        self.assertEqual(suma((1,2), (3,4)), (4,6))
        self.assertEqual(suma((0,0), (5,3)), (5,3))
    
    def test_resta(self):
        """Pruebas para la función resta"""
        self.assertEqual(resta((5,5), (2,3)), (3,2))
        self.assertEqual(resta((10,8), (10,8)), (0,0))
    
    def test_producto(self):
        """Pruebas para la función producto"""
        self.assertEqual(producto((1,2), (3,4)), (-5,10))
        self.assertEqual(producto((2,0), (3,0)), (6,0))
    
    def test_division(self):
        """Pruebas para la función división"""
        resultado = division((1,2), (1,-1))
        self.assertAlmostEqual(resultado[0], -0.5, places=10)
        self.assertAlmostEqual(resultado[1], 1.5, places=10)
        
        # Prueba división por cero
        with self.assertRaises(ZeroDivisionError):
            division((1,2), (0,0))
    
    def test_conjugado(self):
        """Pruebas para la función conjugado"""
        self.assertEqual(conjugado((3,4)), (3,-4))
        self.assertEqual(conjugado((5,-2)), (5,2))
    
    def test_modulo(self):
        """Pruebas para la función módulo"""
        self.assertAlmostEqual(modulo((3,4)), 5.0)
        self.assertAlmostEqual(modulo((0,5)), 5.0)
    
    def test_conversion1(self):
        """Pruebas para conversión cartesiano a polar"""
        r, theta = conversion1((1,1))
        self.assertAlmostEqual(r, math.sqrt(2))
        self.assertAlmostEqual(theta, math.pi/4)
        
        r2, theta2 = conversion1((0,1))
        self.assertAlmostEqual(r2, 1.0)
        self.assertAlmostEqual(theta2, math.pi/2)
    
    def test_conversion2(self):
        """Pruebas para conversión polar a cartesiano"""
        x, y = conversion2(math.sqrt(2), math.pi/4)
        self.assertAlmostEqual(x, 1.0, places=10)
        self.assertAlmostEqual(y, 1.0, places=10)
        
        x2, y2 = conversion2(1, math.pi/2)
        self.assertAlmostEqual(x2, 0.0, places=10)
        self.assertAlmostEqual(y2, 1.0, places=10)
    
    def test_fase(self):
        """Pruebas para la función fase"""
        self.assertAlmostEqual(fase((0,1)), math.pi/2)
        self.assertAlmostEqual(fase((1,0)), 0.0)

if __name__ == "__main__":
    unittest.main()