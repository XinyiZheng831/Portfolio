# Week 6

### Labs

During the first week, the goal was to get the initial setup working with MediaPipe inside TouchDesigner. The first version of the system focused on basic human body detection using the camera feed, successfully extracting landmark data like hands, head, and torso positions.

Several experiments were conducted to test whether MediaPipe’s skeleton output could be used to trigger real-time visual responses. The system was modularized early on, dividing components for easier future expansion — such as splitting video input, skeleton tracking, and visual processing pipelines into separate networks.

---

### Reading & Reflections

Reading:

Dunne & Raby’s idea of design as a “methodological playground” really stuck with me. It reframes design not as problem-solving, but as thought-experiment-making. That hit close to home—I tend to approach projects too pragmatically, always trying to “make it work,” and forgetting that speculative detours can be just as valuable. Vaughan-Lee’s Letter from the Editor was a soft but sharp reminder: we’re so used to mastering nature, but maybe listening is also a form of making. It made me wonder: what would it mean to design not for control, but for coexistence?

Working:

The week helped us better understand how MediaPipe integrates with TouchDesigner, and how much preprocessing is needed to clean and use its output data. It also became clear that achieving smooth interaction would require extra interpolation or filtering of the raw landmark data.

---

### Peer Support

A few technical issues were encountered while importing Python-based MediaPipe scripts into TouchDesigner. Through peer discussion, we figured out how to isolate the Python environment properly and ensure compatibility with real-time execution inside TouchDesigner. We also shared insights on how others were organizing their OP networks to remain readable.

---

### Project Development

The basic tracking foundation was laid this week. We also began initial brainstorming for two contrasting scenes — one representing a soft, dreamy "angel" theme, and another with more intense, dark-toned "demon" energy. The direction was to make both environments switchable and reactive to the user’s body.

