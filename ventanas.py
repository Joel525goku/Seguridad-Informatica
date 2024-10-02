import tkinter as tk
from tkinter import Toplevel


# Definición de las clases como ejemplo
class Tienda:
    @staticmethod
    def mostrar_info():
        return "Información de la Tienda."


class Horas:
    @staticmethod
    def mostrar_info():
        return "Información de Horas."


class Operaciones:
    @staticmethod
    def mostrar_info():
        return "Información de Operaciones."


class Camara:
    @staticmethod
    def mostrar_info():
        return "Información de la Cámara."


class Problema4:
    @staticmethod
    def mostrar_info():
        return "Información del Problema 4."


def mostrar_clase(clase):
    ventana_clase = Toplevel(ventana)
    ventana_clase.title(clase.__name__)

    info = clase.mostrar_info()
    etiqueta_info = tk.Label(ventana_clase, text=info)
    etiqueta_info.pack(pady=10)

    boton_cerrar = tk.Button(ventana_clase, text="Cerrar", command=ventana_clase.destroy)
    boton_cerrar.pack(pady=5)


def main():
    global ventana
    ventana = tk.Tk()
    ventana.title("Ventana Principal")

    # Crear botones para cada clase
    boton_tienda = tk.Button(ventana, text="Tienda", command=lambda: mostrar_clase(Tienda))
    boton_tienda.pack(pady=5)

    boton_horas = tk.Button(ventana, text="Horas", command=lambda: mostrar_clase(Horas))
    boton_horas.pack(pady=5)

    boton_operaciones = tk.Button(ventana, text="Operaciones", command=lambda: mostrar_clase(Operaciones))
    boton_operaciones.pack(pady=5)

    boton_camara = tk.Button(ventana, text="Cámara", command=lambda: mostrar_clase(Camara))
    boton_camara.pack(pady=5)

    boton_problema4 = tk.Button(ventana, text="Problema 4", command=lambda: mostrar_clase(Problema4))
    boton_problema4.pack(pady=5)

    ventana.mainloop()


if __name__ == "__main__":
    main()
