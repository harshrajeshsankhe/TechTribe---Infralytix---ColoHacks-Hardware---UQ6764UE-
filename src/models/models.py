from dataclasses import dataclass, field
from enum import Enum
import time

class RobotState(Enum):
    IDLE = "idle"
    SCANNING = "scanning"
    NAVIGATING = "navigating"
    RESCUING = "rescuing"
    RETURNING = "returning"
    EMERGENCY = "emergency"

@dataclass
class Position:
    x: float
    y: float
    theta: float = 0.0

@dataclass
class Victim:
    id: int
    x: float
    y: float
    confidence: float
    heat_sig: float
    is_alive: bool = True
