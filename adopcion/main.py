"""Aplicación interactiva para gestionar adopciones de mascotas."""

import sys #permite trabajar con el sistema de Python.
from pathlib import Path

 #permite manejar rutas de archivos de forma segura.

if __package__ in (None, ""):#verifica si el script se está ejecutando directamente, no como parte de un paquete.
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent)) #Si es directo, __package__ suele estar vacío.
#En ese caso, Python no sabe automáticamente que adopcion es un paquete, así que se agrega la carpeta padre al sys.path:
    from adopcion.models.mascota import Mascota #Esto hace que el proyecto pueda importar:
    from adopcion.models.persona import Adoptante
    from adopcion.models.refugio import Refugio
else: #se ejecuta cuando el archivo se importa como parte de un paquete
    from .models.mascota import Mascota #En ese caso, se usan imports relativos
    from .models.persona import Adoptante #porque ya estamos dentro del paquete adopcion.1
    from .models.refugio import Refugio

def registrar_mascotas_ejemplo(refugio):# Registramos 3 mascotas de ejemplo
    mascotas = [
        Mascota("Firulais", "Perro", 3),
        Mascota("Misu", "Gato", 2),
        Mascota("Rocky", "Perro", 5),
    ]

    for mascota in mascotas:
        refugio.registrar_mascota(mascota)    

def mostrar_mascotas(lista_mascotas):
    if not lista_mascotas:
        print("No hay mascotas registradas.")
        return

    for mascota in lista_mascotas:
        print(mascota)

def main():
# Creamos el refugio
    refugio = Refugio()
    # Creamos un adoptante
    adoptante = Adoptante("Juan", 25)
    registrar_mascotas_ejemplo(refugio)
    print("Bienvenido al sistema de adopción.")
    adoptante.presentarse()

    # Registramos 3 mascotas de ejemplo_old
    """ refugio.registrar_mascota(Mascota("Firulais", "Perro", 3))
    refugio.registrar_mascota(Mascota("Misu", "Gato", 2))
    refugio.registrar_mascota(Mascota("Rocky", "Perro", 5)) """


    # Menú interactivo
    while True:
                print("\n--- Menú de Adopción ---")
                print("1. Listar mascotas disponibles")
                print("2. Adoptar una mascota")
                print("3. Ver mascotas adoptadas")
                print("4. Salir")

                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    disponibles = refugio.listar_disponibles()
                    print("\nMascotas disponibles:")
                    mostrar_mascotas(disponibles)
                    """ disponibles = refugio.listar_disponibles()
                    if disponibles:
                        print("\nMascotas disponibles:")
                        for m in disponibles:
                            print(m)
                    else:
                        print("\nNo hay mascotas disponibles.") """

                elif opcion == "2":
                    nombre = input("Ingrese el nombre de la mascota que desea adoptar: ").strip()
                    resultado = refugio.asignar_adopcion(nombre, adoptante)
                    print(resultado)

                elif opcion == "3":
                    print("\nMascotas adoptadas por", adoptante.nombre)
                    if not adoptante.mascotas_adoptadas:
                        print("Todavía no ha adoptado ninguna mascota.")
                    else:
                        for mascota in adoptante.mascotas_adoptadas:
                            print(mascota)
                            """ if adoptante.mascotas_adoptadas:
                                print("\nMascotas adoptadas por", adoptante.nombre)
                                for m in adoptante.mascotas_adoptadas:
                                    print(m)
                            else:
                                print("\nNo ha adoptado ninguna mascota.")"""
                elif opcion == "4":
                    print("¡Gracias por usar el sistema de adopción!")
                    break

                else:
                    print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
