from robot_control_class import RobotControl
import math

rc = RobotControl()
laser = rc.get_laser_full()

while laser[360] >= 1:
    rc.move_straight()
    laser = rc.get_laser_full()
rc.stop_robot()

rc.turn("clockwise", 0.2, 7)
