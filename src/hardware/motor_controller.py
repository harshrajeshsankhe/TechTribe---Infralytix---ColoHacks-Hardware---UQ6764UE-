class MotorController:

    def __init__(self):
        self.status = "stopped"

    def move(self):
        self.status = "moving"

    def stop(self):
        self.status = "stopped"

    def rescue(self):
        print("Rescue arm activated")
