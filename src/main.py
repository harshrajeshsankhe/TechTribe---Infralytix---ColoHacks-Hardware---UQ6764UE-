from controller.robot_controller import RobotController
import time

robot = RobotController()

for _ in range(20):
    robot.run()
    time.sleep(1)
