"""Gestión de las mascotas disponibles en el refugio."""

from adopcion.models.helpers import buscar_mascota
from adopcion.models.mascota import Mascota


# Clase Refugio: administra las mascotas disponibles
class Refugio:
    """Administra las mascotas disponibles para adopción."""

    def __init__(self):
        # Atributo privado: lista de mascotas
        self.__mascotas = []

    def registrar_mascota(self, mascota: Mascota):
        """Registra una mascota nueva en el refugio."""
        # Agregar una nueva mascota al refugio
        self.__mascotas.append(mascota)

    def listar_disponibles(self):
        """Retorna las mascotas que aún no han sido adoptadas."""
        # Retornar solo las mascotas que NO han sido adoptadas
        return [m for m in self.__mascotas if not m.adoptado]

    def asignar_adopcion(self, nombre_mascota: str, adoptante):
        """Asigna una mascota disponible a un adoptante."""
        # Buscar la mascota por nombre usando la función auxiliar
        mascota = buscar_mascota(nombre_mascota, self.__mascotas)

        if mascota is None:
            return f"Error: La mascota '{nombre_mascota}' no existe en el refugio."
        if mascota.adoptado:
            return f"Error: La mascota '{nombre_mascota}' ya fue adoptada."

        # Si está disponible, se asigna al adoptante
        adoptante.adoptar(mascota)
        return f"La mascota '{nombre_mascota}' ha sido adoptada por {adoptante.nombre}."
