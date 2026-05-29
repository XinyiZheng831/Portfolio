# Week 8

### Labs

We continued developing the interaction system for the angel scene. One key addition was refining the blowing gesture by adding a velocity threshold—only when the user's mouth movement exceeded a certain rate would the bubble respond with a visible bounce. This avoided unnecessary triggering and made the experience feel more controlled and intuitive. We also introduced noise-based deformation to the SOP structure to simulate subtle distortions of the soap bubble when the hand lingers or changes direction mid-air.

![SprintVideo-ezgif com-speed](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/21ef0a4c-9636-4ad0-8539-34825d000c55)


![sprint2_angel](https://git.arts.ac.uk/24005614/Responsive-Environments-Blog-2024/assets/1159/a07b6630-22d0-4ef7-bf40-b7c7b05af884)


---

### Reading & Reflections

This week, we studied interactive installations involving fluid simulation and soft body physics. Inspired by artists who created digital fabric and bubble forms, we reflected on how softness in digital visuals can evoke emotion. This encouraged us to fine-tune the response curves in our system to make the visuals feel less mechanical and more "alive."

---

### Peer Support

We encountered inconsistencies between different laptop camera inputs—some had better color sensitivity or faster frame rates. Together, we tested our patch on different machines and adjusted MediaPipe’s detection confidence and smoothing parameters. This collaborative debugging improved cross-device stability. Additionally, one teammate suggested visually debugging the data stream using a custom null CHOP monitor, which helped isolate a lag issue in the network.

---

### Project Development

The bubble mesh was fully integrated with face and hand tracking. We created two states—"idle bubble" and "active interaction"—with smooth transitions based on user input intensity. A layered TOP composite was added to simulate light reflection on the bubble surface, enhancing realism. This made the experience visually richer and more immersive.
