#!/usr/bin/env python
 
import rospy
from std_msgs.msg import Float64

rospy.init_node('laser_command')
pub = rospy.Publisher('laser_command_topic', Float64, queue_size=10)
speed=rospy.get_param('~speed',2)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  msg = Float64()
  msg.data=speed
  pub.publish(msg)
  rate.sleep()
