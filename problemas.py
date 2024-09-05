import math
#Datos del problema
NO = 1000 #vulnerabilidad Inicial
r = 0.03 #Tasa de reduccion
t = 8 #Tiempo en horas

#solucion final
N_t = NO * math.exp(-r * t)

print(f"Las vulnerabilidades restantes despues de {t} horas"
      f" son: {N_t:.Of}")