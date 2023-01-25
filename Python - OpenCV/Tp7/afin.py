import cv2 as cv
import numpy as np
import time

def warp(image, origin, final):
    (h, w) = image.shape[:2]    #ancho y alto de la imagen
    m_trans = cv.getAffineTransform(origin, final) #devuelve una transformación afín a partir de tres pares de coordenadas utilizando una matriz de 2x3.
    w= cv.warpAffine(image, m_trans, (w, h), borderValue=(255, 255, 255)) #transforma una imagen usando una matriz basada en los parámetros dados 
    return w