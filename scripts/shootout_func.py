def shootout(publisher_name):
	rand1 = random.randrange(25, 50, 1)
	rand2 = random.randrange(-50, -25, 1)
	rand = random.choice([rand1, rand2])
    msg = SSL()
    time.sleep(5)
    msg.cmd_vel.linear.x = 0.5
    publisher_name.publish(msg)
    time.sleep(1)
    msg.cmd_vel.linear.x = 0.5
    publisher_name.publish(msg)
    msg.kicker = True
    time.sleep(2)
    msg.cmd_vel.linear.x = 0.5
    msg.cmd_vel.angular.z = rand * 0.01
    publisher_name.publish(msg)
    time.sleep(2.5)
    msg.cmd_vel.linear.x = 0.0
    msg.cmd_vel.angular.z = 0.0
    msg.kicker = False
    publisher_name.publish(msg)
    time.sleep(1)
