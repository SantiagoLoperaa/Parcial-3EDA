"""""
Simulación de Red Social - Parcial #4 (Masacre en la UPB)

Básicamente este archivo demuestra el flujo completo del proyecto:
1. Carga masiva de perfiles desde CSV (Tabla Hash)
2. Generación aleatoria de lazos de amistad (Grafo)
3. Verificación de conectividad (Union-Find)
4. Sugerencia de amigos (Cola de Prioridad + Merge Sort)
"""""

import random
from services.gestor_perfiles import GestorPerfiles
from services.motor_sugerencias import MotorSugerencias

def main():
    print("------------------------------------------------")
    print(" SIMULACIÓN DE RED SOCIAL - PARCIAL #4")
    print("------------------------------------------------\n")

    # 1 Crear el gestor principal de perfiles
    gestor = GestorPerfiles()

    # 2 Cargar los perfiles desde un archivo CSV
    print(" Cargando perfiles desde data/perfiles_ejemplo.csv ...")
    cantidad = gestor.cargarPerfilesDesdeCSV("data/perfiles_ejemplo.csv")
    print(f" {cantidad} perfiles cargados correctamente.\n")

    # 3️3 Generar amistades aleatorias entre los usuarios cargados
    print(" Generando lazos de amistad aleatorios...")
    generar_amistades_aleatorias(gestor, cantidad)
    print(" Lazos generados exitosamente.\n")

    # 4️ Verificar conectividad entre dos usuarios
    print(" Verificando conectividad (Union-Find):")
    print("¿u1 y u3 están conectados?", gestor.estanConectados("u1", "u3"))
    print("¿u4 y u6 están conectados?", gestor.estanConectados("u4", "u6"))
    print()

    # 5 Crear el motor de sugerencias
    motor = MotorSugerencias(gestor)

    # 6 Mostrar sugerencias sin filtros
    print(" Sugerencias generales para el usuario u1 (Ana Perez):")
    sugerencias = motor.sugerirAmigos("u1")
    mostrar_sugerencias(sugerencias)

    # 7 Mostrar sugerencias filtradas por género masculino
    print("\n Sugerencias para u1 (solo género masculino):")
    sugerencias_m = motor.sugerirAmigos("u1", filtroGenero="M")
    mostrar_sugerencias(sugerencias_m)

    # 8 Mostrar sugerencias filtradas por rango de edad
    print("\n Sugerencias para u1 (edad entre 25 y 35 años):")
    sugerencias_edad = motor.sugerirAmigos("u1", filtroEdadMin=25, filtroEdadMax=35)
    mostrar_sugerencias(sugerencias_edad)

    print("\n Simulación finalizada con éxito.")
    print("------------------------------------------------")

# --------------------------------------------------------------
# Función auxiliar: Generar amistades aleatorias
# --------------------------------------------------------------
def generar_amistades_aleatorias(gestor: GestorPerfiles, cantidad_perfiles: int, lazos_min: int = 4, lazos_max: int = 7):
    """
    Crea lazos de amistad aleatorios entre los perfiles existentes.
    Parámetros:
      gestor: instancia de GestorPerfiles
      cantidad_perfiles: cantidad total de perfiles cargados
      lazos_min / lazos_max: rango de cantidad de lazos por perfil
    """
    # Obtener todos los userIds cargados
    todos_ids = []
    for bucket in gestor.tabla.buckets:
        for userId, _ in bucket:
            todos_ids.append(userId)

    # Crear lazos aleatorios
    for userId in todos_ids:
        num_lazos = random.randint(lazos_min, lazos_max)
        posibles_amigos = [x for x in todos_ids if x != userId]
        random.shuffle(posibles_amigos)
        seleccionados = posibles_amigos[:num_lazos]

        for amigoId in seleccionados:
            # Generar una calidad aleatoria de amistad (1 a 5)
            calidad = random.randint(1, 5)
            try:
                gestor.generarLazo(userId, amigoId, calidad)
            except Exception:
                # Evitar duplicar lazos ya existentes
                continue

# --------------------------------------------------------------
# Función auxiliar: Mostrar sugerencias formateadas
# --------------------------------------------------------------
def mostrar_sugerencias(lista_sugerencias):
    """
    Muestra de forma formateada las sugerencias obtenidas.
    """
    if not lista_sugerencias:
        print("   (sin sugerencias disponibles)")
        return

    for s in lista_sugerencias:
        print(f"   → {s['nombreCompleto']} ({s['genero']}, {s['edad']} años) "
              f"[Prioridad: {s['prioridad']}]")

# --------------------------------------------------------------
# Punto de entrada del programa
# --------------------------------------------------------------
if __name__ == "__main__":
    main()

