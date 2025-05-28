#include <stdio.h>
#include <wiringPi.h>
#include "ultrasonic.h"
#include "servo.h"
#include "stepmotor.h"

#define TRIG 5    // GPIO. Use `gpio readall` to match.
#define ECHO 6
#define SERVO 26  // ex) BCM 26

int main() {
    if (wiringPiSetupGpio() == -1) {
        fprintf(stderr, "wiringPi setup failed\n");
        return 1;
    }

    ultrasonicSetup(TRIG, ECHO);
    servoSetup(SERVO);
    stepMotorSetup();

    while (1) {
        double dist = getDistance(TRIG, ECHO);
        printf("Distance: %.2f cm\n", dist);

        if (dist <= 20.0) {
            sweepServo(SERVO);       // 왕복 서보
            // delay(200);
            // stepMotorStep();         // 스텝모터 한 바퀴 (8 step)
            for (int i = 0; i < 64; i++) {  // 8스텝 x 64 = 한 바퀴
                stepMotorStep();
            }
        } else {
            setServoAngle(SERVO, 90);  // 중간 유지
            stepMotorStop();           // 스텝모터 정지
        }

        delay(1000);
    }

    return 0;
}