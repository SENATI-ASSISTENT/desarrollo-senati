
#### 4. `SENSORS.md`

Este archivo detalla los tipos de sensores compatibles y proporciona información sobre cada uno.

```markdown
# Sensores Compatibles

A continuación se presentan los sensores ultrasónicos compatibles con este proyecto y detalles sobre su implementación.

## HC-SR04

- **Voltaje:** 5V
- **Pines:** 4 (Trigger, Echo, VCC, GND)
- **Rango de Medición:** 2cm - 400cm
- **Archivo:** `hc_sr04.py`
- **Descripción:** Sensor de uso común para medir distancias cortas. Conectado a través de pines de Trigger y Echo.

## US-100

- **Voltaje:** 3.3V - 5V
- **Pines:** 5 (Trigger, Echo, VCC, GND, Serial)
- **Rango de Medición:** 2cm - 450cm
- **Archivo:** `us_100.py`
- **Descripción:** Sensor versátil que soporta conexiones UART para una lectura de distancia más precisa.

## US-016

- **Voltaje:** 5V
- **Pines:** 4 (Trigger, Echo, VCC, GND)
- **Rango de Medición:** 2cm - 400cm
- **Archivo:** `us_016.py`
- **Descripción:** Similar al HC-SR04 pero con un rango de medición ligeramente diferente y otros parámetros de precisión.
