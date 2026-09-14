# Clase Mascota: representa una mascota en el refugio
class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, adoptado: bool = False):
        # Atributos básicos de la mascota
        self.nombre = nombre  # Nombre de la mascota
        self.especie = especie  # Especie (ejemplo: "Perro", "Gato")
        self.edad = edad  # Edad en años
        self.adoptado = adoptado  # Estado de adopción (por defecto False)

    def __str__(self):
        # Este método define cómo se mostrará la mascota al imprimirla
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Adoptado: {self.adoptado}"
