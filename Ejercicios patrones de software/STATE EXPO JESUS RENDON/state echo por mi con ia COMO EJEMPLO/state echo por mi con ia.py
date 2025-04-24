from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def reproducir(self):
        pass

    @abstractmethod
    def pausar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

class EstadoReproduciendo(Estado):
    def reproducir(self):
        return "Ya está reproduciendo."

    def pausar(self):
        return "Pausando la reproducción."

    def detener(self):
        return "Deteniendo la reproducción."

class EstadoPausado(Estado):
    def reproducir(self):
        return "Reanudando la reproducción."

    def pausar(self):
        return "Ya está en pausa."

    def detener(self):
        return "Deteniendo la reproducción."

class EstadoDetenido(Estado):
    def reproducir(self):
        return "Iniciando la reproducción."

    def pausar(self):
        return "No se puede pausar, está detenido."

    def detener(self):
        return "Ya está detenido."

class ReproductorMusica:
    def __init__(self):
        self.estado_detenido = EstadoDetenido()
        self.estado_reproduciendo = EstadoReproduciendo()
        self.estado_pausado = EstadoPausado()
        self.estado = self.estado_detenido

    def set_estado(self, estado):
        self.estado = estado

    def reproducir(self):
        mensaje = self.estado.reproducir()
        if isinstance(self.estado, EstadoDetenido) or isinstance(self.estado, EstadoPausado):
            self.set_estado(self.estado_reproduciendo)
        return mensaje

    def pausar(self):
        mensaje = self.estado.pausar()
        if isinstance(self.estado, EstadoReproduciendo):
            self.set_estado(self.estado_pausado)
        return mensaje

    def detener(self):
        mensaje = self.estado.detener()
        self.set_estado(self.estado_detenido)
        return mensaje

# Ejemplo de uso
reproductor = ReproductorMusica()

print(reproductor.reproducir())  # Iniciando la reproducción.
print(reproductor.reproducir())  # Ya está reproduciendo.
print(reproductor.pausar())      # Pausando la reproducción.
print(reproductor.detener())     # Deteniendo la reproducción.
print(reproductor.pausar())      # No se puede pausar, está detenido.
print(reproductor.reproducir())  # Iniciando la reproducción.