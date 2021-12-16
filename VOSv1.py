from os import kill
import RPi.GPIO as GPIO
import threading
from gpiozero import LED, Button
from datetime import datetime
import csv
import time
import threading as th


ledKamer = LED(4)
ledVPk = LED(17)
buttonkamer103 = Button(2)
buttonkamer103._hold_repeat = False
buttonkamer104 = Button(16)
buttonkamer105 = Button(23)
buttonVPK = Button(10)

statusVPK = False
# status False = geen VPK aanwezig in de kamer
# status True = VPK aanwezig in de kamer


ledKamer.off()

calls = []

class Kamer():
    def locateSource(source):
        if(source == buttonkamer103):
            return "room 103"
        elif(source == buttonkamer104):
            return "room 104"
        elif(source == buttonkamer105):
            return "room 105"
        else:
            return "source unknown"

    def oproep(source):
        global calls, ledKamer,ledVPk
        ledKamer.blink()
        ledVPk.on()
        current_date_time = datetime.now()
        new_list = [Kamer.locateSource(source), current_date_time,]
        with open ('/home/pi/Project-Ai/calls.csv', 'a+', newline='') as file:
            file_write = csv.writer(file)
            file_write.writerow(new_list)
            file.close()

class verpleegkundige():
    def oproep():
        global statusVPK, ledKamer,ledVPk
        if (statusVPK == False):
            statusVPK = True
            ledKamer.on()
            ledVPk.off()
        else:
            statusVPK = False
            ledKamer.off()
  
while True:
    buttonkamer103.when_activated = Kamer.oproep
    buttonkamer104.when_activated = Kamer.oproep
    buttonkamer105.when_activated = Kamer.oproep

    buttonVPK.when_activated = verpleegkundige.oproep