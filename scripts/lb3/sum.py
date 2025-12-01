#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16MultiArray, Int16

def callback(msg):
    total = 0
    rospy.loginfo(f"Sum-node heard {msg.data}") 
    for item in msg.data:
        total += item
    send_msg = Int16()
    send_msg.data = total
    pub.publish(total)

rospy.init_node('sum')
pub = rospy.Publisher('to_request', Int16, queue_size=10)
rospy.Subscriber('to_sum', Int16MultiArray, callback, queue_size=10)
rospy.spin()
