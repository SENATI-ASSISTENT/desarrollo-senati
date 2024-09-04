
#### 3. `USAGE.md`

Este archivo explica cómo usar el proyecto, incluyendo ejemplos de código.

```markdown
# Uso del Proyecto

Este proyecto permite medir distancias utilizando diferentes tipos de sensores ultrasónicos.

## Ejecución Básica

Para ejecutar el proyecto y ver los resultados de los sensores, simplemente ejecuta:

```bash
python main.py
```
# Simulacion

El proyecto incluye capacidades de simulación para facilitar pruebas sin necesidad de hardware físico. Esto es útil durante las fases de desarrollo y prueba de lógica.

## Pasos para la simulacion

- Ejecuta el archivo main.py que se encuentra en el directorio principal.

### Ejemplo de Simulacion

```python
from sensors.hc_sr04 import HCSR04Sensor
from sensors.us_100 import US100Sensor
from sensors.us_016 import US016Sensor

# Crear instancias de los sensores en modo simulado
hc_sr04_sensor = HCSR04Sensor(trigger_pin=17, echo_pin=27, simulated=True)
us_100_sensor = US100Sensor(trigger_pin=22, echo_pin=23, simulated=True)
us_016_sensor = US016Sensor(trigger_pin=24, echo_pin=25, simulated=True)

# Medir distancias simuladas
print("Distancia medida por HC-SR04:", hc_sr04_sensor.measure_distance(), "cm")
print("Distancia medida por US-100:", us_100_sensor.measure_distance(), "cm")
print("Distancia medida por US-016:", us_016_sensor.measure_distance(), "cm")
```

# Uso con sensores reales

## 1: Requistos

- Python 3.7+
- Placa de Desarrollo: Raspberry Pi, Arduino, etc.
- Librerías GPIO: Instala las librerías necesarias según tu placa de desarrollo.

Puede Instalarlo con:

```bash
pip install RPi.GPIO    # Para Raspberry Pi
pip install pyfirmata   # Para Arduino

```

## 2: Pasos para uso real

- Conectar los Sensores: Conecta los pines trigger y echo de cada sensor a los pines GPIO de la placa de desarrollo. Consulta la documentación del sensor y la placa para conocer los pines adecuados.

- Ajustar el Código: Modifica el archivo main.py para desactivar la simulación. Asegúrate de pasar simulated=False al crear instancias de los sensores.

- Ejecutar el Script: main.py.

### Ejemplo de uso con Sensores Reales

```python
# main.py

from sensors.hc_sr04 import HCSR04Sensor
from sensors.us_100 import US100Sensor
from sensors.us_016 import US016Sensor

# Crear instancias de los sensores en modo real
hc_sr04_sensor = HCSR04Sensor(trigger_pin=17, echo_pin=27, simulated=False)
us_100_sensor = US100Sensor(trigger_pin=22, echo_pin=23, simulated=False)
us_016_sensor = US016Sensor(trigger_pin=24, echo_pin=25, simulated=False)

# Medir distancias reales
print("Distancia medida por HC-SR04:", hc_sr04_sensor.measure_distance(), "cm")
print("Distancia medida por US-100:", us_100_sensor.measure_distance(), "cm")
print("Distancia medida por US-016:", us_016_sensor.measure_distance(), "cm")
```

## 3: Consejos para la Integracion

- Verifica las conexiones: Asegúrate de que los cables estén correctamente conectados y de que no haya conexiones sueltas.

- Chequea el voltaje: Algunos sensores pueden requerir un voltaje específico (3.3V o 5V). Verifica que tu fuente de energía coincida con los requisitos del sensor.

- Prueba con un sensor a la vez: Si encuentras problemas, intenta conectar y probar un sensor a la vez para aislar cualquier problema.

- Observa las luces LED: Muchos sensores tienen indicadores LED que muestran el estado de funcionamiento (por ejemplo, cuando envían un pulso). Úsalos para verificar si el sensor está recibiendo energía y operando.

## 4: Solucion de Problemas Comunes

- No se mide la distancia: Verifica que los pines de trigger y echo estén conectados correctamente y que no estén invertidos.

- Mediciones inestables: Asegúrate de que no haya interferencias físicas delante de los sensores y que estén correctamente alineados.

- Error de permisos en Raspberry Pi: Asegúrate de ejecutar el script con permisos adecuados o como superusuario (sudo python main.py).

---

## Nota Final

Este archivo `USAGE.md` ahora ofrece una guía clara y detallada para configurar y usar los sensores ultrasónicos tanto en simulación como en entornos reales.

**¡Esperamos que esta documentación te sea de gran utilidad!** 

Si tienes alguna pregunta o necesitas asistencia adicional, no dudes en ponerte en contacto con el equipo de soporte o consultar los recursos adicionales disponibles en el repositorio.

