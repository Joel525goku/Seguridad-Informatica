'''import tkinter as tk

def main():
    ventana = tk.Tk()
    ventana.title("Primer Creacion de Ventanas")
    ventana.mainloop()

if __name__ == "__main__":
    main()'''

'''import tkinter as tk
def cambiar_texto():
    etiqueta.config(text="¡Texto cambiado")

def main():
    ventana = tk.Tk()
    ventana.title("Manejo de etiquetas y boton")
    global etiqueta
    etiqueta = tk.Label(ventana, text="Texto Original")
    etiqueta.pack()
    boton = tk.Button(ventana, text="Cambiar Text", command=cambiar_texto)
    boton.pack()
    ventana.mainloop()

if __name__ == "__main__":
    main()'''

'''Solicitando nombre en especifico : if __name__ == "__main__":'''
'''Para validar el valor : __'''


import tkinter as tk
from tkinter import Toplevel

def abrir_ventana():
    nombre = entrada.get()
    if nombre:
        ventana_saludo = Toplevel(ventana)
        ventana_saludo.title("¡Saludo!")
        etiqueta_saludo = tk.Label(ventana_saludo, text=F"Hola {nombre}")
        etiqueta_saludo.pack(pady=10)
        boton_cerrar = tk.Button(ventana_saludo, text="Cerrar", command=ventana_saludo.destroy)
        boton_cerrar.pack(pady=5)
def main():
    global ventana, entrada
    ventana = tk.Tk()
    ventana.title("Ventana Principal")
    etiqueta = tk.Label(ventana, text="Ingresa tu nombre: ")
    etiqueta.pack(pady=10)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=10)
    boton = tk.Button(ventana, text="Saludo", command=abrir_ventana)
    boton.pack(pady=10)
    ventana.mainloop()
if __name__ == "__main__":
    main()
    
'''Programa Pincipal que contenga una botonera con almenos 5 act'''