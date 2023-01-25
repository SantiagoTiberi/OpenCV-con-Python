import cv2

img = cv2.imread('hoja.png', 0)

print(str(len(img)))

for i in range(len(img)):
    for j in range(len(img[0])):
        if(img[i][j]<245):
            img[i][j]=0

cv2.imwrite('resultado.png', img)

