import numpy as np
import random
import imageio.v2 as iio
import tqdm
from PIL import Image

iterations = 1024*32
frame_count = 1024

phi = 1.618033988749894
iphi = 1/phi 

iterations_per_frame = iterations//frame_count

res = 1024

wout = iio.get_writer(f'sq-phi-center-{res}-{iterations}.mp4')

img = np.ndarray((res,res), dtype=np.uint8)

for x in range(res):
    for y in range(res):
        img[x][y] = 0

points = [[0, 0], [res-1, 0], [0, res-1], [res-1, res-1], [res/2, res/2]]

x = points[0][0]
y = points[0][1]

for i in tqdm.tqdm(range(iterations // iterations_per_frame)):
    for e in range(iterations_per_frame):
        point = random.choice(points)
        x = x*(1-iphi) + point[0]*iphi
        y = y*(1-iphi) + point[1]*iphi
        img[int(x)][int(y)] = 255
    wout.append_data(img)

wout.close()
img = Image.fromarray(img)
img.save(f"sq-phi-center-{res}-{iterations}.png")

