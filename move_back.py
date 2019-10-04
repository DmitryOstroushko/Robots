#!/usr/bin/env python
import rospy
import roslib
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

k0 = 10

def callback(msg):
    global k0
    k0 = msg.ranges[180]


def move():
    rospy.init_node('robot_24', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    scan_publisher = rospy.Subscriber('/scan', LaserScan, callback)
    lidar_msg = LaserScan()

    filname = 'n'
    with open(filname) as f_obj:
        line = f_obj.readlines()
    n = int(line[0])
    m = 0
    new_dist = float(line[1]) - 0.04
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        m += 1
        vel_msg.angular.z = -1
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        if k0 <= new_dist:
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            break
    while not rospy.is_shutdown():
        n -= 1
        vel_msg.linear.x = 100
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        if n == 0:
            break
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    while not rospy.is_shutdown():
        m -= 1
        vel_msg.angular.z = -1
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        if m == 0:
            break
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
