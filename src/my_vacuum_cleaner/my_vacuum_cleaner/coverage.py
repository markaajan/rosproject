#from action_msgs.msg import GoalStatus
import numpy as np
import matplotlib.pyplot as plt
from nav2_msgs.action import FollowWaypoints
#from nav2_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
import math as math

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class MinimalActionClient(Node):

    def __init__(self):
        super().__init__('minimal_action_client')
        self._client = ActionClient(self, FollowWaypoints, '/FollowWaypoints')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            self.send_points(mgoal)
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback        
        self.get_logger().info('Received feedback: {0}'.format(feedback.current_waypoint))

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.missed_waypoints))
        # Shutdown after receiving a result
        #rclpy.shutdown()

    def send_points(self, points):
        # self.get_logger().info('Waiting for action server...')
        # self._action_client.wait_for_server()
        
        msg = FollowWaypoints.Goal()
        msg.poses = points
        
        self._client.wait_for_server()
        self._send_goal_future = self._client.send_goal_async(msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)    

        self.get_logger().info('Sending goal request...')

        # self._send_goal_future = self._action_client.send_goal_async(
        #     msg,
        #     feedback_callback=self.feedback_callback)

        # self._send_goal_future.add_done_callback(self.goal_response_callback)


points = []
width = 0.5

def genpoints (a,b,c,d): #Send points ,x1,y1,x2,y2

    global points
    if a > c:
        y = a
        a = c
        c = y
        y = b
        b = d
        d = y
        # This is to flip the coordinated for ease of handling
    cc = c - ((c - a) % width)
    dd = d - ((d - b) % width)
    aa = a
    bb = b
    points.append((aa,bb))
    # if c-a < b-d:
    #     n = math.floor((c - a) / width)
    # else:
    #     n = math.floor((d - b) / width)
    # aa = a
    # bb = b
    # flag = False
    # for i in range(n):
    #     for j in range(i+1):
    #         if flag:
    #             points.append(((a + (width * j)),(b - (width * (i - j)))))
    #             aa = a + (width * j)
    #             bb = b - (width * (i - j))
    #         else:
    #             points.append(((a + (width * (i-j))), (b - (width * j))))
    #             aa = a + (width * (i - j))
    #             bb = b - (width * j)
    #     flag = not flag
    # if aa == a:
    #     bb = bb - n
    #     points.append(aa,bb)
    #     while bb > d:
    #         while aa > c:
    #             bb = bb + n
    #             aa = aa + n
    flag = True
    while aa <= cc:
        if flag:
            if bb > dd:
                bb = bb - width
                if ~((aa >= -3.26) & (aa <= -1.47) & (bb <= 2.977) & (bb >= 1.8366)) :
                    points.append((aa,bb))
            else:
                flag = False
                aa = aa + width
        else:
            if bb < b:
                bb = bb + width
                if ~((aa >= -3.26) & (aa <= -1.47) & (bb <= 2.977) & (bb >= 1.8366)):
                    points.append((aa,bb))
            else:
                flag = True
                aa = aa + width




