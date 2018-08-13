import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool

class ObjectDetector:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.subscriber = rospy.Subscriber(self.topic_name, LaserScan, self.scan_cb)
        self.publisher = rospy.Publisher('~object_detected', Bool, queue_size=1)

    def scan_cb(self, msg):
	previous_range = msg.ranges[0]
        detected_close = False
        for index in range(1, len(msg.ranges)):
            current_range = msg.ranges[index]
            if current_range < previous_range - 1.0: # Detect a laser distance jump of at least 1 meter
                detected_close = True
            else:
                if detected_close and current_range > previous_range + 1.0: # Detect a laser distance jump of at least 1 meter
                    publisher_message = Bool()
                    publisher_message.data = True
                    self.publisher.publish(publisher_message)
            previous_range = msg.ranges[index]
