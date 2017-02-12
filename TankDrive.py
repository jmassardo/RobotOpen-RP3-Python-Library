# Add header with references and credits and stuff here
from RobotOpen import *

# Let's get the party started!

def enabled():
    # Put your code here to do stuff
    print("enabled!")

def disabled():
    # safety code
    # make sure to stop any motors and turn off any other moving parts
    print("disabled!")

def timedtasks():
    # periodic stuff like publishing data to the dashboard
    Dashboard = RODashboard()
    Dashboard.publish()

#setup ports and stuff here
#Call the begin function in the RobotOpen Main class
Robot = RobotOpen()
Robot.begin()

while(True):
    Robot.syncDS()