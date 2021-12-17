import RPi.GPIO as GPIO
import threading
from gpiozero import LED, Button
from datetime import datetime
import csv
import time
import threading as th


ledRoom = LED(4)
ledNurse = LED(17)
buttonRoom103 = Button(2)
buttonRoom103._hold_repeat = False
buttonRoom104 = Button(16)
buttonRoom105 = Button(23)
buttonNurse = Button(10)

statusNurse = False
# status False = geen VPK aanwezig in de kamer
# status True = VPK aanwezig in de kamer


ledRoom.off()


class room():
    def __init__(self, roomNumber, patient, button):
        self.roomNumber
        self.patient
        self.button
        self.source

    def locateSource(source):
        if(source == buttonRoom103):
            return "room 103"
        elif(source == buttonRoom104):
            return "room 104"
        elif(source == buttonRoom105):
            return "room 105"
        else:
            return "source unknown"

    def call(source):
        global ledRoom,ledNurse
        ledRoom.blink()
        ledNurse.on()
        current_date_time = datetime.now()
        newCall = [room.locateSource(source), current_date_time,]
        with open ('/home/pi/Project-Ai/calls.csv', 'a+', newline='') as file:
            file_write = csv.writer(file)
            file_write.writerow(newCall)
            file.close()
            

class Nurse():
    def call():
        global statusNurse, ledRoom,ledNurse
        if (statusNurse == False):
            statusNurse = True
            ledRoom.on()
            ledNurse.off()
        else:
            statusNurse = False
            ledRoom.off()

while True:
    buttonRoom103.when_activated = room.call
    buttonRoom104.when_activated = room.call
    buttonRoom105.when_activated = room.call

    buttonNurse.when_activated = Nurse.call