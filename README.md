# TechTribe---Infralytix---ColoHacks-Hardware---UQ6764UE-

# Earthquake Rescue Robot (Low-Cost Autonomous System)

## Overview
The Earthquake Rescue Robot is a modular, low-cost robotic system designed to assist in search and rescue operations during disasters like earthquakes.

It combines Arduino-based hardware with Python-based intelligence to detect victims, avoid obstacles, monitor gas hazards, and perform rescue actions.

> Designed within a budget of ₹10,000 – ₹15,000 for practical implementation.

---

## Key Features
- Victim Detection (Temperature + Sound)
- Obstacle Avoidance (Ultrasonic Sensor)
- Gas Hazard Detection (MQ Sensor)
- Autonomous Navigation
- Rescue Arm Mechanism
- Arduino ↔ Python Communication

---

## System Architecture
Sensors (Ultrasonic, Gas, Temp)
↓
Arduino Controller
↓ Serial Communication
Python Processing System
↓
Decision Making
↓
Motor Control + Rescue Action


---

## Tech Stack

### Software
- Python 3
- OOP (Modular Architecture)
- PySerial

### Hardware
- Arduino UNO
- L298N Motor Driver
- Ultrasonic Sensor (HC-SR04)
- Gas Sensor (MQ-2 / MQ-7)
- Temperature Sensor (LM35 / MLX90614)
- Servo Motor
- DC Motors + Chassis

---

## Budget

| Component | Cost (₹) |
|----------|--------|
| Arduino UNO | 500 |
| Ultrasonic Sensor | 100 |
| Gas Sensor | 200 |
| Temperature Sensor | 100–800 |
| Motor Driver | 250 |
| Motors + Wheels | 2000 |
| Servo Motor | 200 |
| Battery | 1000 |
| Chassis | 1500 |
| Misc | 1000 |

**Total: ₹6,000 – ₹12,000**

---

## Project Structure
earthquake-rescue-robot/
│
├── src/
│ ├── controller/
│ ├── sensors/
│ ├── detection/
│ ├── navigation/
│ ├── hardware/
│ ├── planning/
│ ├── comms/
│ └── models/
│
├── arduino/
│ └── robot_controller.ino
│
├── README.md

---

## Hardware Connections

### Ultrasonic Sensor
- TRIG → Pin 9
- ECHO → Pin 10

### Gas Sensor
- A0 → A0

### Temperature Sensor
- OUT → A1

### Motor Driver (L298N)
- ENA → 5
- IN1 → 6
- IN2 → 7
- ENB → 11
- IN3 → 12
- IN4 → 13

### Servo Motor
- Signal → Pin 3

---

## Working Flow
1. Sensors collect data
2. Arduino processes and sends via Serial
3. Python analyzes data
4. Robot takes action:
   - Move
   - Stop
   - Rescue
   - Emergency shutdown

---

## Safety Features
- Gas detection stops robot
- Obstacle detection prevents collision
- Controlled rescue arm movement

---

## Future Improvements
- Camera + OpenCV human detection
- SLAM navigation
- Mobile app control
- Live dashboard
- AI-based decision system

---

## Use Cases
- Disaster rescue operations
- Robotics competitions
- Engineering final year project

---

## Author
Harsh Sankhe
Sneha Kaidan

---

## Support
If you like this project:
- Star the repo
- Fork it
- Build your own version

---

## License
MIT License

