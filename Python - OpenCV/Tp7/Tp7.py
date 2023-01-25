import cv2 as cv
import numpy as np
from afin import warp

puntos = []
def draw_circle (event, x, y, flags, param):
    global puntos, fondo_2
    if event == cv.EVENT_LBUTTONDOWN: # Si se presiona el boton izquierdo
        puntos.append([x, y])
        cv.circle(fondo_2, (x, y), 3, (200, 200, 0), -1)

def select_points(image, points_num): 
    global puntos
    puntos = []
    cv.namedWindow('Seleccionar_Puntos')
    cv.setMouseCallback('Seleccionar_Puntos', draw_circle)

    while True:
        cv.imshow('Seleccionar_Puntos', image)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
        if len(puntos) == points_num:
            break
    cv.destroyAllWindows()
    return np.array(puntos, dtype=np.float32)


img = cv.imread('ubuntu.jpg', cv.IMREAD_COLOR)

fondo = cv.resize(cv.imread('lenna.png'), img.shape[1::-1])  # redimenciono inicio: fin: paso

backup_img = img.copy()  #ubuntu
backup_fondo = fondo.copy() # lenna
(h, w) = img.shape[:2]
#print(h,w)

while (True):
    cv.imshow('Afin', img)
    k = cv.waitKey(1) & 0xFF  # Enmascaro con una AND

    if k == ord('a'):
        cv.destroyAllWindows()
        
        pts_img= np.array(np.float32([[0, 0], [w, 0], [0, h]])) #array con tres puntos esquinas de la imgen ubuntu (izquierda arriba y abajo y derecha arriba)
        
        fondo_2 = fondo.copy()  # imgaen lenna  dimencionada y lo guardo a fondo_2
        pts_fondo = select_points(fondo_2, 3)   #le mando la imagen ojo   ,  deveulve el array con los 3 ptos 
        #print(dst_pts)
        img = backup_img.copy()   # ubuntu
        fondo = backup_fondo.copy()  #lenna        

        img =  warp(img, pts_img, pts_fondo) # Aplico transformada (ubuntu , ptos ubuntu , ptos lenna,)
        #cv2.imshow('X',img) #imagen transformada
        
        img2gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #paso ubuntu a blanco y negro para poder umbralizar        
        #cv.imshow('j',img2gray)
        #Aplico el umbral, donde img2gray es la foto en blanco y negro, los dos parámetros siguientes son los límites de color y la última parte es el tipo de umbral elegido como THRESH_BINARY que separa lo negro del blanco tal como es la imagen
        ret, mask = cv.threshold(img2gray, 200, 255, cv.THRESH_BINARY ) #umbralizacion para separar fondo de la imagen 
        #cv2.imshow('A',mask)  #imagen de ubuntu umbralizada (blaco y negro)
        mask_inv = cv.bitwise_not(mask) #imagen inversa lo que era blanco ahora es engro
        
        fondo_3 = cv.bitwise_and(fondo, fondo, mask=mask)  #2 imagenes lenna y 1 (blanco y negro) ubuntu con la mascara del combinacuon lineal de las imagenes  
        #cv2.imshow('b',fondo_3) # lenna con el ubuntu negro       
        img_3 = cv.bitwise_and(img, img, mask=mask_inv)  #lenna mascara inversa
        #cv2.imshow('A',img_3)  #todo negro y el ubuntu a color 
        
        img = cv.add(fondo_3, img_3) #sumo las 2 imagenes  (hace una combinacion lineal) 
        # img2_fg al ser una toda negra (valor 0) menos el logo se le suma img1_bg que es lenna con el logo en negro, asi se convinan los colores, cambiando de
        #negro al color que se le sume 
        cv.imwrite('T_afin.png', img)

    elif k == ord('q'):
        break

