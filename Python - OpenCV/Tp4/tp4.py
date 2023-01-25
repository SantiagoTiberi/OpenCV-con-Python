#Usando como base el programa anterior, escribir un programa que permita seleccionar un rectángulo de una imagen, luego
#   g guarda la imagen dentro del rectangulo en el disco,
#   r restaura la imagen original y permite realizar nuevamente la seleccion,
#   q finaliza.

import cv2 as cv
import numpy as np

save = False
ix, iy, ix2, iy2 = 0 ,0, 0, 0
drawing = False

def draw_rect(event, x, y, flags, params):
    global ix, iy, ix2, iy2, drawing, img, backup

    if event == cv.EVENT_LBUTTONDOWN:#indica que el boton izquierdo del mouse se presiono
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:#indica que el puntero del mouse se movio por la ventana
        if drawing is True:
            img = cv.imread(backup)
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2) # dibujo el ractangulo , pto inicial final y en la posicion actual donde se movio el mouse
    elif event == cv.EVENT_LBUTTONUP: #indica que se suelta el boton izquierdo del mouse
        drawing = False
        ix2, iy2 = x, y #inicializo las coordenadas finales con las ultimas coordenadas del mouse
        cv.rectangle(img, (ix, iy), (ix2, iy2), (50, 50, 150), 2) #(50, 50, 150) setean el color del rectangulo al soltar el mouse, 1 es el grosor de las lineas
    

def save_img(ix, iy, ix2, iy2, img):
    print("\n\n----GUARDANDO LA IMAGEN----")
    rx = abs(ix2 - ix) #largo del rectangulo
    ry = abs(iy2 - iy) #alto del rectangulo
    print("rx: ",rx, ", ry: ",ry)
    
    #cut = np.zeros((ry,rx,3), np.uint8) #numpy arrays, creo una matriz de tamaño ry y rx (3D por los colores) para guardar la imagen
    
    print ('xi:',ix, 'xf:',ix2,'yi:',iy,'yf:',iy2)
        
    ix, ix2 = min(ix, ix2), max(ix, ix2)  #coordenada min y max de la variable X
    iy, iy2 = min(iy, iy2), max(iy, iy2)  #lo mismo en la varbiale Y 
    cut = roi[iy:iy2, ix:ix2]
    cv.imwrite('resultado.jpg', cut)
    cv.imshow('recorte', cut)



backup= 'lenna.png' #guarda en backup la imagen para las proximas llamadas
img = cv.imread(backup)
roi=img.copy() #region de la imagen, la uso para que no quede marcado el borde del rectangulo en el recorte
cv.namedWindow('Imagen Original')
cv.setMouseCallback('Imagen Original', draw_rect) #envia a la funcion draw_rect los parametros del mouse en el orden en que se encuentran en la funcion
i=0


while(1):
    cv.imshow('Imagen Original', img)
    k = cv.waitKey(10) & 0xFF
    if k == ord('r'):
        img = cv.imread(backup) #vuelve a leer la imagen original
        if (i==1):
            cv.destroyWindow('recorte')
            i=0

        
    elif k == ord('g'):
        save_img(ix, iy, ix2, iy2, img)
        i=1
    
    elif k == ord('q'):
        break

cv.destroyAllWindows()
