#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16MultiArray


def callback(msg):
    res = []
    rospy.loginfo(f"Poly-node heard {msg.data}") 
    for ind, value in enumerate(msg.data, start=1):
        res.append(value ** (4-ind))

    send_msg = Int16MultiArray()
    send_msg.data = res
    pub.publish(send_msg)


rospy.init_node('polynomial')
pub = rospy.Publisher('to_sum', Int16MultiArray, queue_size=10)
rospy.Subscriber('to_poly', Int16MultiArray, callback, queue_size=10)

rospy.spin()
