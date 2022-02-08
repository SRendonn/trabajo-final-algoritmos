import math
from this import d
from typing import Tuple, List, Any


class Punto:

    def __init__(self, x: int, y: int, conexiones: List['Punto'] = []) -> None:
        self._x = x
        self._y = y
        self._conexiones: List['Punto'] = conexiones
        self._bloqueado: bool = False
        self._indice: int = None

    def get(self) -> Tuple:
        return (self._x, self._y)

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def set_index(self, index: int) -> None:
        self._indice = index

    @staticmethod
    def distancia_entre_puntos(p1: 'Punto', p2: 'Punto') -> float:
        return math.sqrt((p1.get_x() - p2.get_x())**2 + (p1.get_y() - p2.get_y())**2)
        # Se usa la distancia euclidiana, explicar por que

    @staticmethod
    def pares_cercanos(listaPuntos: List['Punto']) -> Tuple[Tuple['Punto', 'Punto'], float]:

        tupla_puntos_type = Tuple['Punto', 'Punto']

        # Lo ideal seria solo ordenar una vez, y cada que saquemos un punto medio guardarlo donde ya deberia ir
        listaPuntos.sort(key=lambda x: x.get_x())

        for index in range(len(listaPuntos)):
           listaPuntos[index].set_index(index)
        # -------------------------------------------

        def dividir_pares_separados(i: int, j: int, puntosSeleccionados: Tuple[tupla_puntos_type, float]) -> Tuple[tupla_puntos_type, float]:
            delta = puntosSeleccionados[1]

            xP: float = listaPuntos[(i + j) // 2].get_x()
            s: List['Punto'] = []

            for k in range(i, j + 1):
                if(abs(listaPuntos[k].get_x() - xP) < delta):
                    s.append(listaPuntos[k])

            s.sort(key=lambda x: x.get_y())
            respuesta = puntosSeleccionados
            for p in range(0, len(s) - 1):
                q = p + 1
                while q < len(s) and q <= p + 7:
                    d = Punto.distancia_entre_puntos(s[p], s[q])
                    if d < respuesta[1]:
                        respuesta = ((s[p], s[q]), d)
                    q += 1
            return respuesta

        def dividir_pares(i: int, j: int) -> Tuple[tupla_puntos_type, float]:
            if i == j:
                return ((listaPuntos[i], listaPuntos[j]), math.inf)
            elif j - i == 1:
                return ((listaPuntos[i], listaPuntos[j]), Punto.distancia_entre_puntos(listaPuntos[i], listaPuntos[j]))
            else:
                dl: Tuple[tupla_puntos_type, float] = dividir_pares(
                    i, (i + j) // 2)
                dr: Tuple[tupla_puntos_type, float] = dividir_pares(
                    1 + (i + j) // 2, j)

                puntosSeleccionados: Tuple[tupla_puntos_type, float]

                if dl[1] < dr[1]:
                    puntosSeleccionados = dl
                else:
                    puntosSeleccionados = dr

                return dividir_pares_separados(i, j, puntosSeleccionados)
        
        par_cercano = dividir_pares(0, len(listaPuntos) - 1)
        lista_nueva = listaPuntos[:]
        print(par_cercano[0][0]._indice)
        print(listaPuntos[par_cercano[0][0]._indice])
        print(par_cercano[0][0])
        return par_cercano
