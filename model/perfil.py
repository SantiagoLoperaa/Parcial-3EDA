# Leí que el símbolo -> en Python sirve para indicar el tipo de dato que devuelve una función o método
from typing import Dict, List, Tuple

class Perfil:

    def __init__(self, userId: str, nombreCompleto: str, edad: int, genero: str):
        # Acá nicializamos los atributos del perfil
        self.userId = str(userId)
        self.nombreCompleto = nombreCompleto
        self.edad = int(edad)
        self.genero = genero
        self.listaAmigos: Dict[str, int] = {}  # friendId: peso de 1 a 5

    def agregarAmigo(self, friendId: str, peso: int) -> None:
        """
        Acá se agrega o actualiza la amistad con friendId y asigna el peso (1-5).
        """
        if peso < 1 or peso > 5:
            raise ValueError("El peso de amistad debe estar entre 1 y 5.")
        self.listaAmigos[str(friendId)] = int(peso)

    def eliminarAmigo(self, friendId: str) -> None:
        """
        Aquí se elimina la relación de amistad con friendId si existe.
        """
        self.listaAmigos.pop(str(friendId), None)

    def esAmigoDirecto(self, friendId: str) -> bool:
        """
        Retornamos True si friendId está en la lista de amigos.
        """
        return str(friendId) in self.listaAmigos

    def obtenerAmigos(self) -> List[Tuple[str, int]]:
        """
        Devuelve una lista de tuplas (friendId, peso).
        """
        return list(self.listaAmigos.items())

    def obtenerPesoAmistad(self, friendId: str) -> int:
        """
        Retorna el peso de amistad con friendId o None si no existe.
        """
        return self.listaAmigos.get(str(friendId))
