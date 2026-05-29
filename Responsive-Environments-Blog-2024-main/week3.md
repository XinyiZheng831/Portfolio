# Week 3

### Labs

This week, I implemented the core car controls in Unity, using keyboard input for acceleration, steering, and braking. I added obstacles and coin models to the scene and set up collision detection: when the car hits a coin, it disappears and the score increases. Although it’s still keyboard-controlled, I prepared the structure for future SerialPort integration.

---

### Reading & Reflections

Reading:

Macklin and Sharp reframed game design for me—not as skill-building, but as a worldview. I was particularly struck by the idea that play isn’t decoration, it’s the language. It made me question: in my own interactive projects, am I offering room for the player to find their own rhythm? The Arduino-to-Unity video, while technical, started to feel like grammar lessons in this new language. Tools are only meaningful when they support a logic of play—otherwise, they’re just animated shells.

Working:

I reviewed how OnCollisionEnter and OnTriggerEnter work in Unity and set up collision-triggered effects. I ran into issues with the car clipping through objects but resolved it by tweaking Collider parameters and physics materials. I started thinking about how to map touch inputs to car physics in a way that feels smooth and intuitive.


---

### Peer Support

I checked with Xinle Wang about how the sensor data is encoded (e.g., which touch point triggers what), and we prepared the Unity input mapping accordingly. We also discussed control sensitivity and brainstormed whether to add drifting mechanics later.

---

### Project Development

I suggested adding sound effects, like playing a sound when collecting coins or triggering an effect when colliding with obstacles, to make the game feel more immersive. Next step: connect real sensor data to replace keyboard control.

