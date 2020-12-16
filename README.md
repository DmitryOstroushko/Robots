# Robots

## About project
This project was created during hackaton __"ROBOTS is our everything"__ organazied by __School 21__.  
The aim of the project is to create a script in Python language which contols a robot under ROS (Robot Operating System).  
A task consists from three parts:  
1. To move the robot forward until it meets an obstacle. The robot must stop at a distance of about 30 centimeters in front of the obstacle  
2. To rotate the robot 180 degrees  
3. To move the robot back to a start point  

## Scripts
There are two scripts: [move_forward.py](https://github.com/DmitryOstroushko/Robots/blob/master/move_forward.py) and [move_back.py](https://github.com/DmitryOstroushko/Robots/blob/master/move_back.py).  

Script [move_forward.py](https://github.com/DmitryOstroushko/Robots/blob/master/move_forward.py) moves a robot forward step by step. The script controls distance between the robot and an obstacle on each step. When a distance is less than 30 centimeters the robots stops. At this moment the script saves a length of a path which it has moved. Then the robots rotates 180 degrees.  

Script [move_back.py](https://github.com/DmitryOstroushko/Robots/blob/master/move_back.py) moves the robot straight, a length of a way equals a value saved in [move_forward.py](https://github.com/DmitryOstroushko/Robots/blob/master/move_forward.py) script. It supposed that the robot moves back to the start point. 
