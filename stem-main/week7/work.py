import cv2
from cv2 import circle, rectangle
from dorothy import Dorothy
import random

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("Setup")
        self.camera = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed, (dot.width, dot.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)

            for face_x, face_y, face_w, face_h in faces:
                # Colorful circles
                for i in range(3):
                    color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                    circle(camera_feed, 
                           (face_x + face_w // 2, face_y + face_h // 2 + 5), 
                           face_w // (6 - i), color, thickness=2)

                # Add solid rectangles around faces )
                for i in range(1, 6):
                    rectangle(camera_feed, 
                              (face_x - i, face_y - i), 
                              (face_x + face_w + i, face_y + face_h + i), 
                              (255, 255, 0))

                # Add random dots on the face
                for _ in range(5):  # 5 random dots
                    random_offset_x = random.randint(-face_w // 4, face_w // 4)
                    random_offset_y = random.randint(-face_h // 4, face_h // 4)
                    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    circle(camera_feed, 
                           (face_x + face_w // 2 + random_offset_x, face_y + face_h // 2 + random_offset_y), 
                           face_w // 20, random_color, thickness=-1)

            dot.canvas = camera_feed

MySketch()