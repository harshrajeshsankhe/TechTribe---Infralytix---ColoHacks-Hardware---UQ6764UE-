import random

class SensorSuite:
    """Budget-friendly simulated sensors"""

    def read(self):
        return {
            "distance": random.uniform(10, 200),  # ultrasonic cm
            "temperature": random.uniform(25, 40),  # IR sensor
            "gas": random.uniform(0, 100),  # MQ sensor
            "sound": random.uniform(30, 90)
        }

    def is_environment_safe(self, reading):
        return reading["gas"] < 70
