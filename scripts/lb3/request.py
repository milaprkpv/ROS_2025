#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16MultiArray, Int16



def callback(msg):
    rospy.loginfo(f"The result is {msg.data}")
    rospy.signal_shutdown('Recieved a result msg')

def request():
    rospy.init_node('request')
    pub = rospy.Publisher('to_poly', Int16MultiArray, queue_size=10)
    rospy.Subscriber('to_request', Int16, callback, queue_size=10)

    a = int(input("Enter a number a: "))
    b = int(input("Enter a number b: "))
    c = int(input("Enter a number c: "))
    
    msg = Int16MultiArray()
    msg.data = [a, b, c]
    pub.publish(msg)
    rospy.spin()

request()
