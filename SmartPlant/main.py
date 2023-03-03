from machine import Pin
import network   #import des fonctions lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json

sensor = machine.ADC(28)
relay = machine.Pin(16, machine.Pin.OUT)
led = machine.Pin(17, machine.Pin.OUT)
led.off()

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'iPhone de Quentin'
password = 'quentinco'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://172.20.10.3:3000/humidity"
url_water = "http://172.20.10.3:3000/water"

def pump_on():
    led.on()
    relay.value(1)
    utime.sleep(2)
    #print("Pump On")

def pump_off():
    led.off()
    relay.value(0)
    #print("Pump Off")

def handle_button_press():
    response = urequests.get(url_water)
    json = response.json()
    water = json['water']
    response.close()
    if water == 0:
        pump_off()
    else:
        pump_on()

while not wlan.isconnected(): # tant que la raspi n'est pas connecté
    print("connecting...")
    utime.sleep(1)

while (True):
    handle_button_press()

    sensor_val = sensor.read_u16()
    try:
        #print("POST value")
        print(sensor_val)
        r = urequests.post(url, json={"value": sensor_val})
        r.close()
        utime.sleep(2)

    except Exception as e:
        print(e)
        utime.sleep(5)