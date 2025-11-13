import cv2
import matplotlib as plt

img = cv2.imread('photo.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

r1,r2 = (20,20,150,150), (img.shape[1]-170, img.shape[0]-170,150,150)

cv2.rectangle(img,r1[:2], r1[0] + r1[2], r1[1] + r1[3], (0,255,255), 2)
cv2.rectangle(img,r2[:2], r2[0] + r2[2], r2[1] + r2[3], (255,0,255), 2)

c1 = (r1[0]+r1[2]//2, r1[1]+ r1[3]//2)
c2 = (r2[0]+r2[2]//2, r2[1]+ r2[3]//2)

cv2.circle(img, c1, 8, (0,255,0), -1)
cv2.circle(img, c2, 8, (0,0,255), -1)
cv2.line(img, c1, c2, (0,255,0), 2)

f = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Center 1', (c1[0]-30 , c1[1]+ 30), f, 0.6, (0,255,0), 2)
cv2.putText(img, 'Center 2', (c2[0]-30 , c2[1]+ 30), f, 0.6, (0,255,0), 2)

h = img.shape[0]
cv2.arrowedLine(img, (img.shape[1]-40, 20), (img.shape[1]-40, h-20), (255,255,0), 2, tipLength=0.05)
cv2.arrowedLine(img, (img.shape[1]-40, h-20), (img.shape[1]-40, 20), (255,255,0), 2, tipLength=0.05)
cv2.putText(img, f'Height: {h}px', (img.shape[1]-200, h//2), f, 0.6, (255,255,0), 2)


plt.figure(figsize=(12,8))
plt.imshow(img)
plt.axis('off')
plt.title("Annotated Image")
plt.show()