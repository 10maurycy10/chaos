import numpy as np
import random
import imageio.v2 as iio
import tqdm
from PIL import Image

iterations = 1024*32*8
frame_count = 1024

iterations_per_frame = iterations//frame_count

res = 1024*4

wout = iio.get_writer(f'{res}-{iterations}.mp4')

img = np.ndarray((res,res), dtype=np.uint8)

for x in range(res):
    for y in range(res):
        img[x][y] = 0

points = [[0, 0], [res-1, 0], [res/2, res-1]]

x = points[0][0]
y = points[0][1]

for i in tqdm.tqdm(range(iterations // iterations_per_frame)):
    for e in range(iterations_per_frame):
        point = random.choice(points)
        x = (x + point[0])/2
        y = (y + point[1])/2
        img[int(x)][int(y)] = 255
    wout.append_data(img)

wout.close()
img = Image.fromarray(img)
img.save(f"{res}-{iterations}.png")

