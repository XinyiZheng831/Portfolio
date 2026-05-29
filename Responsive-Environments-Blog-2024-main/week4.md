# Week 4

### Labs

This week focused on connecting Arduino with Unity via SerialPort. I wrote a script to receive serial data and mapped specific touch points to car controls: touch point 5 for left, point 9 for right, point 1 for acceleration. After testing, the sensor inputs now successfully control the car in-game! I also fine-tuned turning sensitivity and adjusted coin spawn frequency.

---

### Reading & Reflections

Reading:

The “Sound Toys” chapter reframed audio for me—not as a backdrop, but as playable material. A. Dolphin describes sound as a “shapeable” substance, which hit home because I usually treat audio as aesthetic filler, not an actor. David Kanaga’s talk was like psychedelic game philosophy—linking music with matter and lifeforms. A bit out-there, but it made me wonder: can sound be “touched”? Robin Arnott, in contrast, pulled me back down to earth: mindful pacing and breathing space can be more immersive than constant sensory overload.

Working:

I learned about handling real-time data in Unity. At first, there were delays and laggy responses, but I solved this by running the SerialPort reading in a separate thread, preventing the main thread from being blocked. This lab deepened my understanding of hardware integration in Unity.


---

### Peer Support

I tested the full workflow with Xinle Wang and confirmed that each touch input correctly triggers the intended action in Unity. We also checked the stability of data transfer and discussed adding filters to prevent false touches.

---

### Project Development

We proposed making a 3D-printed casing to mount the touchpad and Arduino securely, making the steering wheel feel more realistic. We’re also planning to add a lap timer and design more challenging race tracks.
