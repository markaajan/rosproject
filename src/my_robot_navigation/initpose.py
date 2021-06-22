#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisherClass(Node):

    def __init__(self):
        super().__init__('initpose')
        self.mypub = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 1)
        self.create_timer(0.1, self.mytimercallback)

    def mytimercallback(self):
        mymsg = PoseWithCovarianceStamped()
        mymsg.header.frame_id = 'map'
        mymsg.pose.pose.position.x = -1.93
        mymsg.pose.pose.position.y = -0.73
        mymsg.pose.pose.position.z = 0.0
        mymsg.pose.pose.orientation.x = 0.0
        mymsg.pose.pose.orientation.y = 0.0
        mymsg.pose.pose.orientation.z = 0.0
        mymsg.pose.pose.orientation.w = 1.0
        self.mypub.publish(mymsg)

def main():
    rclpy.init()
    myfirstpublisher = MyPublisherClass()
    try:
        rclpy.spin(myfirstpublisher)
    except KeyboardInterrupt:
        pass
    myfirstpublisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


