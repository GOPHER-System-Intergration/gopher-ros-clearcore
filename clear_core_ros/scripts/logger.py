#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import serial
import json
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    clearCore = serial.Serial('/dev/ttyACM0', 115200,timeout=.1)
    while not rospy.is_shutdown():
        data = clearCore.readline().decode("utf-8").strip()
        if len(data) > 0:
            status = json.loads(data)
            print(status)
        # print("\n ---------------")
        # rospy.loginfo(data)
        
        # pub.publish(jsondata)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass