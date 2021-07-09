#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    ttbot3 = get_package_share_directory('turtlebot3_gazebo')
    local = get_package_share_directory('my_robot_slam')
    navi = get_package_share_directory('my_robot_navigation')
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ttbot3, 'launch/turtlebot3_house.launch.py')
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(local, 'localization.launch.py')
            ),
        ),
        #IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource(
        #       os.path.join(navi, 'navigation.launch.py')
        #    ),
        #),
        Node(
            package='pubsub',
            executable='publisher',
            name='set_initial_pose',
            output='screen'),
        Node(
           package='my_vacuum_cleaner',
           node_executable='coverage',
           node_name='coverage',
           output='screen'),




    ])
    
    
    


