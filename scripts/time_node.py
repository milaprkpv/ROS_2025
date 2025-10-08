#!/usr/bin/env python3
import rospy
import datetime
from std_msgs.msg import String

def simple_time_publisher():
    # Инициализируем узел
    rospy.init_node('simple_time_publisher', anonymous=True)
    
    # Создаем издателя
    pub = rospy.Publisher('current_time', String, queue_size=10)
    
    # Устанавливаем период 5 секунд
    rate = rospy.Rate(0.2) 
    
    rospy.loginfo("Простой узел времени запущен. Период: 5 секунд")
    
    while not rospy.is_shutdown():
        # Получаем текущее время
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Создаем и публикуем сообщение
        message = f"Время: {current_time}"
        pub.publish(message)
        rospy.loginfo(message)
        
        # Ждем 5 секунд
        rate.sleep()

if name == '__main__':
    try:
        simple_time_publisher()
    except rospy.ROSInterruptException:
        rospy.loginfo("Узел остановлен")
