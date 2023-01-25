import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X','V', 'I' ,'D')
fps = int(cap.get(cv2.CAP_PROP_FPS)) #guarda los fps del video

print('El frame rate es',fps)

delay = int((1/fps)*1000)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #ancho
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #alto

print("El ancho es",width, "y el alto es", height)

framesize = (width,height)

out=cv2.VideoWriter('salida.avi', fourcc, int(fps), framesize)

while(True):
    ret, frame = cap.read()
    if ret is True:
    
        out.write(frame)
        cv2.imshow('Vetana', frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
out.release()
cv2.destroyAllWindows()
