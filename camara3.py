import cv2
captura = cv2.VideoCapture(0)
if not captura.isOpened():
    print("No se pudo acceder a la camara")
    exit()
while True:
    ret, frame = captura.read()
    if not ret:
        print("No se pudo capturar el frame")
        break
    cv2.imshow('Video en vivo',frame )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
captura.release()
cv2.destroyAllWindows()