# Proyecto de Sensores Ultrasónicos

Este proyecto implementa una interfaz para trabajar con sensores ultrasónicos utilizando Python y Programación Orientada a Objetos (POO). El objetivo es facilitar la medición de distancias mediante diferentes tipos de sensores ultrasónicos.

## Características

- Soporte para múltiples sensores ultrasónicos (HC-SR04, US-100, US-016).
- Uso de clases para encapsular la funcionalidad de cada sensor.
- Fácil de extender para añadir nuevos sensores.

## Estructura del Proyecto

```plaintext
ultrasonic_sensors/
├── sensors/
│   ├── __init__.py
│   ├── hc_sr04.py
│   ├── us_100.py
│   └── us_016.py
├── __init__.py
└── sensor.py
main.py