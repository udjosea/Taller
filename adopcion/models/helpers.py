# Función auxiliar para buscar una mascota en una lista
def buscar_mascota(nombre: str, lista_mascotas: list):
    for mascota in lista_mascotas:
        if mascota.nombre.lower() == nombre.lower():  # Ignora mayúsculas/minúsculas
            return mascota
    return None  # Si no se encuentra, retorna None
