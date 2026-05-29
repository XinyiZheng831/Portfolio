# Week 7 — Working with Video

This week, I explored integrating face detection with dynamic visual effects. My initial aim was to create a program that detects faces via a webcam feed and overlays graphical elements. 

Through iterative experimentation, I added increasingly complex features, moving from static shapes to dynamic, colorful, and randomized visuals. 

## Initial Setup and Camera Feed Capture

In this step, the camera and face detection is set. The command cv2.VideoCapture(0) opens the webcam, and the CascadeClassifier loads a pre-trained model for detecting faces. This is the first step in face-tracking, which lets the program capture video frames and pass them on for further processing.

`def setup(self):`
    `print("Setup")`
    `self.camera = cv2.VideoCapture(0)`
    `self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")`

![6741733010358_ pic](https://git.arts.ac.uk/24005614/stem/assets/1159/1fb8e131-2e61-4bc1-ad0e-ce61739b40dc)

## Converting Camera Feed for Processing

Next, the camera feed is resized to match the canvas size defined in Dorothy. The image is then converted from BGR (the default format used by OpenCV) to RGB (the format Dorothy uses). Afterward, I converted the image to grayscale because face detection works better with grayscale images, which are also faster to process.

`camera_feed = cv2.resize(camera_feed, (dot.width, dot.height))`
`camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)`
`camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)`

## Initial Experiment: Static Clown Mask Overlay

To begin, I wrote a simple face-detection script that draws a static overlay on detected faces. Using OpenCV’s CascadeClassifier for face detection and the Dorothy framework for rendering, I placed a circular shape resembling a clown nose over each detected face.

`for face_x, face_y, face_w, face_h in faces:`
    `# Draw a static clown nose`
    `circle(camera_feed,`
           `(face_x + face_w // 2, face_y + face_h // 2 + 20),`
           `face_w // 6, 255, -1)`

This basic setup taught me how to work with live video and draw simple shapes. However, it lacked visual interest and felt too static.

## Adding Complexity: Dynamic Colors and Shapes

Building on the initial work, I sought to make the visuals more engaging by incorporating dynamic colors and additional shapes. I introduced randomized colors and layered circles of different sizes to create a vibrant, dynamic effect.

`for i in range(3):`
    `color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))`
    `circle(camera_feed,`
           `(face_x + face_w // 2, face_y + face_h // 2 + 5),` 
           `face_w // (6 - i), color, thickness=2)`

This addition allowed me to experiment with layering and color dynamics, giving each frame a unique look. The randomized color palettes significantly increased the visual variety. 

## Adding Rectangles Around Faces

Next, I added gradient rectangles around each detected face. The color of rectangle is bright and vibrant, complementing the shape of the face, and it changes in size depending on the distance of the face from the screen., creating a smooth effect.

`for i in range(1, 6):`
    `rectangle(camera_feed,`
              `(face_x - i, face_y - i),` 
              `(face_x + face_w + i, face_y + face_h + i),` 
              `(255, 255, 0))`

## Adding Random Dots on the Face

In this section, I add five randomly placed dots on the face. Each dot’s position is calculated using random offsets within the face’s width (face_w) and height (face_h). This introduces more randomness and whimsy to the composition. The colors of the dots are also randomly generated, further makinging it playful and unpredictable.

`for _ in range(5):  # 5 random dots`
    `random_offset_x = random.randint(-face_w // 4, face_w // 4)`
    `random_offset_y = random.randint(-face_h // 4, face_h // 4)`
    `random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))`
    `circle(camera_feed,` 
           `(face_x + face_w // 2 + random_offset_x, face_y + face_h // 2 + random_offset_y),` 
           `face_w // 20, random_color, thickness=-1)`

https://git.arts.ac.uk/24005614/stem/assets/1159/1265e3d7-40bb-4e43-ac35-9b6db491edc1


## An Error!

Issue I encountered: Overlapping and Messy Graphics

In an earlier version of the code, when drawing random colored circles and rectangles, the graphics could overlap or become chaotic, especially due to the randomness of their position and color. To prevent and make it cleaner, I carefully adjusted size and opacity of shapes to avoid crowding the face area. I also ensured that these graphics were drawn in a sequence that would reduce visual clutter.

This experience taught me the importance of careful management of graphic elements to ensure both functionality and aesthetics.

## Conclusion and Reflection 

In this project, I gained a deeper understanding of how to integrate real-time video processing and interactive visual effects. By working with face detection and layering dynamic shapes and colors, I improved my ability and learned how to adjust those elements to create visually engaging results. The process taught me the importance of controlling randomness—particularly when generating colors, sizes, and placements so that the visual output remains both unpredictable and harmonious.

Additionally, this project helped me refine the way I structure my code and manage parameters. By extracting parameters like color ranges and position offsets into variables with meaningful names, I was able to better organize my work and easily tweak the effects. Moving forward, I see the potential to extend this project, perhaps incorporating more interactive elements or developing a larger-scale piece by evolving these parameters over time.


