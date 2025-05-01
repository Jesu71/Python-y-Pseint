# Producto como tal
class Pizza:
    def __init__(self):
        self.tamano = None
        self.new_method()

    def new_method(self):
        self.ingredientes = []
    def __str__(self):
        return f"Pizza de tamaño {self.tamano} con ingredientes: {', '.join(self.ingredientes)}"

# Interfaz Builder.
class PizzaBuilder:
    def set_tamano(self, tamano):
        pass 
    
    def add_queso(self):
        pass
    
    def add_pepperoni(self):
        pass
    
    def add_champinones(self):
        pass
    
    def build(self):
        pass

# Builder concreto.
class PizzaConcreteBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def set_tamano(self, tamano):
        self.pizza.tamano = tamano
        return self  # Para permitir la union de los metodos.
    
    def add_queso(self):
        self.pizza.ingredientes.append("queso")
        return self
    
    def add_pepperoni(self):
        self.pizza.ingredientes.append("pepperoni")
        return self
    
    def add_champinones(self):
        self.pizza.ingredientes.append("champiñones")
        return self
    
    def build(self):
        return self.pizza

# tipo de producto usando los builder (tipo de pizza)
class Pizzeria:
    def __init__(self, builder):
        self.builder = builder

    def construir_pizza_personalizada(self, tamano, ingredientes):
        self.builder.set_tamano(tamano)
        
        for ingrediente in ingredientes:
            if ingrediente == "queso":
                self.builder.add_queso()
            elif ingrediente == "pepperoni":
                self.builder.add_pepperoni()
            elif ingrediente == "champiñones":
                self.builder.add_champinones()
        
        return self.builder.build()

# Programa
def main():
    builder = PizzaConcreteBuilder()
    pizzeria = Pizzeria(builder)
    
    tamano = "grande"
    ingredientes = ["queso", "pepperoni", "champiñones"]
    
    pizza_personalizada = pizzeria.construir_pizza_personalizada(tamano, ingredientes)
    
    print(pizza_personalizada)

if __name__ == "__main__":
    main()
