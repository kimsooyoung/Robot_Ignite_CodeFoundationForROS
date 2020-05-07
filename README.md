# Robot Ignite Code Foundation for ROS Prerequisites Exam

### Project Status:

![issue_badge](https://img.shields.io/badge/exam%20score-6.5-orange) 

## [Robot Ignite](https://www.theconstructsim.com/)의 첫번째 코스 Code Foundation for ROS의 시험 솔루션입니다.

시험은 다음과 같은 환경에서 이루어집니다.  

![python_exam_scene](https://user-images.githubusercontent.com/12381733/81247607-66d3d500-9055-11ea-8e4f-d6360c34122d.png)


시험은 크게 두 파트로 나뉩니다.

- Linux for Robotics
- Python for Robotics

## Part 1: Linux for Robotics

### Task 0

Inside your workspace (~/catkin_ws/src/), create a new folder named linux_exam. Inside this folder you will place all the files required for the exam. The full path has to be like this:

``` bash
/home/user/catkin_ws/src/linux_exam
```

### Task 1

Inside the linux_exam folder, create a new bash script named task1.sh, that does the following:

* First, it moves inside the linux_exam folder.
* Once it is there, it generates a folder structure like the following one: this->is->my->linux->exam (check Specifications)
* Inside the final folder, named exam, it creates a new file named my_file.py
* Finally, it prints to the screen the following string:

> This bash script has finished!

#### Specifications

* The string printed at the end MUST be exactly the same as the one showed above.
* The full folders structure has to be like this:

``` bash
/home/user/catkin_ws/src/linux_exam/this/is/my/linux/exam/my_file.py
```
### Task 2

Given the following ROS commands:

To make the Turtlebot robot perform a small square movement:

``` bash
rosrun linux_exam small_square.py
```

To make the Turtlebot robot perform a medium square movement:

``` bash
rosrun linux_exam medium_square.py
```

To make the Turtlebot robot perform a big square movement:

```bash
rosrun linux_exam big_square.py
```

Inside the `linux_exam` folder, create a new bash script, named `task2.sh`, that does the following:

It receives one parameter, which can contain one of the following values:

* small_square
* medium_square
* big_square

If the parameter is **small_square**, the bash script will make the Turtlebot robot perform the small square movement.
If the parameter is **medium_square**, the bash script will make the Turtlebot robot perform the medium square movement.
If the parameter is **big_square**, the bash script will make the Turtlebot robot perform the big square movement.

#### Specifications

The name of the parameters received by your bash script MUST be exactly the same as the ones specified above.

### Task 3

Inside the linux_exam folder, create a new bash script, named task3.sh, that does the following:

* First, it goes to the folder named exam, which you created in Task 1.
* Once there, it removes any existing file, and it creates 3 new ones, named like this: exam1.py, exam2.py and exam3.py.
* Finally, it assigns to each file the following permissions:

* exam1.py:

> Owner: Read, Write and Execute
> Group: Read and Execute
> All others: Read

* exam2.py:

> Owner: Read and Execute
> Group: None
> All others: Execute

* exam3.py:

> Owner: Write
> Group: Read
> All others: Execute

## Part 2: Python for Robotics

## Task 0

Inside your workspace `(~/catkin_ws/src/)`, create a new folder named `python_exam`. Inside this folder you will place all the files required for the exam. The full path has to be like this:
``` bash
/home/user/catkin_ws/src/python_exam
```

## Task 1

Inside the `python_exam` folder, create a new Python script named `task1.py`. Inside this script, create a function named `get_highest_lowest`. This function does the following:

* First, it creates an instance of the RobotControl class.
* Second, it gets all the values of the laser readings and it stores them into a list.
* Then, it compares all these laser values that you have stored in the list in order to detect the highest value and the lowest one.
* Finally, it returns the position in the list of the highest and lowest values (check Specifications).

#### Specifications
* The name of the function **MUST BE** the one specified above: `get_highest_lowest`.
* Bear in mind that the function doesn't have to return the values (highest and lowest), but the position in the list of those values.
* Your final (after you have tested that it works properly) program **MUST** contain the get_highest_lowest function, but **MUST NOT** contain any call to this function.
* The function has to return the position values in an specific order: first, it returns the position of the highest value and second, it returns the position of the lowest value.
* The laser readings list may contain some values that are expressed as inf. You MUST NOT take these values into account when calculating the highest and lowest value. Only take into account the numeric values.

```
#### Example
Given the following list:

[1,2,3,4,5,inf]
Your function has to return the position in the list of the numbers 1 (lowest) and 5 (highest).
```

### Task 2

Inside the python_exam folder, create a new Python script, named task2.py, that does the following:

* First, it starts moving the robot forwards while it captures de laser readings in front of the robot.
* When the laser readings detect that there's an obstacle (the wall) at less than 1 meter in front of the robot, the robot will stop its movement.
* After it stops, the robot will turn 90 degrees to his right, facing the opening corner in the room (check Specifications).

### Task 3

Inside the python_exam folder, create a new Python script, named task3.py. Inside this script, create a Python class named `ExamControl`.

The `ExamControl` class has to contain, at least, the following 2 methods:

* `get_laser_readings`: This method, when called, returns the values of the laser readings of the right and left side of the robot (check Specifications).
* `main`: This method, when called, makes the Turtlebot robot start the behavior described below:
Initially, the robot starts moving forward, towards the opening in the room.

While moving forward, your program keeps checking the values of the laser readings at the right and left sides of the robot.

When these laser values indicate that there are no obstacles detected neither at the left nor at the right side, the robot will stop it's movement.

Check the Example section for more details on the expected behavior.

#### Specifications
* The names of the class and the methods MUST BE exactly the same as the ones specified above.
* Your final program (after you have tested that it works properly) MUST contain the ExamControl class, but MUST NOT contain any instance of the class.
* The initial position of the robot for this exercise it's the end position of the robot in the previous Exercise
* The get_laser_readings method has to return the values in an specific order: first, it returns the value of the left side and second, it returns the value of the right side.
* We consider as laser readings from the left and right sides of the robot, the ones at the extremes of the laser values array. 
