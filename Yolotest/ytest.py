import torch
from matplotlib import pyplot as plt
from PIL import Image

img_path = "/home/jk/yolov5/data/images/bus.jpg"

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
results = model(img_path)

results.print()
results.render()
img = Image.fromarray(results.ims[0])
plt.imshow(img)
plt.axis("off")
plt.show()
