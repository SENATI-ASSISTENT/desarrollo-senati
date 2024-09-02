# ultrasonic_sensors/sensor.py

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin, voltage=5):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.voltage = voltage

    def measure_distance(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    def get_data(self):
        distance = self.measure_distance()
        return {
            "trigger_pin": self.trigger_pin,
            "echo_pin": self.echo_pin,
            "voltage": self.voltage,
            "distance_cm": distance
        }
