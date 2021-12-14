import RPi.GPIO as GPIO
from gpiozero import LED, Button
from datetime import datetime
import csv


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

    def oproep(source):
        global calls, ledKamer,ledVPk
        ledKamer.blink()
        ledVPk.on()
        current_date_time = datetime.now()
        new_list = [source, current_date_time]
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
    if(buttonkamer103.is_active==True):
        source = "room 103"
        Kamer.oproep(source)
    elif(buttonkamer104.is_active==True):
        source = "room 104"
        Kamer.oproep(source)
    elif(buttonkamer105.is_active==True):
        source = "room 105"
        Kamer.oproep(source)
        

    buttonVPK.when_activated = verpleegkundige.oproep
    
