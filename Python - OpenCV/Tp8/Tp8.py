import cv2 as cv
import numpy as np




def homog(image):

    (h, w) = image.shape[:2]    
    pts_bordes = np.float32([[0,0], [w,0], [w,h], [0,h]]) #Se eligen como puntos transformados las esquinas de la imagen original para obtener una imagen rectangular de ese tamaño
    
    pts_img = select_points(fondo_2, 4)
    
    m_pers = cv.getPerspectiveTransform(pts_img, pts_bordes) #devuelve una transformada con los puntos del borde y los elegidos
    homografia = cv.warpPerspective(image, m_pers, (w, h))
    
    return homografia 

puntos = []
def draw_circle (event, x, y, flags, param):
    global puntos, fondo_2
    if event == cv.EVENT_LBUTTONDOWN: # Si se presiona el boton izquierdo
        puntos.append([x, y]) #Creamos una tupla con las coordenadas definidas por el mouse.

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
        # elif k == ord('r'):
        #     cv.destroyAllWindows()
        #     img = backup.copy()
            
        if len(puntos) == points_num: #si se guardan 4 puntos se cierra la seleccion y pasa a la transformacion
            break
    cv.destroyAllWindows()
    
    return np.array(puntos, dtype=np.float32)


img = cv.imread('edificio.jpg', cv.IMREAD_COLOR)
#img = cv.resize(img, (800, 600))
backup = img.copy()
i=0

while (True):
    cv.imshow('Rectificacion de imagenes', img)
    k = cv.waitKey(1) & 0xFF  # Enmascaro con una AND

    if k == ord('h'):
        cv.destroyAllWindows()
        fondo_2 = backup.copy() #se usa backup ya que img va a ir siendo modificada durante el programa
        img = backup.copy()
        img = homog(img)
        cv.imwrite('rectificada.png', img)
        
       
    elif k == ord('r'):
        cv.destroyAllWindows()
        img = backup.copy()


    elif k == ord('q'):
        break
cv.destroyAllWindows()
