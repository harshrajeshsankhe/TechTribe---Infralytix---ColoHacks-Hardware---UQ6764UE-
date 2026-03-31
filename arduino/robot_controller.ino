#include <Servo.h>

// ─── Pin Definitions ─────────────────────────────
#define TRIG_PIN 9
#define ECHO_PIN 10
#define GAS_PIN A0
#define TEMP_PIN A1

#define ENA 5
#define IN1 6
#define IN2 7
#define ENB 11
#define IN3 12
#define IN4 13

#define SERVO_PIN 3

Servo rescueServo;

// ─── Setup ───────────────────────────────────────
void setup() {
  Serial.begin(9600);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(GAS_PIN, INPUT);
  pinMode(TEMP_PIN, INPUT);

  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  rescueServo.attach(SERVO_PIN);
  rescueServo.write(0);
}

// ─── Functions ───────────────────────────────────

// Ultrasonic distance
float getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance = duration * 0.034 / 2;
  return distance;
}

// Temperature (LM35 basic)
float getTemperature() {
  int val = analogRead(TEMP_PIN);
  float voltage = val * (5.0 / 1023.0);
  float temp = voltage * 100;
  return temp;
}

// Gas level
int getGasLevel() {
  return analogRead(GAS_PIN);
}

// Motor controls
void moveForward() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 150);
  analogWrite(ENB, 150);
}

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

// Rescue arm
void rescueAction() {
  rescueServo.write(90);
  delay(1000);
  rescueServo.write(0);
}

// ─── Loop ────────────────────────────────────────
void loop() {
  float distance = getDistance();
  float temp = getTemperature();
  int gas = getGasLevel();

  // Send data to Python (Serial)
  Serial.print(distance);
  Serial.print(",");
  Serial.print(temp);
  Serial.print(",");
  Serial.println(gas);

  // Emergency condition
  if (gas > 400) {
    stopMotors();
    Serial.println("EMERGENCY_GAS");
    delay(1000);
    return;
  }

  // Obstacle avoidance
  if (distance < 20) {
    stopMotors();
    delay(500);
  } else {
    moveForward();
  }

  // Victim detection
  if (temp > 35 && temp < 40) {
    stopMotors();
    Serial.println("VICTIM_DETECTED");
    rescueAction();
  }

  delay(500);
}
