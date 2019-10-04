#!/usr/bin/env python
import rospy
import roslib
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import json

k = 0
def callback(msg):
    global k
    k = msg.ranges[0]

def move():
    rospy.init_node('robot_24', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    scan_publisher = rospy.Subscriber('/scan', LaserScan, callback)
    lidar_msg = LaserScan()
    rate = rospy.Rate(10)
    n = 0
    filename = 'n'
    while not rospy.is_shutdown():
        n += 1
        vel_msg.linear.x = 1
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        if k <= 0.43:
            dist = k
            break
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    with open(filename, 'w') as f_obj:
        f_obj.write(str(n) + '\n')
        f_obj.write(str(dist))

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
