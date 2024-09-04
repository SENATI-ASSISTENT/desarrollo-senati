# ultrasonic_sensors/sensors/us_016.py

from ..sensor import UltrasonicSensor
import random  # Simulación de la medición de distancia

class US016Sensor(UltrasonicSensor):
    def __init__(self, trigger_pin, echo_pin):
        super().__init__(trigger_pin, echo_pin, voltage=5)

    def measure_distance(self):
        # Simulación de la medición de distancia
        return random.uniform(2, 400)
