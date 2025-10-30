from typing import Dict

class UnionFindWeighted:
    """
    Me quejaba de la tabla hash y esto estuvo peor (sobre todo porque falté a esta clase :( ).
    """

    def __init__(self):
        # parent: nodo -> padre
        # size: root -> tamaño del árbol
        self.parent: Dict[str, str] = {}
        self.size: Dict[str, int] = {}

    def agregar(self, nodo: str) -> None:
        """
        Agrega nodo como conjunto singleton si no existe.
        """
        nodo = str(nodo)
        if nodo not in self.parent:
            self.parent[nodo] = nodo
            self.size[nodo] = 1

    def find(self, nodo: str) -> str:
        """
        Encuentra la raíz de nodo con compresión de caminos.
        """
        nodo = str(nodo)
        if nodo not in self.parent:
            self.agregar(nodo)
        # Encontrar raíz
        raiz = nodo
        while self.parent[raiz] != raiz:
            raiz = self.parent[raiz]
        # Compresión de caminos
        while nodo != raiz:
            siguiente = self.parent[nodo]
            self.parent[nodo] = raiz
            nodo = siguiente
        return raiz

    def union(self, nodo1: str, nodo2: str) -> None:
        """
        Une los conjuntos que contienen nodo1 y nodo2. Usa tamaño (weighted).
        """
        r1 = self.find(nodo1)
        r2 = self.find(nodo2)
        if r1 == r2:
            return
        if self.size[r1] < self.size[r2]:
            self.parent[r1] = r2
            self.size[r2] += self.size[r1]
        else:
            self.parent[r2] = r1
            self.size[r1] += self.size[r2]

    def estan_conectados(self, nodo1: str, nodo2: str) -> bool:
        """
        Retorna True si ambos nodos pertenecen al mismo componente conectado.
        """
        return self.find(nodo1) == self.find(nodo2)
