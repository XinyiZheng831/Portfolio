#include <Servo.h>

const int servo1 = 2;
const int servo2 = 3;
const int servo3 = 5;
const int servo4 = 6;
const int servo5 = 9;

Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;

void setup() {
  myservo1.attach(servo1);
  myservo2.attach(servo2);
  myservo3.attach(servo3);
  myservo4.attach(servo4);
  myservo5.attach(servo5);

  myservo1.write(75);  //right 60 - center 75 - left 90
  myservo2.write(95);  //down 70 - center 95 - up 110
  myservo3.write(50);  //close 50 - open 80
  myservo4.write(80);  //down 110 - center 80 - up 60
  myservo5.write(90);  //right 70 - center 90 - left 110
  delay(2000);
}

void loop() {
  // MOVE 1
  myservo3.write(80);  //close 50 - open 80
  delay(2000);
  myservo1.write(90);   //right 60 - center 75 - left 90
  myservo5.write(110);  //right 70 - center 90 - left 110
  delay(1000);

  // MOVE 2
  myservo1.write(60);  //right 60 - center 75 - left 90
  myservo5.write(70);  //right 70 - center 90 - left 110
  delay(1000);

  // MOVE 3
  myservo1.write(90);   //right 60 - center 75 - left 90
  myservo5.write(110);  //right 70 - center 90 - left 110
  delay(1000);

  // MOVE 4
  myservo1.write(60);  //right 60 - center 75 - left 90
  myservo5.write(70);  //right 70 - center 90 - left 110
  delay(1000);

  // MOVE 5
  myservo1.write(75);  //right 60 - center 75 - left 90
  myservo5.write(90);  //right 70 - center 90 - left 110
  delay(1000);

  // MOVE 6
  myservo2.write(70);  //down 70 - center 95 - up 110
  myservo4.write(110);  //down 110 - center 80 - up 60
  delay(1000);

  // MOVE 7
  myservo2.write(110);  //down 70 - center 95 - up 110
  myservo4.write(60);  //down 110 - center 80 - up 60
  delay(1000);

  // MOVE 8
  myservo2.write(95);  //down 70 - center 95 - up 110
  myservo4.write(80);  //down 110 - center 80 - up 60
  delay(1000);

  // MOVE 9
  myservo3.write(50);  //close 50 - open 80
  delay(2000);
}