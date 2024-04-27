import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

pwm_ledb = PWM(Pin(8,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledb.freq(1_000) # dont la frequence est de 1000 (default)
pwm_ledb.duty_u16(0) # on lui donne une valeur comprise entre 0  et 65535 qui est conver
pwm_ledv = PWM(Pin(9,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledv.freq(1_000) # dont la frequence est de 1000 (default)
pwm_ledv.duty_u16(0) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3vti entre 0 et 3.3v
pwm_ledr = PWM(Pin(10,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledr.freq(1_000) # dont la frequence est de 1000 (default)
pwm_ledr.duty_u16(0) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v

house = {"Gryffindor" : [30000, 0, 0], "Ravenclaw" : [0, 0, 30000] , "Hufflepuff" : [30000, 30000, 0], "Slytherin" : [0, 30000, 0]}


ssid = 'Lucario'
password = 'lamis2005'
wlan.connect(ssid, password) # connecte la raspi au réseau
#url = "https://hp-api.onrender.com/api/character/9e3f7ce4-b9a7-4244-b709-dae5c1f1d4a8"
# http ton IP ton port route 1 sous route
url = "http://192.168.1.66:3000/iot/card"
while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        maison = r.json()[0]["house"]
        print(r.json()[0]["house"]) # traite sa reponse en Json
        r.close() # ferme la demande
        utime.sleep(1)
        pwm_ledr.duty_u16(house[maison][0])
        pwm_ledb.duty_u16(house[maison][1])
        pwm_ledv.duty_u16(house[maison][2])
        
    except Exception as e:
        print(e)
        

#condition si 
# sinon 
#else: 
    #print("Error")
        
        
        

        

    
