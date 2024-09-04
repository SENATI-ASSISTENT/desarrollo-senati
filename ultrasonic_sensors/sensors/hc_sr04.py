# ultrasonic_sensors/sensors/hc_sr04.py

from ultrasonic_sensors.sensor import UltrasonicSensor
import random  # Simulación de la medición de distancia

class HCSR04Sensor(UltrasonicSensor):
    def __init__(self, trigger_pin, echo_pin):
        super().__init__(trigger_pin, echo_pin, voltage=5)

    def measure_distance(self):
        # Simulación de la medición de distancia
        return random.uniform(2, 400)
