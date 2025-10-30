import cv2
import os
import sys


img_name = 'example.jpg'
img_path = img_name if os.path.isabs(img_name) else os.path.join(os.path.dirname(__file__), img_name)

if not os.path.exists(img_path):
    print(f"ERROR: file not found: {os.path.abspath(img_path)}")
    sys.exit(1)

image = cv2.imread(img_path)
if image is None:
    print("ERROR: cv2.imread failed (file may be unreadable/corrupted or missing codecs).")
    sys.exit(1)

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 800, 500)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")