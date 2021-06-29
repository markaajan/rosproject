#from action_msgs.msg import GoalStatus
from nav2_msgs.action import FollowWaypoints
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



width = 0.13

def genpoints (a,b,c,d): #Send points ,x1,y1,x2,y2

    points = []
    if a > c:
        y = a
        a = c
        c = y
        y = b
        b = d
        d = y
        # This is to flip the coordinated for ease of handling


    n = math.floor((c - a) / width)
    flag = False
    for i in range(n):
        for j in range(i+1):
            if flag:
                points.append(((a + (width * j)),(b - (width * (i - j)))))
            else:
                points.append(((a + (width * (i-j))), (b - (width *  j))))
        flag = not flag


    return (points)

def main(args=None):
    rclpy.init(args=args)

    action_client = MinimalActionClient()
    points = genpoints(-6.9064,0.58458,-5.16437,-3.65905)
    rgoal = PoseStamped()
    rgoal.header.frame_id = "map"
    rgoal.header.stamp.sec = 0
    rgoal.header.stamp.nanosec = 0
    rgoal.pose.position.z = 0.0
    rgoal.pose.position.x = 1.93793
    rgoal.pose.position.y = -1.88138
    rgoal.pose.orientation.w = 1.0

    # bgoal = PoseStamped()
    # bgoal.header.frame_id = "map"
    # bgoal.header.stamp.sec = 0
    # bgoal.header.stamp.nanosec = 0
    # bgoal.pose.position.z = 0.0
    # bgoal.pose.position.x = -2.0
    # bgoal.pose.position.y = -1.0
    # bgoal.pose.orientation.w = 1.0
    
    mgoal = []
    for point in points:
        newgoal = PoseStamped()
        newgoal.pose.position.x = point[0]
        newgoal.pose.position.y = point[1]
        mgoal.append(newgoal)

    action_client.send_points(mgoal)

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
