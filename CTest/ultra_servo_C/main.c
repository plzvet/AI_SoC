#include <stdio.h>
#include <wiringPi.h>
#include "ultrasonic.h"
#include "servo.h"

#define TRIG 27
#define ECHO 28
#define SERVO 29

int main() {
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "wiringPi setup failed\n");
        return 1;
    }

    ultrasonicSetup(TRIG, ECHO);
    servoSetup(SERVO);

    while (1) {
        double dist = getDistance(TRIG, ECHO);
        printf("Distance: %.2f cm\n", dist);

        if (dist <= 20.0)
            sweepServo(SERVO);
        else {
            setServoAngle(SERVO, 90);  // idle position
            delay(200);
        }

        delay(300);
    }

    return 0;
}