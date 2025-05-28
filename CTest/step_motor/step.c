#include <wiringPi.h>
#include <stdio.h>

#define IN1 17
#define IN2 18
#define IN3 27
#define IN4 22

void step(int a, int b, int c, int d) {
    digitalWrite(IN1, a);
    digitalWrite(IN2, b);
    digitalWrite(IN3, c);
    digitalWrite(IN4, d);
}

int main() {
    wiringPiSetupGpio(); // BCM 모드
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);

    int steps[8][4] = {
        {1,0,0,0},
        {1,1,0,0},
        {0,1,0,0},
        {0,1,1,0},
        {0,0,1,0},
        {0,0,1,1},
        {0,0,0,1},
        {1,0,0,1}
    };

    printf("스텝모터 무한 시계방향 회전 시작\n");

    int i;
    while (1) {
        for (i = 0; i < 8; i++) {
            step(steps[i][0], steps[i][1], steps[i][2], steps[i][3]);
            delay(1); // 속도 조절 가능 (숫자 줄이면 빠르게 회전)
        }
    }

    return 0;
}
