#ifndef SERVO_H
#define SERVO_H

void servoSetup(int pin);
void sweepServo(int pin);
void setServoAngle(int pin, int angle);

#endif