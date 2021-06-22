#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pubsub',
            node_executable='publisher',
            node_name='pub',
            output='log'),
    ])

