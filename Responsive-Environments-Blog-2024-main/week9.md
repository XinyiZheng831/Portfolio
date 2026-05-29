# Week 9

### Labs

This week, we began the development of the demon-themed scene, aiming for a visually striking contrast with the light and dreamy angel aesthetic. The core idea was to use real-time hand and face tracking data from MediaPipe to control purple flame-like particle effects that respond to user gestures.

We integrated MediaPipe for both hand and face tracking, which gave us stable 3D positional data in real-time. These coordinates were then used to drive an Nvidia Flow Emitter inside a COMP, which simulated volumetric purple smoke or flame around the user’s hands. We tested different emission rates, decay speeds, and noise patterns to make the flames feel energetic yet eerie.

![sprint2_devil](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/766dd22a-f33f-498a-86b9-2e26fdb79b24)


---

### Reading & Reflections

We researched visual coding techniques in interactive VJing and game FX design. A key insight was how gesture-controlled fire or aura effects can be made to feel responsive by adjusting the latency and particle life span. We also reflected on the symbolism of color—purple, in this context, reinforced the dark and surreal mood we aimed for.

---

### Peer Support

One teammate experienced instability in particle rendering when the hand moved too fast, leading to visual lag or bursts. We debugged this by clamping the velocity data and introducing a smoothing CHOP. Additionally, there was an issue with face tracking conflict—when the user’s hand crossed the face, the particles sometimes jumped unexpectedly. Through discussion, we redesigned the particle emitter’s priority logic so that hand data would override face position only when at a certain distance threshold.

---

### Project Development

By the end of the week, we completed a functional prototype of the demon scene. The user’s hands and head emitted dynamic purple flames that followed their real-time movements. In addition to the hand effects, a separate set of flames was placed above the user’s head to enhance the supernatural impression.The particle effects were fully parameterized—allowing us to adjust attributes such as flame size, density, noise turbulence, and lifetime to achieve a variety of visual intensities. These adjustments made the system flexible for experimentation and fine-tuning. All visual elements were composited using a final TOP network and organized for integration alongside the previously completed angel scene, forming the dual-scene structure of the project.Moreover, the transition from the angel scene to the demon scene was triggered by a specific hand gesture—clenching a fist.

