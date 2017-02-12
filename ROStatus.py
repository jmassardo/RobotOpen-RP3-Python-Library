'''
ROStatus.py
Diagnostic data for the controller

RobotOpen RP3 Library
By James Massardo
2/4/2017


Based on the RobotOpen HA Library by 221 Robotics // Eric Barch
www.robotopen.biz
'''
import socket
PORT = 22211
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(('', PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data