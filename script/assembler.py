#!/usr/bin/env python
#from sensor_msg import PointCloud
import roslib; roslib.load_manifest('laser_assembler')
import rospy; from laser_assembler.srv import *
import sensor_msgs.msg
from sensor_msgs.msg import PointCloud

rospy.init_node("test_client")
rospy.wait_for_service("assemble_scans")
pub = rospy.Publisher("cloud_result",PointCloud, queue_size=10)


rate = rospy.Rate(0.2)

while not rospy.is_shutdown():
#msg = PointCloud()
  try:
    assemble_scans = rospy.ServiceProxy('assemble_scans', AssembleScans)
    resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
    print "Got cloud with %u points" % len(resp.cloud.points)
  except rospy.ServiceException, e:
    print "Service call failed: %s"%e
# msg.data = resp
  pub.publish(resp.cloud)
  rate.sleep()
