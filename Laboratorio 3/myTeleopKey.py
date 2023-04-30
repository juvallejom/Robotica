import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
import numpy as np

TERMIOS = termios

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

def Reset(x, y, ang):
    try: 
        rospy.wait_for_service('/turtle1/teleport_absolute')
        resetService = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute) 
        resetVar = resetService(x, y, ang)
    except rospy.ServiceException as e:
        print(str(e))

def Spin(lin, ang):
    try: 
        rospy.wait_for_service('/turtle1/teleport_relative')
        SpinService = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative) 
        SpinVar = SpinService(lin, ang)
    except rospy.ServiceException as e:
        print(str(e))
    
catk
if __name__ == '__main__':
    pubVel(0,0,0.1)
    try:
        while(1):
            teclado = getkey()
            if teclado == b'w': 
               pubVel(1,0,0.1)
            if teclado == b'a': 
               pubVel(0,1,0.1)
            if teclado == b's': 
               pubVel(-1,0,0.1)
            if teclado == b'd': 
               pubVel(0,-1,0.1)
            if teclado == b'r': 
               Reset(5.544445,5.544445,0.000000)
            if teclado == b' ': 
               Spin(0,np.pi)
            if teclado == b'f': 
                break
            
    except rospy.ROSInterruptException:
        pass
