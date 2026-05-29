# Week 4
#  Kinect Data Study, Motion Mapping & System Exploration

### Research 

This week I focused on understanding the Kinect sensor more deeply and how bodily motion could be translated into stable and expressive data inside TouchDesigner. I spent time testing different types of body tracking, especially depth silhouettes, joint positions, and basic gesture detection. Rather than jumping directly into emotional design, my main goal this week was to understand the behaviour of motion data itself — how sensitive it is, how noisy it becomes, and how it behaves under different lighting and distances.

At the same time, I began thinking more seriously about how one single body input could later support multiple emotional systems. I looked at several TouchDesigner projects that use modular structures and parallel networks, especially those that allow the same input to drive different visual outcomes. This research directly supported my later idea of running seven emotional systems in parallel.

---

### Development

This week was mainly devoted to system exploration and technical testing rather than designing specific emotions. I built a basic Kinect input pipeline, including depth input, skeleton tracking, smoothing, and velocity extraction. A large part of the week went into simply standing in front of the camera and observing how my movement turned into numerical data and silhouettes on screen. I tested how small gestures, fast motion, and body distance affected stability.

Motion Mapping：
![b21da028df8e90d06f34e18c0a9c246c](https://git.arts.ac.uk/user-attachments/assets/40e427f3-5628-4198-9146-7003ea33c9c8)


I also began to sketch the overall structure of the future system. Instead of building finished effects, I created several empty visual containers as early placeholders for the seven sins. These were not yet emotional systems, but simple visual spaces where I could later insert different behaviours. At this stage, my main concern was whether the system could technically support multiple parallel visual processes without becoming unstable.

TD Network Overview：
![ChatGPT Image 2025年11月25日 21_05_35](https://git.arts.ac.uk/user-attachments/assets/983adda5-184f-4172-bf47-fd5f32d35633)


Another important part of this week was experimenting with basic mapping strategies — linking movement speed to visual intensity, hand position to spatial transformation, and body distance to scale. These early mappings later became the basic logic for the emotional systems, even though at this point they were still purely functional.


---

### Reflection

Week 4 became a crucial transition point between early technical exploration and the actual emotional design of the Seven Sins. Instead of thinking in terms of “visual effects”, I started to think in terms of “behaviour”. This shift later shaped the entire project.

Through repeated testing with the Kinect, I also became very aware of the physical limitations of the sensor — noise, latency, and instability — which later influenced my decisions to simplify gestures and prioritise robustness over complexity. Most importantly, this week gave me confidence that one body input could indeed be transformed into many different visual identities, which directly led to the beginning of my first sin, Pride, in Week 5.

