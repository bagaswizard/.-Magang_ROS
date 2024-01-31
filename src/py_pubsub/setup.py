from setuptools import find_packages, setup

package_name = 'py_pubsub'
maintainer='bagas',
maintainer_email="bagaswrwn@gmail.com",
description='Examples of minimal publisher/subscriber using rclpy',
license='Apache License 2.0',

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bagas',
    maintainer_email='bagaswrwn@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'listener = py_pubsub.subscriber:main',
        ],
},
)
