#ifndef ULTRASONIC_H
#define ULTRASONIC_H

void ultrasonicSetup(int trig, int echo);
double getDistance(int trig, int echo);

#endif