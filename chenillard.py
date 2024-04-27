from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 17 # declaration d'une variable pinNumber à 17
led1 = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber = 2 # declaration d'une variable pinNumber à 14
led2 = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 14
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber = 10 # declaration d'une variable pinNumber à 10
led3 = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 10 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)


while True:          # boucle infini
    led1.toggle()     # change l'etat de la 1led
    utime.sleep(0.1)   # attendre 1 seconde 
    led2.toggle()     # change l'etat de la 2led
    utime.sleep(0.1)   # attendre 1 seconde 
    led3.toggle()     # change l'etat de la 3led
    utime.sleep(0.1)   # attendre 1 seconde 
    #led.on()        allume la led 
    #led.off()       eteind la led 
