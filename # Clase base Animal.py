# Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos protegidos (encapsulación)
        self._nombre = nombre
        self._edad = edad

    # Método getter (encapsulación)
    def get_nombre(self):
        return self._nombre

    # Método que será sobrescrito (polimorfismo)
    def hacer_sonido(self):
        return "El animal hace un sonido"

    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"


# Clase derivada Perro (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad)
        self.raza = raza

    # Polimorfismo: sobrescritura del método
    def hacer_sonido(self):
        return "El perro ladra: ¡Guau guau!"

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Raza: {self.raza}"

class GestorAnimales:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal.mostrar_info())
            # Polimorfismo: cada objeto responde distinto
            print(animal.hacer_sonido())
            print("-" * 30)
#from modelos.perro import Perro
#from servicios.gestor_animales import GestorAnimales

def main():
    # Crear instancias de las clases
    perro1 = Perro("Max", 3, "Labrador")
    perro2 = Perro("Rocky", 5, "Pastor Alemán")

    # Crear el gestor (servicio)
    gestor = GestorAnimales()

    # Agregar animales
    gestor.agregar_animal(perro1)
    gestor.agregar_animal(perro2)

    # Mostrar información y comportamiento
    gestor.mostrar_animales()

if __name__ == "__main__":
    main()
