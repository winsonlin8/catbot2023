from setuptools import find_packages, setup

package_name = 'sensors'

setup(
    name=package_name,
    version='0.0.2',  
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='winsonl8',
    maintainer_email='winsonlin411@gmail.com',
    description='Quadruped catbot sensors and motor control package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_controller = sensors.motor_controller:main',
        ],
    },
)
