# Arte ASCII elejido, (unos gatos jejeje).
gato_1 = r"""
 |\---/|
 | o_o |
  \_^_/
"""

gato_2 = r"""
  /\_/\  
 ( o.o ) 
  > ^ <
"""

# Mostrar el arte del mismo.
print(gato_1)
print("Este es tu gato virtual. ¿Qué quieres que haga?")
print("Opciones: 'dormir', 'comer', 'jugar', 'salir'")

while True:
    # Leer la acción que se ingrese previamente.
    accion = input("¿Qué debe hacer tu gato?: ").lower()

    if accion == "dormir":
        print(f"{gato_2}\nTu gato está durmiendo... zzz")
    elif accion == "comer":
        print(f"{gato_1}\nTu gato está comiendo. ¡Ñam ñam!")
    elif accion == "jugar":
        print(f"{gato_2}\nTu gato está jugando y saltando por todos lados!")
    elif accion == "salir":
        print("¡Adiós! El gato se ha ido con otro dueño :`).")
        break
    else:
        print("Esa opción no es válida. Intenta con 'dormir', 'comer', 'jugar' o 'salir'.")