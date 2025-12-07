#!/usr/bin/env python3
import rospy
import math
import tf

if __name__ == '__main__': 
    rospy.init_node('tf_carrot')

    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    
    radius = 1.44 
    angular_speed = 0.84 
    
    starting_time = rospy.Time.now()
    
    while not rospy.is_shutdown():
        try:
            cur_time = rospy.Time.now()
            elapsed = (cur_time - starting_time).to_sec() 
            carrot_x = radius * math.cos(angular_speed * elapsed) 
            carrot_y = radius * math.sin(angular_speed * elapsed) 
            
            broadcaster = tf.TransformBroadcaster()
            broadcaster.sendTransform(
                (carrot_x, carrot_y, 0),
                tf.transformations.quaternion_from_euler(0, 0, 0),
                rospy.Time.now(),
                "carrot",  
                "turtle1"  
            )
 
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rate.sleep()