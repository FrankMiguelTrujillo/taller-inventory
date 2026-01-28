# adivinanza-numero-python

Un juego interactivo simple en Python donde el usuario tiene **8 intentos** para adivinar un número aleatorio entre 1 y 100.

## Descripción

El programa genera un número secreto y guía al jugador con pistas ("mayor" o "menor") hasta que adivine o se agoten los intentos. Incluye manejo de errores (ValueError) y validación de rango.

## Características

- Generación aleatoria del número (módulo `random`)
- Límite de 8 intentos
- Mensajes claros de pista (número mayor/menor)
- Validación de entrada numérica y rango (1-100)
- Manejo de excepciones para entradas no numéricas

## Cómo jugar

1. Clona el repositorio
2. Ejecuta el script:
   ```bash
   python adivina_numero.py
