#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>

#define SERVO_PIN 29  
#define PWM_RANGE 200 


int angleToDuty(int angle) {
    return (5 * (180 - angle) + 25 * angle) / 180;
}

int main(void) {
    
    if (wiringPiSetup() == -1) {
        fprintf(stderr, "wiringPi setup failed\n");
        return 1;
    }

    
    if (softPwmCreate(SERVO_PIN, 0, PWM_RANGE) != 0) {
        fprintf(stderr, "softPwmCreate failed\n");
        return 1;
    }

    
    while (1) {
       
        for (int ang = 0; ang <= 180; ang += 5) {
            int duty = angleToDuty(ang);
            softPwmWrite(SERVO_PIN, duty);
            delay(20);  
        }
      
        for (int ang = 180; ang >= 0; ang -= 5) {
            int duty = angleToDuty(ang);
            softPwmWrite(SERVO_PIN, duty);
            delay(20);
        }
    }

    return 0;
}

