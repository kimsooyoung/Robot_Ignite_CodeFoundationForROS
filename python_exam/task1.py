from robot_control_class import RobotControl
import math

def get_highest_lowest():
    rc = RobotControl()
    laser = rc.get_laser_full()
    laser_dict = {}
    output = []
    for i, elem in enumerate(laser):
        if not math.isinf(elem):
            laser_dict[i] = elem
    max_val = max(laser_dict.values())
    min_val = min(laser_dict.values())
    print(max_val, min_val)

    for key, val in laser_dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if val == max_val:
            output.append(key)
            break

    for key, val in laser_dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if val == min_val:
            output.append(key)
            break
    return output

max_index, min_index = get_highest_lowest()
print(max_index, min_index)
