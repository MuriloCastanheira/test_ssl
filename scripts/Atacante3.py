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
    rospy.init_node("Atacante_3", anonymous=False)
    
    rospy.Subscriber("/vision", SSL_DetectionFrame, player_blue)
    #print(rospy.get_param('Atacante3'))
    #pub = rospy.Publisher(rospy.get_param('atacante3'), SSL, queue_size=10)
    topic = rospy.get_param('Atacante3')
    pub = rospy.Publisher(topic["Atacante3"], SSL, queue_size=10)

    r = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        vel_max =0.5
        ssl_msg = SSL()
        robot = robot2
        car_x = robot.x
        car_y = robot.y
        #gol.x = 2000
        #gol.y = 0.0
        velocidade = 0
        x = 0
        y = 0
        dist_ballcar = math.sqrt((ballx - car_x) * (ballx - car_x) + (bally - car_y) * (bally - car_y))
        

        if  dist_ballcar > 1000: # vai pra traz do carrinho
            x = ballx - 1000
            y = bally 
            velocidade = vel_max
            print("1")
        else:

            x = ballx 
            y = bally 
            velocidade = vel_max
            print("2")

        diff_x = x - car_x
        diff_y = y - car_y # bally - car_y

        if diff_x!=0:
            theta = math.atan(diff_y/diff_x)
        else:
            theta = 0 

        dist = math.sqrt(diff_x * diff_x + diff_y * diff_y)

        if car_x > x:
            ssl_msg.cmd_vel.linear.x = - velocidade
            ssl_msg.cmd_vel.angular.z = (theta - robot.orientation ) * 5

        else:
            ssl_msg.cmd_vel.linear.x =  velocidade
            ssl_msg.cmd_vel.angular.z =  (theta - robot.orientation) * 5
                    
        pub.publish(ssl_msg)
        posball()

        r.sleep()