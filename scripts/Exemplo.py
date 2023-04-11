#! /usr/bin/env python3
import rospy
from grsim_ros_bridge_msgs.msg import *
from krssg_ssl_msgs.msg import *
from geometry_msgs.msg import *

Bola =   SSL_DetectionBall()
robot0 = SSL_DetectionRobot()
robot1 = SSL_DetectionRobot()
robot2 = SSL_DetectionRobot()
robot3 = SSL_DetectionRobot()
robot4 = SSL_DetectionRobot()


def position_ball(data):
	global Bola		
	Bola = data.balls

def player_blue(data):
	global robot0,robot1,robot2,robot3,robot4
				
	for i in range(0, len(data.robots_blue)):
		id_robots = data.robots_blue[i].robot_id
		if id_robots == 0:
			robot0 = data.robots_blue[i]
		if id_robots == 1:
			robot1 = data.robots_blue[i]
		if id_robots == 2:
			robot2 = data.robots_blue[i]
		if id_robots == 3:
			robot3 = data.robots_blue[i]
		if id_robots == 4:
			robot4 = data.robots_blue[i]

if __name__ == "__main__":
    rospy.init_node("test_ssl", anonymous = False)

    rospy.Subscriber("/vision", SSL_DetectionFrame, position_ball)
    rospy.Subscriber("/vision", SSL_DetectionFrame, player_blue)
    
    pub = rospy.Publisher('/robot_blue_0/cmd', SSL, queue_size=10)

    r = rospy.Rate(10)
    
    while not rospy.is_shutdown():
 
        print("ROBO: ",robot0.x, robot0.y)
        ssl_msg = SSL()
        ssl_msg.cmd_vel.linear.x = 10.1
        pub.publish(ssl_msg)
        r.sleep()

