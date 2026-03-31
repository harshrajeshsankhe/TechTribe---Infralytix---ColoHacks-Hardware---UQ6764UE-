from sensors.sensor_suite import SensorSuite
from detection.victim_detector import VictimDetector
from navigation.navigator import Navigator
from hardware.motor_controller import MotorController
from planning.mission_planner import MissionPlanner
from comms.comms import Comms
from models.models import RobotState

class RobotController:

    def __init__(self):
        self.sensors = SensorSuite()
        self.detector = VictimDetector()
        self.nav = Navigator()
        self.motor = MotorController()
        self.planner = MissionPlanner()
        self.comms = Comms()

        self.state = RobotState.IDLE

    def run(self):
        reading = self.sensors.read()

        if not self.sensors.is_environment_safe(reading):
            self.state = RobotState.EMERGENCY
            self.motor.stop()
            self.comms.send("Gas danger!")
            return

        victims = self.detector.detect(reading, self.nav.current_pos)

        for v in victims:
            self.planner.add(v)
            self.comms.send("Victim detected")

        target = self.planner.get()

        if target:
            self.nav.move_towards(target)
            self.motor.move()

            if abs(self.nav.current_pos.x - target.x) < 0.5:
                self.motor.rescue()
