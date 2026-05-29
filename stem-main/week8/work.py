from cv2 import rectangle
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    thumbnail_size = (80, 100)
    dataset = dot.get_images("week8/Peking Opera faces", thumbnail_size)

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")

    def draw(self):
        # Background color
        dot.background((180, 0, 0))

        # Add dynamic effects for the faces
        num_faces = 20
        for i in range(num_faces):
            new_canvas = dot.get_layer()
            index = np.random.randint(len(self.dataset))
            to_paste = self.dataset[index]

            # Draw rotation path for the faces
            period = 80
            factor = (dot.frame % period) / period
            theta = (factor * (i / num_faces)) * 1.5 * np.pi

            # Calculate the face position 
            radius = 180
            x = int(dot.width // 2.5 + radius * np.cos(theta))
            y = int(dot.height // 2.5 + radius * np.sin(theta))

            # Ensure pasted position doesn't go off the canvas
            coords = (x - self.thumbnail_size[0] // 2, y - self.thumbnail_size[1] // 2)

            # Paste the face image onto canvas
            dot.paste(new_canvas, to_paste, coords)

            # Compute the rotation matrix
            rotate = np.array([
                [np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]
            ])

            # Calculate the rotated image position, ensure visible
            origin = (dot.width // 2, dot.height // 2)
            new_canvas = dot.transform(new_canvas, rotate, origin)

            # Display layer
            dot.draw_layer(new_canvas)

MySketch()