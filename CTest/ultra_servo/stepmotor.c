#include <wiringPi.h>
#include "stepmotor.h"

#define IN1 17
#define IN2 18
#define IN3 27
#define IN4 22

static int steps[8][4] = {
    {1,0,0,0},
    {1,1,0,0},
    {0,1,0,0},
    {0,1,1,0},
    {0,0,1,0},
    {0,0,1,1},
    {0,0,0,1},
    {1,0,0,1}
};

void stepMotorSetup() {
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
}

void stepMotorStep() {
    for (int i = 0; i < 8; i++) {
        digitalWrite(IN1, steps[i][0]);
        digitalWrite(IN2, steps[i][1]);
        digitalWrite(IN3, steps[i][2]);
        digitalWrite(IN4, steps[i][3]);
        delay(3);  // 회전 속도 조절
    }
}

void stepMotorStop() {
    digitalWrite(IN1, 0);
    digitalWrite(IN2, 0);
    digitalWrite(IN3, 0);
    digitalWrite(IN4, 0);
}