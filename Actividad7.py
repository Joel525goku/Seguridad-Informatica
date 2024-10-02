import tkinter as tk
from tkinter import Toplevel

# Importa tus clases aquí
import Tienda
import Horas
import operaciones
import camara
import problema4


# Suponiendo que cada clase tiene un método `obtener_ventas` que retorna una lista de ventas
def mostrar_ventas(clase):
    ventana_ventas = Toplevel(ventana)
    ventana_ventas.title(f"Ventas de {clase.__name__}")

    # Supongamos que la clase tiene un método para obtener las ventas
    # Ajusta el método según sea necesario
    ventas = clase.obtener_ventas()  # Este método debería estar definido en cada clase

    etiqueta_ventas = tk.Label(ventana_ventas, text=f"Ventas de {clase.__name__}:\n" + "\n".join(ventas))
    etiqueta_ventas.pack(pady=10)

    boton_cerrar = tk.Button(ventana_ventas, text="Cerrar", command=ventana_ventas.destroy)
    boton_cerrar.pack(pady=5)


def main():
    global ventana
    ventana = tk.Tk()
    ventana.title("Ventana Principal")

    # Crea botones para cada clase
    boton_tienda = tk.Button(ventana, text="Tienda", command=lambda: mostrar_ventas(Tienda))
    boton_tienda.pack(pady=5)

    boton_horas = tk.Button(ventana, text="Horas", command=lambda: mostrar_ventas(Horas))
    boton_horas.pack(pady=5)

    boton_operaciones = tk.Button(ventana, text="Operaciones", command=lambda: mostrar_ventas(operaciones))
    boton_operaciones.pack(pady=5)

    boton_camara = tk.Button(ventana, text="Cámara", command=lambda: mostrar_ventas(camara))
    boton_camara.pack(pady=5)

    boton_problema4 = tk.Button(ventana, text="Problema 4", command=lambda: mostrar_ventas(problema4))
    boton_problema4.pack(pady=5)

    ventana.mainloop()


if __name__ == "__main__":
    main()
