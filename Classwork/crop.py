import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Shreyas\\CodingalProjects\\Ai\\Classwork\\pencil.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap = 'gray')
plt.title("Grayscale image")
plt.show()

croped_image = image[100:300, 200:400]
croped_rgb = cv2.cvtColor(croped_image,cv2.COLOR_BGR2GRAY)
plt.imshow(croped_rgb)
plt.title("Cropped region")
plt.show()

(h, w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M , (w,h))

rotated_rgb = cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8")*50
brighter = cv2.add(image, brightness_matrix)

brighter_rgb = cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter image")
plt.show()