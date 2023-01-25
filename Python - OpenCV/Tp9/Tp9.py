import cv2
import numpy as np
from math import sqrt



factor = 0.37383 #Es la relacion entre la altura real de la puerta y los pixeles para la imagen rectificada h = 200cm = 535 px -->200/535 = 0.37383
                 #Ancho de la puerta 80cm --> 80*0.37383 = 218 px


pts = [[],[]]

def perspectiva(image, pts_original, pts_persp):
    (h, w) = image.shape[:2]
    m_pers = cv2.getPerspectiveTransform(pts_original, pts_persp) #devuelve una transformada con los puntos del borde y los elegidos
    rectif = cv2.warpPerspective(img, m_pers, (w, h), borderMode=cv2.BORDER_CONSTANT)
    return rectif


def select_points (event,x,y,flags,param):
    global drawing, pts, i
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pts[i] = x,y #se crea una tupla con las coordenadas del mouse
        cv2.circle(persp, pts[i], 2,  (20,175,80), 2) 
        i = i+1
        if i == 2: #si ya se seleccionaron los dos puntos ...
            drawing = False
            cv2.line(backup, (pts[0][0],pts[0][1]), (pts[1][0],pts[1][1]), (20,175,80), 1) #se hace una linea entre los puntos seleccionados 
            dist = ". " + str(round((sqrt(((x-pts[0][0])*(factor/100))**2+((y-pts[0][1])*(factor/100))**2)),2)) + " metros" #texto con la medicion
            cv2.putText(backup, dist, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (20,175,80), 2) #texto , ubicacion , fuente , factor de escala color y el ancho 

        elif (drawing is True):
            backup[:] = persp[:] #Actualza las medidas (marca el primer punto en el dibujo backup)	

img = cv2.imread('puerta.jpeg') #Cargo la imagen
img = cv2.resize(img, (600, 800))
cv2.imshow('Original',img)
backup = img.copy()
x1, y1 = 217, 119  #esquina superior izquierda de la puerta sin rectificar
x2, y2 = 487, 79   #esquina superior derecha de la puerta sin rectificar
x3, y3 = 475, 720  #esquina inferior derecha de la puerta sin rectificar
x4, y4 = 264, 673  #esquina inferior izquierda de la puerta sin rectificar

#rectángulo con la misma relación de aspecto que la puerta real, comenzando el rectangulo por la esquina sup izquierda x1 y1
pts_persp = np.array([[x1, y1], [x1+218, y1], [x1+218, y1+535], [x1, y1+535]], dtype=np.float32) #  dst_pts (ptos destinos ) x1+ancho de puerta en pixel; y1+largo de puerta en pixel                          
        
pts_original = np.float32([[x1,  y1], [x2,  y2], [x3, y3], [x4, y4]])     # harcodeo los selected_point, puntos de las esquinas del marco de la imagen original 
        
persp = perspectiva(img, pts_original, pts_persp)  #y los envio a la funcion perspective para rectificar

backup = persp.copy()
backup_2 = persp.copy()
cv2.namedWindow('Medicion de objetos')
cv2.setMouseCallback("Medicion de objetos", select_points)# Si se produce un evento de mouse sobre esa ventana se debe llamar a la función selection

i=0             #inicializo contador de puntos a elegir

while(True):
    cv2.imshow('Medicion de objetos',backup)
    k=cv2.waitKey(1)& 0xFF

    if k == ord('r'):
        i = 0
        backup = backup_2.copy()
        persp = backup_2.copy()
    if k == ord('g'):
        cv2.imwrite('Resultado.png', backup)
    if k == ord('q'):
        break
cv2.destroyAllWindows()
