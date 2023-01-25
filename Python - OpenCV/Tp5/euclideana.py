import cv2 as cv
import numpy as np


def euclideana(image, angle,tx=0, ty=0):  #imagen , angulo , traslacion en x , translacion y 
    (h, w) = image.shape[:2]  #dimencion de la matriz 
    angle = np.radians(angle)   #Giro antihorario paso a radianes por que la matriz que utlizo recibe angle en radianes

    E = np.float32([[np.cos(angle), np.sin(angle), tx],                # genero la matriz
                    [-np.sin(angle), np.cos(angle), ty],])

    #E = cv2.getRotationMatrix2D(((w/2), (h/2)), angle, 1) #otra forma de generar la matriz euclideana, en este se pasa en angle en grados
    
    euclideana = cv.warpAffine(image, E, (h+200, w+200))  #imagen , la matriz transformacion , tamaño de la imagen de salida 
    return euclideana