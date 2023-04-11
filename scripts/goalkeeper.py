#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import *
from gazebo_msgs.msg import *
from grsim_ros_bridge_msgs.msg import *
from krssg_ssl_msgs.msg import *
import math
import random

pelota = SSL_DetectionBall()	
robot0 = SSL_DetectionRobot()
robot1 = SSL_DetectionRobot()
robot2 = SSL_DetectionRobot()
robot3 = SSL_DetectionRobot()
robot4 = SSL_DetectionRobot()
ballx = 0
bally = 0

def posball():
    global ballx, bally
    
    try:
        ballx= pelota[0].x
        bally= pelota[0].y
    except:
        return

def player_blue(data):
    global robot0,robot1,robot2,robot3,robot4,pelota
                
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
                
    pelota = data.balls


if __name__=="__main__":
    rospy.init_node("Goleiro", anonymous=False)
    
    rospy.Subscriber("/vision", SSL_DetectionFrame, player_blue)
    pub = rospy.Publisher('/robot_blue_3/cmd', SSL, queue_size=10)

    r = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        ssl_msg = SSL()
        robot = robot3
        car_x = robot.x
        car_y = robot.y

        diff_x = -random.randint(4400,4600) - car_x
        diff_y = bally  - car_y

        if diff_x!=0:
            theta = math.atan(diff_y/diff_x)
        else:
            theta = 0 

        dist = math.sqrt(diff_x * diff_x + diff_y * diff_y)
        
        if dist < 0:
            ssl_msg.cmd_vel.linear.x = 0
            ssl_msg.cmd_vel.angular.z = 0

        else:
            print(bally, car_y)

            if car_x > - random.randint(4400,4600):
                ssl_msg.cmd_vel.linear.x = - 5
                ssl_msg.cmd_vel.angular.z = (theta - robot.orientation ) * 5

            else:
                ssl_msg.cmd_vel.linear.x =  5
                ssl_msg.cmd_vel.angular.z =  (theta - robot.orientation) * 5
                           
        pub.publish(ssl_msg)
        posball()

        r.sleep()