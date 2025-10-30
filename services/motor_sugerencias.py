from model.max_pq import MaxPQ
from services.ordenamiento import merge_sort_perfiles_por_nombre
from services.gestor_perfiles import GestorPerfiles
from typing import List, Optional, Dict

class MotorSugerencias:
    """
    Servicio que implementa la lógica para sugerir amigos (FoF) con priorización.
    Me quejaba de la hash y el union-find, aquí todo estuvo peor.
    Yo tengo la teoría de que Juanpa es freelancer en sus tiempos libres y de parcial nos pone
    sus proyectos. 
    """

    def __init__(self, gestor: GestorPerfiles):
        self.gestor = gestor

    def sugerirAmigos(self, userId: str, filtroGenero: Optional[str] = None,
                      filtroEdadMin: Optional[int] = None, filtroEdadMax: Optional[int] = None,
                      k: Optional[int] = None) -> List[Dict]:
        """
        Devuelve una lista de sugerencias ordenadas por prioridad (desc) y por nombre dentro de la misma prioridad.
        Cada entrada de retorno es un dict con keys: userId, nombreCompleto, edad, genero, prioridad.
        Parámetros de filtro son opcionales.
        """
        perfilX = self.gestor.buscarPerfil(userId)
        if perfilX is None:
            raise KeyError("El usuario solicitado no existe.")

        amigosDirectos = set([fid for fid, _ in perfilX.obtenerAmigos()])
        candidatos_prioridad: Dict[str, int] = {}  # userId -> prioridad maxima observada

        # 1) Iterar sobre amigos directos A de X
        for friendA_id, pesoXA in perfilX.obtenerAmigos():
            # Obtener perfil de A
            perfilA = self.gestor.buscarPerfil(friendA_id)
            if perfilA is None:
                continue
            # Iterar sobre amigos de A (B)
            for friendB_id, pesoAB in perfilA.obtenerAmigos():
                if friendB_id == userId:
                    continue
                if friendB_id in amigosDirectos:
                    continue
                # Potencial candidato — prioridad basada en calidad X-A (pesoXA)
                prioridad = pesoXA
                # Aplicar filtros tempranos consultando perfilB
                perfilB = self.gestor.buscarPerfil(friendB_id)
                if perfilB is None:
                    continue
                if filtroGenero is not None and perfilB.genero.lower() != filtroGenero.lower():
                    continue
                if filtroEdadMin is not None and perfilB.edad < filtroEdadMin:
                    continue
                if filtroEdadMax is not None and perfilB.edad > filtroEdadMax:
                    continue
                # Mantener prioridad maxima si candidato aparece por varios amigos
                actual = candidatos_prioridad.get(friendB_id)
                if actual is None or prioridad > actual:
                    candidatos_prioridad[friendB_id] = prioridad

        # 2) Insertar candidatos en MaxPQ
        pq = MaxPQ()
        for candId, prio in candidatos_prioridad.items():
            perfilCand = self.gestor.buscarPerfil(candId)
            if perfilCand is None:
                continue
            pq.insertar(perfilCand, prio)

        # 3) Extraer por prioridad y agrupar por prioridad para luego ordenar por nombre
        listado_resultados = []
        if pq.esta_vacia():
            return listado_resultados

        # Agrupar por prioridad: prioridad -> lista de Perfil
        grupos_por_prioridad = {}
        while not pq.esta_vacia():
            elem = pq.extraer_max()
            if elem is None:
                break
            prioridad, perfil = elem
            grupos_por_prioridad.setdefault(prioridad, []).append(perfil)

        # 4) Construir salida ordenada: prioridades descendentes, dentro de prioridad ordenar por nombre
        for prioridad in sorted(grupos_por_prioridad.keys(), reverse=True):
            lista_perfiles = grupos_por_prioridad[prioridad]
            lista_ordenada = merge_sort_perfiles_por_nombre(lista_perfiles)
            for perfil in lista_ordenada:
                listado_resultados.append({
                    "userId": perfil.userId,
                    "nombreCompleto": perfil.nombreCompleto,
                    "edad": perfil.edad,
                    "genero": perfil.genero,
                    "prioridad": prioridad
                })
                if k is not None and len(listado_resultados) >= k:
                    return listado_resultados
        return listado_resultados
