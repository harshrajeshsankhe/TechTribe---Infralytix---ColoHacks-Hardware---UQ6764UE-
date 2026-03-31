from models.models import Position
import math

class Navigator:

    def __init__(self):
        self.current_pos = Position(0, 0)

    def move_towards(self, target):
        dx = target.x - self.current_pos.x
        dy = target.y - self.current_pos.y

        dist = math.hypot(dx, dy)

        if dist < 0.1:
            return

        self.current_pos.x += dx / dist * 0.5
        self.current_pos.y += dy / dist * 0.5