def main(args=None):
    rclpy.init(args=args)

    action_client = MinimalActionClient()
    genpoints(-6.7064,0.23458,-5.1437,-2.50905)
    genpoints(-6.3681,4.4557,-5.9061,2.055)
    genpoints(-4.02066,4.2101,-0.19589,0.6802)
    genpoints(0.69472,4.7989,1.6596,2.2501)
    genpoints(3.2304,4.5252,6.8877,0.5546)

    rgoal = PoseStamped()
    rgoal.header.frame_id = "map"
    rgoal.header.stamp.sec = 0
    rgoal.header.stamp.nanosec = 0
    rgoal.pose.position.z = 0.0
    rgoal.pose.position.x = 1.93793
    rgoal.pose.position.y = -1.88138
    rgoal.pose.orientation.w = -1.0
    # rgoal.pose.orientation.x = 0.0
    # rgoal.pose.orientation.y = 0.0
    # rgoal.pose.orientation.z = 0.0

    bgoal = PoseStamped()
    bgoal.header.frame_id = "map"
    bgoal.header.stamp.sec = 0
    bgoal.header.stamp.nanosec = 0
    bgoal.pose.position.z = 0.0
    bgoal.pose.position.x = 1.22
    bgoal.pose.position.y = 0.29
    bgoal.pose.orientation.w = -1.0
    # bgoal.pose.orientation.x = 0.0
    # bgoal.pose.orientation.y = 0.0
    # bgoal.pose.orientation.z = 0.0


    global mgoal
    mgoal = [rgoal, bgoal]
    for point in points:
        newgoal = PoseStamped()
        newgoal.pose.position.x = point[0]
        newgoal.pose.position.y = point[1]
        # newgoal.pose.orientation.w = 0.0
        # newgoal.pose.orientation.x = 0.0
        # newgoal.pose.orientation.y = 0.0
        # newgoal.pose.orientation.z = 0.0
        mgoal.append(newgoal)

    goal1 = PoseStamped()
    goal1.header.frame_id = "map"
    goal1.header.stamp.sec = 0
    goal1.header.stamp.nanosec = 0
    goal1.pose.position.x = 5.55
    goal1.pose.position.y = -0.635
    # goal1.pose.orientation.w = 0.0
    # goal1.pose.orientation.x = 0.0
    # goal1.pose.orientation.y = 0.0
    # goal1.pose.orientation.z = 0.0

    goal2 = PoseStamped()
    goal2.header.frame_id = "map"
    goal2.header.stamp.sec = 0
    goal2.header.stamp.nanosec = 0
    goal2.pose.position.x = 5.599
    goal2.pose.position.y = -4.713009834289551
    # goal2.pose.orientation.w = 0.0
    # goal2.pose.orientation.x = 0.0
    # goal2.pose.orientation.y = 0.0
    # goal2.pose.orientation.z = 0.0

    goal3 = PoseStamped()
    goal3.header.frame_id = "map"
    goal3.header.stamp.sec = 0
    goal3.header.stamp.nanosec = 0
    goal3.pose.position.x = 7.137545585632324
    goal3.pose.position.y = -4.635471343994141
    # goal3.pose.orientation.w = 0.0
    # goal3.pose.orientation.x = 0.0
    # goal3.pose.orientation.y = 0.0
    # goal3.pose.orientation.z = 0.0

    goal35 = PoseStamped()
    goal35.header.frame_id = "map"
    goal35.header.stamp.sec = 0
    goal35.header.stamp.nanosec = 0
    goal35.pose.position.x = 6.976057052612305
    goal35.pose.position.y = -2.6943585872650146
    # goal35.pose.orientation.w = 0.0
    # goal35.pose.orientation.x = 0.0
    # goal35.pose.orientation.y = 0.0
    # goal35.pose.orientation.z = 0.0

    goal4 = PoseStamped()
    goal4.header.frame_id = "map"
    goal4.header.stamp.sec = 0
    goal4.header.stamp.nanosec = 0
    goal4.pose.position.x = 7.185612678527832
    goal4.pose.position.y = -0.7632512450218201
    # goal4.pose.orientation.w = 0.0
    # goal4.pose.orientation.x = 0.0
    # goal4.pose.orientation.y = 0.0
    # goal4.pose.orientation.z = 0.0

    goal5 = PoseStamped()
    goal5.header.frame_id = "map"
    goal5.header.stamp.sec = 0
    goal5.header.stamp.nanosec = 0
    goal5.pose.position.x = -0.6288080811500549
    goal5.pose.position.y = -1.1790292263031006
    # goal5.pose.orientation.w = 0.0
    # goal5.pose.orientation.x = 0.0
    # goal5.pose.orientation.y = 0.0
    # goal5.pose.orientation.z = 0.0

    mgoal.append(goal1)
    mgoal.append(goal2)
    mgoal.append(goal3)
    mgoal.append(goal35)
    mgoal.append(goal4)
    mgoal.append(goal5)


    plt.scatter(*zip(*points))
    plt.show()
    action_client.send_points(mgoal)
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
