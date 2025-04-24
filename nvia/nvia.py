import tkinter as tk
from tkinter import messagebox

def preguntar_paula():
    ventana = tk.Tk()
    ventana.title("Declaración de amor")
    ventana.geometry("400x200")
    ventana.config(bg="#ffcccb")  # Fondo rosa claro

    etiqueta = tk.Label(ventana, text="¿Quieres ser mi novia, Paula?", font=("Arial", 14), bg="#ffcccb")
    etiqueta.pack(pady=20)

    def respuesta_si():
        messagebox.showinfo("Felicidades", "¡Ahora eres la novia de este servidor FELICIDADES!")
        ventana.destroy()

    def respuesta_no():
        messagebox.showinfo("Lo siento", "No puedes decir que no JAJAJA, sigue intentando, venga dale sii!!.")
        ventana.destroy()

    boton_si = tk.Button(ventana, text="Sí", command=respuesta_si, bg="#90ee90")  # Verde claro
    boton_si.pack(side=tk.LEFT, padx=20)

    boton_no = tk.Button(ventana, text="No", command=respuesta_no, bg="#ff6666")  # Rojo claro
    boton_no.pack(side=tk.RIGHT, padx=20)

    ventana.mainloop()
preguntar_paula()