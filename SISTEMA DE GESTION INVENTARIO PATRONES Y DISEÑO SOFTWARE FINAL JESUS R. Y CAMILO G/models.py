from abc import ABC, abstractmethod
from datetime import datetime

class Producto(ABC):
    def __init__(self, nombre, descripcion, precio, cantidad, proveedor_id):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.proveedor_id = proveedor_id

    @abstractmethod
    def get_categoria(self):
        pass

class Zapato(Producto):
    def get_categoria(self):
        return "Zapatos"

class Camisa(Producto):
    def get_categoria(self):
        return "Camisas"

class Pantalon(Producto):
    def get_categoria(self):
        return "Pantalones"

class ProductoFactory:
    @staticmethod
    def crear_producto(tipo, nombre, descripcion, precio, cantidad, proveedor_id):
        if tipo.lower() == "zapatos":
            return Zapato(nombre, descripcion, precio, cantidad, proveedor_id)
        elif tipo.lower() == "camisas":
            return Camisa(nombre, descripcion, precio, cantidad, proveedor_id)
        elif tipo.lower() == "pantalones":
            return Pantalon(nombre, descripcion, precio, cantidad, proveedor_id)
        else:
            raise ValueError(f"Tipo de producto no válido: {tipo}")