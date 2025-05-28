#include <wiringPi.h>
#include "ultrasonic.h"

void ultrasonicSetup(int trig, int echo) {
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
    digitalWrite(trig, LOW);
    delay(30);
}

double getDistance(int trig, int echo) {
    digitalWrite(trig, LOW);
    delayMicroseconds(2);
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);

    while (digitalRead(echo) == LOW);
    int start = micros();
    while (digitalRead(echo) == HIGH);
    int end = micros();

    return (end - start) * 0.017;
}