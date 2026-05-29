#include <Servo.h>
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

// Servo pins
const int servo1 = 2;
const int servo2 = 3;
const int servo3 = 5;
const int servo4 = 6;
const int servo5 = 9;

// Servo objects
Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;

// SoftwareSerial for DFPlayer
SoftwareSerial mySoftwareSerial(10, 11);  // RX, TX
DFRobotDFPlayerMini myDFPlayer;

// PIR sensor pin
#define SENSORPIN 7

// Timers
unsigned long previousMillis = 0;
const long pauseTime = 2000;     // 2 seconds waiting time between steps
bool isPlaying = false;          // Audio playback status
bool pirEnabled = true;          // PIR sensor status

void setup() {
  mySoftwareSerial.begin(9600);
  Serial.begin(115200);
  pinMode(SENSORPIN, INPUT);

  // Initialize servo motors
  myservo1.attach(servo1);
  myservo2.attach(servo2);
  myservo3.attach(servo3);
  myservo4.attach(servo4);
  myservo5.attach(servo5);

  // Servo start positions
  myservo1.write(75);
  myservo2.write(87);
  myservo3.write(50); // Eyelids closed
  myservo4.write(85);
  myservo5.write(85);
  delay(1000);

  Serial.println(F("Initializing DFPlayer..."));

  // Initialize MP3 module
  if (!myDFPlayer.begin(mySoftwareSerial)) {
    Serial.println(F("Unable to begin:"));
    while (true);
  }
  Serial.println(F("DFPlayer Mini online."));
  myDFPlayer.volume(30);  // Volume level (0 - 30)
}

void openEyes() {
  myservo3.write(80);  // Open the eyelids
  delay(1000);    // Wait 1 second
}

void playSound() {
  Serial.println("DFPlayer Working...");
  myDFPlayer.play(1);   // Play a 5-second audio file
  delay(5000);          // Wait for audio duration
}

void moveServos() {
  Serial.println("Moving Servos...");
  // Left and right eye look at the upper left corner
  myservo1.write(65);
  myservo2.write(75);
  myservo5.write(105);
  myservo4.write(65);
  delay(pauseTime);

  // Left and right eye look at the lower right corner
  myservo1.write(85);
  myservo2.write(105);
  myservo5.write(75);
  myservo4.write(105);
  delay(pauseTime);

  // Eyes centered
  myservo1.write(75);
  myservo2.write(87);
  myservo4.write(85);
  myservo5.write(85);
  delay(pauseTime);

  // Eyelids close
  myservo3.write(50);
  delay(pauseTime);
}

void loop() {
  int pirSensor = digitalRead(SENSORPIN);
  
  // If the PIR sensor is active and no action has been taken
  if (pirSensor == HIGH && pirEnabled) {
    pirEnabled = false;  // PIR sensor deactivated
    openEyes();          // Eyes open
    playSound();         // Audio file is played
    moveServos();        // Servo movements are started
    pirEnabled = true;   // PIR sensor reactivated
  }

  delay(50);  // A very short delay, for sensor stability
}
