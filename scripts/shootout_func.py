import random
import time

def shootout(publisher_name):
	rand1 = random.randrange(10, 30, 1)
	rand2 = random.randrange(-10, -30, 1)
	rand = random.choice([rand1, rand2])
    msg = SSL()
    time.sleep(5)
    msg.cmd_vel.linear.x = 0.2
    publisher_name.publish(msg)
    time.sleep(1)
    msg.cmd_vel.linear.x = 0.2
    publisher_name.publish(msg)
    msg.kicker = True
    time.sleep(2)
    msg.cmd_vel.linear.x = 0.2
    msg.cmd_vel.angular.z = rand * 0.001
    publisher_name.publish(msg)
    time.sleep(2.5)
    msg.cmd_vel.linear.x = 0.0
    msg.cmd_vel.angular.z = 0.0
    msg.kicker = False
    publisher_name.publish(msg)
    time.sleep(1)

def Goleiro(publisher_name):
    msg = SSL()
    msg.cmd_vel.linear.y = 0.2
    publisher_name.publish(msg)
    time.sleep(1)
    msg.cmd_vel.linear.y = -0.2
    publisher_name.publish(msg)
    time.sleep(2)
    msg.cmd_vel.linear.y = 0.2
    publisher_name.publish(msg)
    time.sleep(1)