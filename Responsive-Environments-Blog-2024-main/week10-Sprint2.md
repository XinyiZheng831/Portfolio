

**Project Title：Angel & Demon: Interactive Visual Experience -** 
---

## Overview & Project Description

This project aims to create an interactive visual art installation using TouchDesigner and MediaPipe hand gesture recognition technology. Users can directly influence two contrasting visual themes—“Angel” and “Demon”—through hand gestures captured by a camera.
The “Angel” scene uses transparent bubble particles to create a light and dreamy atmosphere, while the “Demon” scene features purple-pink flame effects delivering an intense and mysterious visual impact. The project highlights the integration of interaction and visual expression to provide users with an immersive and intuitive experience.

---
## Supplies & Materials

MediaPipe hand gesture recognition library
HD camera for gesture capture
Photoshop for asset editing
Flame texture sequences
Interactive audio materials

### Components Used:  

TouchDesigner particle system (Particle SOP, Noise CHOP, Feedback TOP, etc.)
Python scripts for MediaPipe gesture data processing and integration
Basic nodes: Transform, Composite, Level
MediaPipe hand tracking module

### Images:  

![sprint2](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/24e1e9cc-43da-4cf5-8af8-de7dafc3e497)

---

## Process

Angel Scene Development Process：

1 Import bubble assets and construct a particle system
2 Use Particle SOP with Noise CHOP to generate natural drifting motion for bubbles
3 Apply Feedback TOP to create motion trails, enhancing the sense of fluidity
4 Adjust global transparency with Level TOP to build a light and ethereal visual style
5 Configure camera input and apply soft color filters to the background
6 Set bubble lifespan parameters for natural appearing and disappearing effects


Demon Scene Development Process：

1 Import flame texture sequences and build a layered flame composition
2 Adjust flame position and transparency with Transform and Composite nodes to fit head and hands
3 Apply custom shaders to generate the purple-pink flame color and flickering effect
4 Use Trail and Blur effects to enhance flow and glow of the flames
5 Bind flame effects to hand tracking data for real-time motion sync
6 Use Render TOP to output the scene and composite it with the user’s camera feed


Scene Switching Mechanism Implementation:

1 Use Python scripts to receive hand gesture data from MediaPipe
2 Define logic: trigger switch when “both hands are clenched into fists”
3 Use Switch TOP to control which scene is currently displayed (Angel or Demon)
4 Add fade-in/out transitions to improve visual smoothness
5 Set the default state as “Angel scene” and ensure stable switching without bouncing

---

## Video Demonstration

The video demonstrates users controlling bubble bursting and flame intensity through real-time hand gestures captured by a camera. Scene switching is smooth, with timely and accurate feedback.

You can see the videos from
https://youtu.be/IABall0GbIg

---

## Final Images

Background:

![Frame 10](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/781493bc-ead1-4f2d-89a0-69d127ec4909)

Shift:

![2025-06-2004 49 522-ezgif com-video-to-gif-converter](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/9afa8de2-d463-415c-bb3b-16b1a8526c3f)


Effects:

![sprint2_devil](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/6c36342a-da31-485a-ac4c-a9f1ae830f5d)

---

## Link to TouchDesigner Files

https://drive.google.com/file/d/1H4cQZEvYJ5mnaNNwoxaB4YEjRucvLLo-/view?usp=sharing

---

## Design Justification 
This project explores the emotional contrast between the “Angel” and “Demon” themes, using natural hand gesture recognition powered by MediaPipe. Our goal was to create a stark contrast in atmosphere while maintaining intuitive user control and system stability. The user can switch scenes simply by hand gestures, with no additional hardware required.

During development, we identified several key issues that need further attention in future iterations:

1 Gesture Response Lag: There is a noticeable delay between MediaPipe input and visual response in TouchDesigner, especially during rapid gesture changes. Optimizing the data bridge or introducing frame synchronization could improve responsiveness.

2 Lack of Transition Animation: Although fade-in/fade-out effects have been added, the scene switch still feels abrupt. Future improvements could include transition animations or dynamic sound cues to enhance narrative flow.

3 Visual Overload in Demon Scene: The heavy use of layered flame effects puts pressure on GPU performance, leading to lower frame rates on certain setups. Future work could simplify shaders or optimize rendering to reduce resource load.

4 Missing Audio Feedback: The interaction currently relies solely on visual changes, which may limit immersion. Incorporating sound design based on gesture triggers could enrich the multisensory experience.

