# -*- encoding: UTF-8 -*-

''' PoseInit: Small example to make Nao go to an initial position. '''

from optparse import OptionParser
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import time
import sys
from math import pi
NAO_IP = "nao2.local"
#NAO_IP = "localhost"

class Pose():
    def __init__(self):
        #ALModule.__init__(self, name)
        self.motionProxy  = ALProxy("ALMotion")
        self.postureProxy = ALProxy("ALRobotPosture")

        # Wake up robot
        self.motionProxy.wakeUp()

        # Send robot to Stand
        self.postureProxy.goToPosture("Stand", 0.5)
        print('Nao stands')

        # Go to rest position
        self.motionProxy.rest()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    naoBroker = ALBroker("naoBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port

    # Warning: pose must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global pose
    pose = Pose()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        naoBroker.shutdown()
        sys.exit(0)
