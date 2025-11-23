#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('even_number_talker')
pub = rospy.Publisher('talking', String, queue_size=10)
overflow_pub = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg = String()
    counter = 0
    while not rospy.is_shutdown():
        rospy.loginfo(counter)
        
        if counter >= 100:
            msg.data = str("OVERFLOW!!!!")
            overflow_pub.publish(msg)
            pub.publish(str(counter))
            counter = 0
        else:
            msg.data = str(counter)
            pub.publish(msg)
            counter += 2
        
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')