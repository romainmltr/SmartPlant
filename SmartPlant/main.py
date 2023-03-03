from machine import Pin
import network   #import des fonctions lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json
adc_pin = machine.ADC(28)
relay_pin = machine.Pin(16, machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'iPhone de Quentin'
password = 'N1c0l4s14!'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://172.20.10.3:3000/humidity"

while not wlan.isconnected(): # tant que la raspi n'est pas connecté
    print("connecting...")
    utime.sleep(3) # attendre 3 secondes

while (True):
    adc_val = adc_pin.read_u16()
    try:
        print("POST")
        # lance une requete sur l'url
        r = urequests.post(url, json={"value": adc_val})

        print("sucess")
        r.close() # ferme la connexion
        utime.sleep(5)

    except Exception as e:
        print(e)
        utime.sleep(5)