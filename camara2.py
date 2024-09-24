import cv2
imagen_color = cv2.imread('C:\\Users\\Equipo05_CC\\Downloads\\OIP.jfif')
cv2.imshow('imagen', imagen_color)
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('imagen_gris: ', imagen_gris)
cv2.imshow('imagen a Escala de Grises: ', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()