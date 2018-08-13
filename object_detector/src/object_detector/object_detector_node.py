#!/usr/bin/env python
import rospy
import object_detector

def main():
    rospy.init_node('object_detector', anonymous=True)

    detector = object_detector.ObjectDetector(rospy.get_param('~laser_topic', '/robot_0/base_scan'))

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
