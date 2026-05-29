# Sprint 1 Documentation

**Project Title -** Sensor-Controlled Car Racing Game ---created with Xinyi Zheng,Xinle Wang
---

## Overview & Project Description
This project is an exciting racing game that integrates sensor technology with game development. Players use a specially designed sensor-based steering wheel to control a virtual car, handling steering, acceleration, and braking in real-time. The objective is to navigate through the track, avoid obstacles, and collect coins to earn rewards.The game not only tests the player’s precision and reaction speed, but also enhances the driving experience through realistic control mechanics, making the gameplay more immersive and engaging.

---
## Supplies & Materials


### Components Used:  
This project utilizes the MPR121 capacitive touch sensor along with an Arduino Leonardo as the main controller. The sensor enables multiple touch inputs, making it possible to create a simulated steering wheel for controlling the in-game car’s steering, acceleration, and braking. Compared to traditional button or joystick controls, this method is more intuitive and enhances the realism of the driving experience.

Technical Implementation
 • MPR121 Sensor: Supports up to 12 independent touch points, allowing for touch-based control of steering, throttle, and braking.
 • Arduino Leonardo: Processes sensor inputs and transmits data via USB to Unity, converting real-world touch gestures into car movement within the game.
 
### Images:  
![image](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/43928fb6-47f5-4d9c-ae62-26f00427f0d9)

---

## Process
1. Hardware Setup 
 • Connect the MPR121 capacitive touch sensor to the Arduino Leonardo using the I2C interface (SCL, SDA).
 • Use jumper wires to connect the sensor’s touch points and design a simulated steering wheel that allows players to control the car’s direction, acceleration, and braking through touch input.
 • Test the circuit connections to ensure the sensor correctly detects touch inputs.

2. Software Development
 • Arduino Programming: Write code to read data from the MPR121 sensor via I2C and send touch input states to the computer through serial communication.(Xinle Wang)
 • Unity Game Development:(Xinyi Zheng)
 • Create a car model in Unity and implement physics-based controls for acceleration, steering, and collision detection.
 • Use SerialPort communication to receive data from the Arduino and map it to the car’s movement.
 • Implement gameplay mechanics, such as avoiding obstacles, collecting coins, and providing rewards based on scores.

3. Integration and Testing
 • Run the Arduino code and verify that Unity correctly receives touch sensor data.
 • Adjust the car’s sensitivity and handling to ensure smooth player control.
 • Conduct multiple rounds of testing to optimize the gaming experience, such as adjusting coin spawn locations and adding difficulty levels.

4. Final Optimization and Deployment
 • Enhance user experience: Fine-tune touch sensitivity for more intuitive steering control.
 • Add visual and audio feedback: Play sound effects when collecting coins and trigger vibrations upon collision.
 • Encapsulate hardware: Design a 3D-printed casing for the steering wheel to improve usability and ergonomics.
 • Final testing and project completion to ensure a stable and enjoyable gameplay experience.

---

## Video Demonstration


https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/17ba8f0d-1d99-456a-bacd-3674d9405098


https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/048cf517-dd69-49a8-bc02-6dc18efc90c6



---

## Final Images

![WechatIMG2600 1](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/99f3593f-71c9-47a4-aaf2-a77b4722ef44)

---

## Arduino Code
（provided by Xinle Wang)

#include <Wire.h>
#include <Adafruit_MPR121.h>
#include <Keyboard.h>  // Include HID library

Adafruit_MPR121 mpr121 = Adafruit_MPR121();  // Create MPR121 object

void setup() {
  Serial.begin(9600);
  if (!mpr121.begin(0x5A)) {  // Default I2C address is 0x5A
    Serial.println("Failed to initialize MPR121!");
    while (1);  // Stop program if initialization fails
  }
  Serial.println("MPR121 Initialized successfully!");

  Keyboard.begin();  // Initialize keyboard emulation
}

void loop() {
  uint16_t touched = mpr121.touched();  // Get touch status

  for (uint8_t i = 0; i < 12; i++) {
    if (touched & (1 << i)) {  // If the i-th touch point is activated
      Serial.print("Touched: ");
      Serial.println(i);

      if (i == 1) Keyboard.press(' ');  // Space key
      else if (i == 5) Keyboard.press(KEY_LEFT_ARROW);  // Left arrow
      else if (i == 9) Keyboard.press(KEY_RIGHT_ARROW);  // Right arrow
    }
    else {
      if (i == 1) Keyboard.release(' ');
      else if (i == 5) Keyboard.release(KEY_LEFT_ARROW);
      else if (i == 9) Keyboard.release(KEY_RIGHT_ARROW);
    }
  }
  delay(100);
}
## Link to Unity Files

https://drive.google.com/file/d/1Jmge_9YfaEiPtrs6RyB4YYzW8F4E9ayj/view?usp=sharing

---

## Design Justification 

The current game is functional but still has several limitations. First, the gameplay is quite basic and may become repetitive. A classmate suggested adding a chaser to increase tension and realism, which could be explored in future versions. Second, the map is fixed and lacks variety, so adding different levels or environments could improve replayability. Third, the sensor control sometimes feels a bit unresponsive, which might affect the user experience. Lastly, visual and sound effects are quite simple at this stage; enhancing them could make the game more immersive.

---
