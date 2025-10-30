from typing import List, Tuple, Any

class MaxPQ:
    """
    Implementé de forma simple una Max Priority Queue basada en un heap binario.
    Se almacena como lista de tuplas (prioridad, item). Prioridad más alta -> extraído primero.
    """

    def __init__(self):
        self.heap: List[Tuple[int, Any]] = []

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][0] <= self.heap[parent][0]:
                break
            self._swap(idx, parent)
            idx = parent

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            left = 2*idx + 1
            right = 2*idx + 2
            largest = idx
            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            if largest == idx:
                break
            self._swap(idx, largest)
            idx = largest

    def insertar(self, item: Any, prioridad: int) -> None:
        """
        Inserta un item con la prioridad dada (int).
        """
        self.heap.append((int(prioridad), item))
        self._sift_up(len(self.heap) - 1)

    def extraer_max(self):
        """
        Extrae y retorna el elemento con mayor prioridad. Retorna (prioridad, item).
        """
        if not self.heap:
            return None
        max_elem = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return max_elem

    def esta_vacia(self) -> bool:
        return len(self.heap) == 0

    def tamaño(self) -> int:
        return len(self.heap)
