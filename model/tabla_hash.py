from typing import List, Tuple, Optional
from model.perfil import Perfil
"""
    Esta mondá costó mucho Juanpa
"""
class TablaHash:

    def __init__(self, capacidad_inicial: int = 103):
        # Usar un número primo como tamaño inicial para mejor distribución 
        self.capacidad = capacidad_inicial
        self.buckets: List[List[Tuple[str, Perfil]]] = [[] for _ in range(self.capacidad)]
        self.cantidad = 0
        self.factorCargaMax = 0.75

    def _hash(self, key: str) -> int:
        """
        Función hash simple basada en suma de códigos y módulo de capacidad.
        """
        # Acepta claves como cadenas
        return sum(ord(c) for c in str(key)) % self.capacidad

    def insertar(self, key: str, valor: Perfil) -> None:
        """
        Inserta o actualiza la entrada (key -> Perfil).
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == str(key):
                bucket[i] = (str(key), valor)
                return
        bucket.append((str(key), valor))
        self.cantidad += 1
        if self.cantidad / self.capacidad > self.factorCargaMax:
            self._rehash()

    def buscar(self, key: str) -> Optional[Perfil]:
        """
        Busca y devuelve el Perfil asociado con la clave o None si no existe.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == str(key):
                return v
        return None

    def eliminar(self, key: str) -> bool:
        """
        Elimina la entrada si existe y retorna True si se eliminó.
        """
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == str(key):
                bucket.pop(i)
                self.cantidad -= 1
                return True
        return False

    def _rehash(self) -> None:
        """
        Redimensiona la tabla a un tamaño aproximadamente doble (primo) y reubica entradas.
        """
        antiguaBuckets = self.buckets
        self.capacidad = self.capacidad * 2 + 1
        self.buckets = [[] for _ in range(self.capacidad)]
        self.cantidad = 0
        for bucket in antiguaBuckets:
            for k, v in bucket:
                self.insertar(k, v)

    def cargar_desde_csv(self, ruta_csv: str, separador: str = ',') -> int:
        """
        Carga perfiles desde un archivo CSV con columnas: userId,nombreCompleto,edad,genero
        Retorna la cantidad de perfiles cargados.
        """
        import csv
        cargados = 0
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.reader(csvfile, delimiter=separador)
            for fila in lector:
                if not fila or len(fila) < 4:
                    continue
                userId, nombreCompleto, edad, genero = fila[0], fila[1], fila[2], fila[3]
                perfil = Perfil(userId, nombreCompleto, int(edad), genero)
                self.insertar(userId, perfil)
                cargados += 1
        return cargados
