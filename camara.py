
'''import cv2
imagen = cv2.imread('C:\\Users\\Equipo05_CC\\Downloads\\OIP.jfif')
cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import cv2
imagen_color = cv2.imread('C:\\Users\\Equipo05_CC\\Downloads\\OIP.jfif')
cv2.imshow('imagen', imagen_color)
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('imagen_gris: ', imagen_gris)
cv2.imshow('imagen a Escala de Grises: ', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


'''Porbar cada una de las tonalidades que se le permita alterar la imagen'''

'''1.-COLOR_BGR2RGB'''
'''import cv2
imagen_color = cv2.imread('C:\\Users\\Equipo05_CC\\Downloads\\OIP.jfif')
cv2.imshow('imagen', imagen_color)
imagen_azul = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)

cv2.imshow('imagen_azul: ', imagen_azul)
cv2.imshow('imagen a Escala de Azules: ', imagen_azul)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''cv2 - Podemos hacer el uso de la camara'''
'''import cv2
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
cv2.destroyAllWindows()'''

'''import cv2
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
        nombre_foto =f"foto_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jfif"
        cv2.imwrite(nombre_foto, frame)
        print(f"Foto Guardada como: {nombre_foto}")
captura.release()
cv2.destroyAllWindows()'''