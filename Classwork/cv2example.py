import cv2  


image = cv2.imread("C:\\Shreyas\\CodingalProjects\\Ai\\Classwork\\example.jpg")

resized_image = cv2.resize(image, (800, 500))

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

cv2.imshow('Loaded Image', resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"Image Dimensions: {resized_image.shape}") 
