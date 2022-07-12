#! /usr/bin/env python
import time
import numpy as np
import rospy
from math import radians
from math import radians
from geometry_msgs.msg import Twist

class GoForward():
    def __init__(self):
        # initiliaze
        rospy.init_node('GoForward', anonymous=False)

	# tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
	# Create a publisher which can "talk" to TurtleBot and tell it to move
        # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
     
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(10)

        # Twist is a datatype for velocity      #using multiple move_cmd as the import and sleep for a long re
        move_cmd_1 = Twist()
        move_cmd_2 = Twist()
        move_cmd_3 = Twist()
        move_cmd_4 = Twist()        
        move_cmd_5 = Twist()
	# let's go forward at 0.2 m/s
        move_cmd_1.linear.x = 0.2
	# let's turn at 0 radians/s
        move_cmd_1.angular.z = radians(30)  
        move_cmd_2.linear.x = 0.1
        move_cmd_2.angular.z = radians(30)                                  
        move_cmd_3.linear.x = 0.1
        move_cmd_3.angular.z = 0     
        move_cmd_4.linear.x = 0.2
        move_cmd_4.angular.z = 0     
        move_cmd_5.linear.x = 0.1
        move_cmd_5.angular.z = radians(30)       
	# as long as you haven't ctrl + c keeping doing...
        while not rospy.is_shutdown():
	    # publish the velocity
            self.cmd_vel.publish(move_cmd_1)
	    # wait for 0.1 seconds (10 HZ) and publish again
            time.sleep(1)
            self.cmd_vel.publish(move_cmd_2)
            time.sleep(1)
            self.cmd_vel.publish(move_cmd_3)
            time.sleep(1)
            self.cmd_vel.publish(move_cmd_4)
            time.sleep(1)
            self.cmd_vel.publish(move_cmd_5)
            time.sleep(1)
            r.sleep()
                        
        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        GoForward()
    except:
        rospy.loginfo("GoForward node terminated.")