#!/usr/bin/env pybricks-micropython


###################################################################################################
#
#   Client side code for 2 robots finding the border of a table problem.
#   tourist.py
#   Santiago de Chile 16/04/2024
# 
#   Programmer: Rodrigo Cruz, Matias Toledo
#
###################################################################################################

#LIBRARIES 

from pybricks.hubs import EV3Brick
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

import urandom
import os

'''''
*
*
*
'''''

ev3 = EV3Brick()  # Initializes the Brick

#GET DEVICE NAME
with open('/etc/hostname') as hostname:
    myname = hostname.read()    #Name should be explorer
print(myname)

#MOTOR AND OTHER SETUPS
left_motor = Motor(Port.D)  # left motor attached on port D 
right_motor = Motor(Port.A)  # right motor attached on port A
robot = DriveBase(left_motor, right_motor, wheel_diameter = 55, axle_track = 105)  # wheel_diameter = 52  axle_track= 125
robot.settings(80)


# CONNECTION SETTINGS 
SERVER = 'Explorer'
client = BluetoothMailboxClient()
movement_box = TextMailbox('movement', client)

# print('waiting for connection...\n')
client.connect(SERVER)
# print('Connected movement mailbox to Server\n')


final_message = []
movement_box.wait()
message = movement_box.read()
array_message = message.split(' ')
final_message = array_message
final_len = len(final_message) - 1

# comprobation
print(final_len,'\n')
print(final_message,'\n')

#Move robot
for i in range(0, final_len , 2):   #repeat until no data left on array 
    distance = int(final_message[i], 0)
    angle = int(final_message[i + 1], 0)

    print(distance,'\n')
    print(angle,'\n')

    #go forward
    robot.straight(-distance)
    robot.stop()

    #go reverse
    robot.straight(100)
    robot.stop()
    
    #gorotate
    robot.turn(angle)
    robot.stop()

