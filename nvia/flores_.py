import tkinter as tk
import pygame
import math

# Configuración de la ventana principal
root = tk.Tk()
root.title("Flores Amarillas para Paula")
root.geometry("600x600")
root.configure(bg='#fffbe3')

# Inicializar pygame para reproducir el audio
pygame.mixer.init()
audio_path = r'C:\Users\USER\Downloads\Music\flores amarillas.mp3'  # Ruta directa al archivo
pygame.mixer.music.load(audio_path)

# Dibujar las flores con un efecto 3D y agregar los tallos
def dibujar_flores(canvas):
    # Dibujar 5 flores alrededor del centro
    for j in range(5):
        angle_offset = (2 * math.pi / 5) * j  # Dividir el círculo en 5 partes para colocar las flores
        x_centro = 300 + 100 * math.cos(angle_offset)  # Coordenada x del centro de la flor
        y_centro = 300 + 100 * math.sin(angle_offset)  # Coordenada y del centro de la flor
        
        # Dibujar el tallo
        canvas.create_line(x_centro, y_centro, x_centro, y_centro + 100, fill='#3e8e41', width=5)  # Tallo verde
        
        # Dibujar los pétalos con un efecto de profundidad
        for i in range(10): 
            angle = (36 * i) * math.pi / 180  
            x = x_centro + 50 * math.cos(angle)
            y = y_centro + 50 * math.sin(angle)
            # Sombras del pétalo para un efecto 3D
            canvas.create_oval(x - 22, y - 22, x + 18, y + 18, fill='#d4a017', outline='#b8860b')  # Sombra
            canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='#f5c71a', outline='#e6b800')  # Pétalo amarillo

        # Centro de la flor con un toque 3D (luz y sombra)
        canvas.create_oval(x_centro - 33, y_centro - 33, x_centro + 27, y_centro + 27, fill='#c68600', outline='#b5651d')  # Sombra del centro
        canvas.create_oval(x_centro - 30, y_centro - 30, x_centro + 30, y_centro + 30, fill='#ffd700', outline='#e6ac00')  # Centro dorado

# Lienzo para dibujar las flores
canvas = tk.Canvas(root, width=600, height=600, bg='#fffbe3')
canvas.pack()

# Dibujar las flores
dibujar_flores(canvas)

# Animación de texto giratorio y luego estabilizado
def animar_texto():
    texto_id = canvas.create_text(300, 300, text="Flores amarillas para la mejor novia, Mi PAU, TE AMO :3",
                                  font=("Helvetica", 16, "bold"), fill="#f50057", anchor="center")
    
    def rotar_texto(angle=0):
        canvas.delete(texto_id)
        new_angle = angle + 5 
        # Volver a crear el texto con el ángulo rotado
        x = 300 + 5 * math.cos(new_angle * math.pi / 180)
        y = 300 + 5 * math.sin(new_angle * math.pi / 180)
        texto_rotado = canvas.create_text(300, 100, text="Flores amarillas para la mejor novia, Mi PAU, TE AMO :3",
                                          font=("Helvetica", 16, "bold"), fill="#f50057", anchor="center")
        
        if new_angle < 360:  
            root.after(50, rotar_texto, new_angle)
        else:
            # Detener el giro y estabilizar el texto en el centro, un poco más arriba de las flores
            canvas.coords(texto_rotado, 300, 100)  
    
    rotar_texto()

# Función para reproducir el audio y comenzar la animación
def reproducir_audio():
    pygame.mixer.music.play()
    animar_texto()

# Botón para reproducir el audio
boton_reproducir = tk.Button(root, text="Reproducir Audio", command=reproducir_audio, bg='#f5c71a', fg='#ffffff', font=('Helvetica', 14), relief='flat')
boton_reproducir.pack(pady=20)
# Iniciar la interfaz gráfica
root.mainloop()