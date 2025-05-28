#include <wiringPi.h>
#include <softPwm.h>
#include "servo.h"

static int angleToDuty(int angle) {
    return (5 * (180 - angle) + 25 * angle) / 180;
}

void servoSetup(int pin) {
    softPwmCreate(pin, 0, 200);
}

void setServoAngle(int pin, int angle) {
    softPwmWrite(pin, angleToDuty(angle));
}

void sweepServo(int pin) {
    for (int ang = 0; ang <= 180; ang += 5) {
        setServoAngle(pin, ang);
        delay(20);
    }
    for (int ang = 180; ang >= 0; ang -= 5) {
        setServoAngle(pin, ang);
        delay(20);
    }
}