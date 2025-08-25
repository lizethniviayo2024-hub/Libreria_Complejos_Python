Calculadora de Números Complejos

Descripción



Este proyecto es una librería en Python que permite trabajar con números complejos usando tuplas. Decidí no usar el tipo complex de Python para aprender a manejar las operaciones desde cero.



Los números complejos se representan así:



Cartesianas: (parte\_real, parte\_imaginaria)



Polares: (magnitud, ángulo\_en\_radianes)



Con esta librería puedes hacer operaciones básicas y conversiones entre coordenadas.



Operaciones que implementé



Suma y resta



Producto y división (maneja división por cero)



Módulo y conjugado



Fase (argumento del número complejo)



Conversión entre cartesiano y polar



Todas las funciones trabajan con tuplas y devuelven resultados en el mismo formato.



Estructura del proyecto

Libreria\_Complejos\_Python/

│

├── calculadora.py           # Funciones principales

├── pruebas\_complejos.py    # Pruebas unitarias

├── README.md               # Documentación

└── .gitignore              # Archivos ignorados

Cómo usarlo

Requisitos



Python 3.6 o superior



Solo uso librerías estándar (math y unittest)



Ejemplo rápido

from calculadora import suma, producto, modulo, conversion1





z1 = (3, 4)    # 3 + 4i

z2 = (1, -2)   # 1 - 2i





print("Suma:", suma(z1, z2))          # (4, 2)

print("Producto:", producto(z1, z2))  # (-5, 10)

print("Módulo de z1:", modulo(z1))    # 5.0





\# Conversión a polar

print("Polar:", conversion1(z1))       # (5.0, 0.927...)

Ejecutar pruebas

python pruebas\_complejos.py



Las pruebas cubren operaciones básicas, conversiones y manejo de casos especiales como la división por cero.



Mi experiencia



Al crear esta librería aprendí mucho sobre cómo funcionan los números complejos internamente y cómo manejar errores como divisiones por cero. Es un proyecto pequeño, pero muy útil para practicar operaciones matemáticas avanzadas en Python.



Autor



Lizeth Niviayo

Proyecto personal – 2025

