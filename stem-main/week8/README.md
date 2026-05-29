# Week 8 - Maths for Multimedia

For this week’s project, I aimed to enhance a visual sketch featuring dynamic, rotating Peking Opera face images. Peking Opera is one of China's intangible heritage traditional culture, with masks of extremely rich colors and patterns, which provides me with a constant source of inspiration for this project. Through experimentation and analysis, I designed the visual composition of Peking Opera to achieve a structured and aesthetically appealing effect. 

## Background Setup and Initialization

In this project, I used the Dorothy library to load a dataset of Peking Opera faces and standardized their size with thumbnail_size. By initializing the MySketch class and using dot.start_loop, I established the setup and draw functions for real-time rendering of dynamic visual effects.

`from cv2 import rectangle`
`from dorothy import Dorothy`
`import numpy as np`

`dot = Dorothy()`

`class MySketch:`
`thumbnail_size = (80, 100)`
`dataset = dot.get_images("week8/Peking Opera faces", thumbnail_size)`
`def __init__(self):`
`dot.start_loop(self.setup, self.draw)`
    
`def setup(self):`
`print("setup")`

## Dynamic Layer Drawing

In the draw method, I started by resetting the background color to ensure that each frame is independent. Then, I used a loop to randomly select and paste several face images onto new layers. The random selection ensures variability and maintains the dynamic nature of the animation.

`def draw(self):`
`dot.background((180, 0, 0))`

`num_faces = 20`
`for i in range(num_faces):`
`new_canvas = dot.get_layer()`
`index = np.random.randint(len(self.dataset))`
`to_paste = self.dataset[index]`

## Path Generation Using Trigonometric Functions

To arrange the faces along a circular path, I used trigonometric functions to calculate the dynamic coordinates of each image. The angle theta varies periodically, ensuring that each image is evenly distributed along the path and continuously rotates as frames progress.

`period = 80`
`factor = (dot.frame % period) / period`
`theta = (factor * (i / num_faces)) * 1.5 * np.pi`

`radius = 180`
`x = int(dot.width // 2.5 + radius * np.cos(theta))`
`y = int(dot.height // 2.5 + radius * np.sin(theta))`

## Center Alignment and Pasting

To ensure accurate alignment of the images along the path, I adjusted their coordinates by subtracting half the image dimensions before pasting them onto the canvas. This ensures that each face is centered at its calculated position.

`coords = (x - self.thumbnail_size[0] // 2, y - self.thumbnail_size[1] // 2)`
`dot.paste(new_canvas, to_paste, coords)`

## Rotation and Layer Transformation

I then applied a rotation matrix to each layer using numpy. This allowed the faces to rotate dynamically around their own centers while moving along the circular path, adding depth and complexity to the animation. Finally, I redrew the transformed layers onto the main canvas.

`rotate = np.array([`
`[np.cos(theta), -np.sin(theta)],`
`[np.sin(theta), np.cos(theta)]])`

`origin = (dot.width // 2, dot.height // 2)`
`new_canvas = dot.transform(new_canvas, rotate, origin)`
`dot.draw_layer(new_canvas)`

## Enhance Animation by Slightly Changing Parameters

I experimented with two code in total, achieving two different effects: one where the images rotate around the center and another has a certain degree of offset during rotation.

The initial code focus on rotating around a central origin. However, I noticed that during the rotation at this angle, the photos on the cards are often obscured by the cards in front and behind them, making it difficult to effectively showcase the visual details of the Peking Opera faces.



https://git.arts.ac.uk/24005614/stem/assets/1159/104b1203-e878-4dcc-a2ef-b31e36d9d609



I made some subtle changes. First, I reduce the thumbnail size from (90, 120) to (80, 100), making the visuals more compact. Additionally, I replaced the fixed coordinates at (100, 100) with dynamically calculated positions along a circular path, enhancing the flow of the animation. Moreover, the rotation angle’s cycle was adjusted from 2 * np.pi to 1.5 * np.pi, speeding up the rotation and adding more rhythm. These changes made the visuals more natural and have a more dynamic, richer aesthetic.



https://git.arts.ac.uk/24005614/stem/assets/1159/5ab7a2df-0fe9-401a-aa93-c76b56e21297



## An Error!

This code encountered fewer errors, but it led to situations where, due to unsuitable parameter values, the image content extended beyond the canvas boundaries, which causes missing cards on the left:

<img width="639" alt="截屏2024-12-01 02 49 39" src="https://git.arts.ac.uk/24005614/stem/assets/1159/c3acddf5-896d-4e8f-a0e3-1c3b6d9c703a">


`x = int(dot.width // 2 + radius * np.cos(theta))`
`y = int(dot.height // 2 + radius * np.sin(theta))`

It has been solved when I replaced the `dot.width//2` and `dot.height//2` to `dot.width//2.5` and `dot.height//2.5`


## Conclusion and Reflection

This project deepened my understanding of creating dynamic visual effects through mathematical functions and matrix transformations. By experimenting with rotation angles and circular paths, I learned how to create smooth, visually appealing animations. Additionally, I improved my coding structure, recognizing the value of parameterization for easier adjustments and better flexibility.

For future work, I plan to incorporate user interaction or audio input to make the animation more engaging. This could include syncing visuals with sound or enabling users to influence the animation in real time, adding a new layer of interactivity.
