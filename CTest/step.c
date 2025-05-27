#include <stdio.h>
#include <wiringPi.h>

void main(void)
{
	wiringPiSetup();
	pinMode(7, OUTPUT);
	digitalWrite(7, 1);
}
