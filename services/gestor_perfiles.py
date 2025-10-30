from model.tabla_hash import TablaHash
from model.perfil import Perfil
from model.union_find import UnionFindWeighted
from typing import Optional

class GestorPerfiles:
    """
    Aca creé el ervicio que une la TablaHash y UnionFind para gestionar perfiles y la creación de lazos.
    """

    def __init__(self, capacidad_inicial: int = 103):
        self.tabla = TablaHash(capacidad_inicial)
        self.unionFind = UnionFindWeighted()

    def crearPerfil(self, userId: str, nombreCompleto: str, edad: int, genero: str) -> Perfil:
        """
        Crea un perfil y lo inserta en la tabla hash. Retorna el perfil creado.
        """
        perfil = Perfil(userId, nombreCompleto, edad, genero)
        self.tabla.insertar(userId, perfil)
        self.unionFind.agregar(userId)
        return perfil

    def buscarPerfil(self, userId: str) -> Optional[Perfil]:
        """
        Busca y retorna el perfil por userId o None.
        """
        return self.tabla.buscar(userId)

    def generarLazo(self, userIdA: str, userIdB: str, calidad: int) -> None:
        """
        Crea una amistad bidireccional entre amigo A y amigo B con la calidad especificada.
        Actualiza la TablaHash y la estructura UnionFind.
        """
        perfilA = self.buscarPerfil(userIdA)
        perfilB = self.buscarPerfil(userIdB)
        if perfilA is None or perfilB is None:
            raise KeyError("Uno o ambos perfiles no existen.")
        if calidad < 1 or calidad > 5:
            raise ValueError("La calidad debe estar entre 1 y 5.")
        # Agregar/actualizar en listas de amigos
        perfilA.agregarAmigo(userIdB, calidad)
        perfilB.agregarAmigo(userIdA, calidad)
        # Unir en union-find
        self.unionFind.union(userIdA, userIdB)

    def estanConectados(self, userIdA: str, userIdB: str) -> bool:
        """
        Indica si userIdA y userIdB están en el mismo componente (union-find).
        """
        return self.unionFind.estan_conectados(userIdA, userIdB)

    def cargarPerfilesDesdeCSV(self, ruta_csv: str, separador: str = ',') -> int:
        """
        Delegar la carga masiva a la TablaHash. Retorna la cantidad cargada.
        """
        cantidad = self.tabla.cargar_desde_csv(ruta_csv, separador)
        # Asegurar que union-find tenga entradas para cada perfil
        # Recorremos buckets y agregamos nodos al union-find
        for bucket in self.tabla.buckets:
            for userId, perfil in bucket:
                self.unionFind.agregar(userId)
        return cantidad
