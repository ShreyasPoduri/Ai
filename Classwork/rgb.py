import cv2 
import numpy as np

def apply_color_filter(image, filter_type):

    filteredImage = image.copy()
    if filter_type == 'red_tint':
        filteredImage[ :, :, 1] = 0
        filteredImage[ :, :, 0] = 0

    elif filter_type == "blue_tint":
        filteredImage[ :, :, 1] = 0
        filteredImage[ :, :, 2] = 0

    elif filter_type == "green_tint":
        filteredImage[ :, :, 0] = 0
        filteredImage[ :, :, 2] = 0

    elif filter_type == "increase_red":
        filteredImage[ :, :, 2] = cv2.add(filteredImage[ :, :, 2], 50)
    elif filter_type == "decrease_blue":
        filteredImage[ :, :, 0] = cv2.subtract(filteredImage[ :, :, 0], 50)

    return filteredImage

image_path = 'C:\\Shreyas\\CodingalProjects\\Ai\\Classwork\\photo.jpg'
image = cv2.imread(image_path)

if image in None:
    print("Error: Image not found")
else:
    filter_type = 'original'

    print("Press the following filters")
    print(" r = Red Tint")
    print(" b = Blue Tint")
    print(" r = Red Tint")
    print(" r = Red Tint")
    print(" r = Red Tint")
