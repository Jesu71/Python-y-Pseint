class Requisito:
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion
        self.cumplido = False

    def marcar_como_cumplido(self):
        self.cumplido = True

    def __str__(self):
        estado = "Cumplido" if self.cumplido else "Pendiente"
        return f"[{self.id}] {self.descripcion} - Estado: {estado}"

class GestionRequisitos:
    def __init__(self):
        self.requisitos = []

    def agregar_requisito(self, descripcion):
        id = len(self.requisitos) + 1
        nuevo_requisito = Requisito(id, descripcion)
        self.requisitos.append(nuevo_requisito)
        print(f"Requisito agregado: {nuevo_requisito}")

    def marcar_requisito_como_cumplido(self, id):
        for req in self.requisitos:
            if req.id == id:
                req.marcar_como_cumplido()
                print(f"Requisito {id} marcado como cumplido.")
                return
        print(f"No se encontró el requisito con ID {id}.")

    def eliminar_requisito(self, id):
        self.requisitos = [req for req in self.requisitos if req.id != id]
        print(f"Requisito {id} eliminado.")

    def listar_requisitos(self):
        if not self.requisitos:
            print("No hay requisitos registrados.")
        else:
            for req in self.requisitos:
                print(req)


# Ejemplo de uso de la herramienta de gestión de requisitos
if __name__ == '__main__':
    gestion = GestionRequisitos()

    # Agregar requisitos
    gestion.agregar_requisito("El sistema debe permitir al usuario registrarse.")
    gestion.agregar_requisito("El sistema debe autenticar al usuario con contraseña.")
    gestion.agregar_requisito("El sistema debe permitir el restablecimiento de contraseña.")

    # Listar requisitos
    print("\nLista de requisitos:")
    gestion.listar_requisitos()

    # Marcar un requisito como cumplido
    gestion.marcar_requisito_como_cumplido(2)

    # Listar requisitos después de marcar uno como cumplido
    print("\nLista de requisitos después de marcar uno como cumplido:")
    gestion.listar_requisitos()

    # Eliminar un requisito
    gestion.eliminar_requisito(1)

    # Listar requisitos después de eliminar uno
    print("\nLista de requisitos después de eliminar uno:")
    gestion.listar_requisitos()
