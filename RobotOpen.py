'''
RobotOpen.py
Main RobotOpen class

RobotOpen RP3 Library
By James Massardo
2/4/2017


Based on the RobotOpen HA Library by 221 Robotics // Eric Barch
www.robotopen.biz
'''
import socket
import binascii

# Port config (UDP)
PORT = 22211

# Define the socket for the UDP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

remoteIP = 0
remotePort = 0

class RobotOpen:
    def begin(self):
        # initiate robot
        print("Begin!")
        # Go ahead and bind to the port.
        sock.bind(('', PORT))

    def syncDS(self):
        # main sync control function
        self.handleData()
    
    def handleData(self):
        # read the packet and collect some info
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        self.parsePacket(data, addr)


    def parsePacket(self, data, addr):
        print "received message:", data
        if data[0] == 'h': # heartbeat packet
            outgoingPacket = binascii.unhexlify('68EE01')
            sock.sendto(outgoingPacket, addr)
        elif data[0] == 'c': # control packet
            print'control packet', data[1]
        elif data[0] == 's': # set parameter packet
            print('heartbeat packet')
        elif data[0] == 'g': # get parameter packet
            print('heartbeat packet')
        else:
            print('received some other weird packet')