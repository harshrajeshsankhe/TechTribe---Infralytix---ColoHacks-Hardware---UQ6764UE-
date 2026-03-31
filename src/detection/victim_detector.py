from models.models import Victim

class VictimDetector:

    def detect(self, reading, pos):
        victims = []

        if 35 <= reading["temperature"] <= 40:
            confidence = (reading["temperature"] / 40) + (reading["sound"] / 100)

            victims.append(Victim(
                id=int(reading["temperature"] * 100),
                x=pos.x + 1,
                y=pos.y + 1,
                confidence=confidence,
                heat_sig=reading["temperature"]
            ))

        return victims
