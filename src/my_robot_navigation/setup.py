import os
from glob import glob
from setuptools import setup

package_name = 'my_robot_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
                (os.path.join('share', package_name), glob('launch/*.launch.py')),
                (os.path.join('share', package_name), glob('config/*.yaml')),   
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='markros2',
    maintainer_email='markose.aajan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'initpose = my_robot_navigation.initpose:main',
        ],
    },
)
