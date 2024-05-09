#!/usr/bin/env pybricks-micropython

# Server side code for 2 robots finding the border of a table problem.
# explorer.py
# Santiago de Chile 16/04/2024
# 
# Programmer: Rodrigo Cruz, Matias Toledo

from pybricks.hubs import EV3Brick
from pybricks.messaging import BluetoothMailboxServer, NumericMailbox, TextMailbox
from pybricks.ev3devices import ColorSensor, Motor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.robotics import DriveBase

import urandom
import os




csensor = ColorSensor(Port.S1)
SPEED = 190
MAX = 5
turns = 0

ev3 = EV3Brick()  # Initializes the Brick

#Get device name
with open('/etc/hostname') as hostname:
    myname = hostname.read()    #Name should be explorer
print(myname)

#Motor and other setups
left_motor = Motor(Port.D)  # left motor attached on port D 
right_motor = Motor(Port.A)  # right motor attached on port A
robot = DriveBase(left_motor, right_motor, wheel_diameter = 55, axle_track = 105)  # wheel_diameter = 52  axle_track= 125
ev3.speaker.set_volume(100)
ev3.speaker.beep(500, 500)

#Mailbox creation
server = BluetoothMailboxServer()

distance_box = TextMailbox('distance', server) #Mailbox for the distance
angle_box = TextMailbox('angle', server)    #Mailbox for the turning angle

#ev3.screen.print('waiting for connection...\n')
#server.wait_for_connection()
#ev3.screen.print('Tourist Succesfully Connected\n')

#Move robot
ev3.screen.print(csensor.reflection())
while True: #Turns MAX times
    ev3.screen.print('I DRIVE \n')
    robot.drive(SPEED, 0)  
    if csensor.reflection() < 18: #While the color is not black, keep moving  
        robot.stop()  
        robot.straight(-100)
        n = urandom.randrange(-180,180,90)
        robot.turn(n)    #Rotate in position
        turns = turns + 1
        distance = robot.distance()   #distance in mm
        angle = robot.angle()         #Angle int
        
        ev3.screen.print(distance,'\n')
        ev3.screen.print(angle,'\n')

        ev3.reset()
        



