import cv2
import datetime
captura = cv2.VideoCapture(0)
if not captura.isOpened():
    print("No se pudo acceder a la camara")
    exit()
while True:
    ret, frame = captura.read()
    if not ret:
        print("No se pudo captura la camara")
        break
    altura, anchura = frame.shape[:2]
    cv2.rectangle(frame,
                  (int(anchura * 0.25), int(altura * 0.25)),
                  (int(anchura * 0.75), int(altura * 0.75)),
                  (255, 0, 0), 2)
    cv2.imshow('Video en vivo',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == 32:
        nombre_foto =f"foto_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        cv2.imwrite(nombre_foto, frame)
        print(f"Foto Guardada como: {nombre_foto}")
captura.release()
cv2.destroyAllWindows()