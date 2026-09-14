"""Aplicación interactiva para gestionar adopciones de mascotas."""

from adopcion.models.mascota import Mascota
from adopcion.models.persona import Adoptante
from adopcion.models.refugio import Refugio

# Creamos el refugio
refugio = Refugio()

# Registramos 3 mascotas de ejemplo
refugio.registrar_mascota(Mascota("Firulais", "Perro", 3))
refugio.registrar_mascota(Mascota("Misu", "Gato", 2))
refugio.registrar_mascota(Mascota("Rocky", "Perro", 5))

# Creamos un adoptante
adoptante = Adoptante("Juan", 25)

# Menú interactivo
while True:
    print("\n--- Menú de Adopción ---")
    print("1. Listar mascotas disponibles")
    print("2. Adoptar una mascota")
    print("3. Ver mascotas adoptadas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        disponibles = refugio.listar_disponibles()
        if disponibles:
            print("\nMascotas disponibles:")
            for m in disponibles:
                print(m)
        else:
            print("\nNo hay mascotas disponibles.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre de la mascota que desea adoptar: ")
        resultado = refugio.asignar_adopcion(nombre, adoptante)
        print(resultado)

    elif opcion == "3":
        if adoptante.mascotas_adoptadas:
            print("\nMascotas adoptadas por", adoptante.nombre)
            for m in adoptante.mascotas_adoptadas:
                print(m)
        else:
            print("\nNo ha adoptado ninguna mascota.")

    elif opcion == "4":
        print("¡Gracias por usar el sistema de adopción!")
        break

    else:
        print("Opción inválida, intente de nuevo.")
