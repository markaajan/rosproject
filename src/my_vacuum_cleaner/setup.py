from setuptools import setup
import os
from glob import glob

package_name = 'my_vacuum_cleaner'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),  
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
        	'coverage = my_vacuum_cleaner.coverage:main',
        ],
    },
)
