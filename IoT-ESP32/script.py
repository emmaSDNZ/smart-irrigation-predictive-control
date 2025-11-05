import network, urequests, time
from machine import Pin, ADC

# Sensores (ejemplo humedad suelo analógico)
humidity_pin = ADC(Pin(34))
humidity_pin.atten(ADC.ATTN_11DB)

# Relay bomba
pump = Pin(5, Pin.OUT)

SERVER_URL = "http://loca_host/decision"

def read_humidity():
    raw = humidity_pin.read()   # 0-4095
    return raw / 4095           # normalizamos 0-1

while True:
    hum = read_humidity()

    payload = {"humidity": hum}
    try:
        res = urequests.post(SERVER_URL, json=payload)
        decision = res.json().get("water", 0)

        if decision == 1:
            pump.on()
            print("🌱 Regando (IA dice sí)")
        else:
            pump.off()
            print("✅ No riego")

    except Exception as e:
        pump.off()
        print("⚠ Error comunicación, bomba apagada")

    time.sleep(60)  # cada 1 min (puedes ajustar)
