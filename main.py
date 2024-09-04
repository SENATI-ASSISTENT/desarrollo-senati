from ultrasonic_sensors.sensors.hc_sr04 import HCSR04Sensor
from ultrasonic_sensors.sensors.us_100 import US100Sensor
from ultrasonic_sensors.sensors.us_016 import US016Sensor

def main():
    # Crear instancias de los sensores
    sensor_hcsr04 = HCSR04Sensor(trigger_pin=1, echo_pin=2)
    sensor_us100 = US100Sensor(trigger_pin=3, echo_pin=4)
    sensor_us016 = US016Sensor(trigger_pin=5, echo_pin=6)

    # Obtener y mostrar los datos de cada sensor
    print(sensor_hcsr04.get_data())
    print(sensor_us100.get_data())
    print(sensor_us016.get_data())

if __name__ == "__main__":
    main()
