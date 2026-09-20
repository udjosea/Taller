# Clase Persona: representa a una persona en general
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


class Adoptante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.mascotas_adoptadas = []

    def adoptar(self, mascota):
        self.mascotas_adoptadas.append(mascota)
""" class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."


# Clase Adoptante: hereda de Persona y puede adoptar mascotas
class Adoptante(Persona):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)  # Llamamos al constructor de Persona
        self.mascotas_adoptadas = []  # Lista vacía para guardar mascotas adoptadas

    def adoptar(self, mascota):
        # Agregamos la mascota a la lista y cambiamos su estado
        self.mascotas_adoptadas.append(mascota)
        mascota.adoptado = True
        return f"{self.nombre} ha adoptado a {mascota.nombre}."
 """
