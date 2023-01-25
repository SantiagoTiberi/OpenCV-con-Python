import cv2 as cv
import numpy as np


def simil(image, angle,tx=0, ty=0, scale=1.0):
    (h, w) = image.shape[:2] #dimencion de la matriz 
    angle = np.radians(angle)   #Giro antihorario pasado a radianes

    S = np.float32([[scale*np.cos(angle),  scale*np.sin(angle), tx],
                    [-scale*np.sin(angle), scale*np.cos(angle), ty],]) #se agrega escala a la matriz euclideana


    simil = cv.warpAffine(image, S, (w+300, h+300)) #imagen , la matriz transformacion , tamaño de la imagen de salida
    return simil
