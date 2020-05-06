from robot_control_class import RobotControl
import math

class ExamControl:
    def get_laser_readings(self):
        output = []
        rc = RobotControl()
        laser = rc.get_laser_full()
        output.append(laser[719])
        output.append(laser[0])        
        return output
    
    def main(self):
        rc = RobotControl()
        d_left, d_right = self.get_laser_readings()
        print(d_left, d_right)
        while True:
            rc.move_straight()
            d_left, d_right = self.get_laser_readings()
            print(d_left, d_right)
            if ( math.isinf(d_left)) and ( math.isinf(d_right)):
                break
        rc.stop_robot()

testMove = ExamControl()
testMove.main()