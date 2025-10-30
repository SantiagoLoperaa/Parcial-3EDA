from typing import List
from model.perfil import Perfil

def merge_sort_perfiles_por_nombre(perfiles: List[Perfil]) -> List[Perfil]:
    """
    Este método ordena una lista de perfiles por atributo nombreCompleto (ascendente) usando merge sort.
    Lo implementé porque es un algoritmo de ordenamiento eficiente y estable, ideal para listas grandes.
    Lo hice con ayuda del recurso que diste en clase y con ChatGPT.
    """
    if len(perfiles) <= 1:
        return perfiles[:]
    mid = len(perfiles) // 2
    left = merge_sort_perfiles_por_nombre(perfiles[:mid])
    right = merge_sort_perfiles_por_nombre(perfiles[mid:])
    return _merge(left, right)

def _merge(left, right):
    i = j = 0
    resultado = []
    while i < len(left) and j < len(right):
        if left[i].nombreCompleto.lower() <= right[j].nombreCompleto.lower():
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado
