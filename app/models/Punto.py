import math
from typing import Tuple, List, Any
import heapq


class Punto:

    def __init__(self, x: int, y: int, conexiones: List['Punto'] = [], tamano: int = 1) -> None:
        self._x = x
        self._y = y
        self._conexiones: List['Punto'] = conexiones
        self._indice: int = None
        self._tamano = tamano

    def get(self) -> Tuple:
        return (self._x, self._y)

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def set_tamano(self, tamano: int) -> int:
        self._tamano = tamano

    def get_tamano(self) -> int:
        return self._tamano

    def set_index(self, index: int) -> None:
        self._indice = index

    def get_index(self) -> int:
        return self._indice

    def set_conexiones(self, conexiones: List['Punto']):
        self._conexiones = conexiones

    def get_conexiones(self) -> List['Punto']:
        return self._conexiones

    def to_list(self) -> List['Punto']:
        lista: List['Punto'] = []
        if self.get_tamano() > 1:
            for punto in self.get_conexiones():
                lista = lista + punto.to_list()
            return lista
        else:
            return [self]
            


    # en la lista de puntos no se debe incluir el punto a buscar
    @staticmethod
    def get_punto_mas_cercano(punto_a_buscar: 'Punto', puntos: List['Punto']) -> Tuple['Punto', float]:
        distancia_mas_cercana = math.inf
        punto_mas_cercano = None
        for i in range(len(puntos)):
            distancia = Punto.distancia_entre_puntos(puntos[i], punto_a_buscar)
            if distancia < distancia_mas_cercana:
                distancia_mas_cercana = distancia
                punto_mas_cercano = puntos[i]
                punto_mas_cercano._indice = i
        return (punto_mas_cercano, distancia_mas_cercana)

    @staticmethod
    def get_punto_medio(puntos: List['Punto'], asignar_conexiones: bool = False) -> 'Punto':

        suma_x: float = 0
        suma_y: float = 0

        tamano: int = 0

        for punto in puntos:
            suma_x += punto.get_x()
            suma_y += punto.get_y()
            tamano += punto.get_tamano()

        punto_medio: Punto = Punto(
            suma_x/len(puntos), suma_y/len(puntos), tamano=tamano)

        if asignar_conexiones:
            punto_medio.set_conexiones(puntos)

        return punto_medio

    @staticmethod
    def distancia_entre_puntos(p1: 'Punto', p2: 'Punto') -> float:
        return math.sqrt((p1.get_x() - p2.get_x())**2 + (p1.get_y() - p2.get_y())**2)
        # Se usa la distancia euclidiana, explicar por que
    
    @staticmethod
    def lista_pares_cercanos(listaPuntos: List['Punto']):
        lista = []
        for i in range(len(listaPuntos) - 1):
            for j in range(i + 1, len(listaPuntos)):
                distancia = Punto.distancia_entre_puntos(listaPuntos[i], listaPuntos[j])
                lista.append((distancia, (listaPuntos[i], listaPuntos[j])))
        return lista


    @staticmethod
    def pares_cercanos(listaPuntos: List['Punto']) -> Tuple[Tuple['Punto', 'Punto'], List['Punto'], float]:

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
        if(par_cercano[0][0]._indice > par_cercano[0][1]._indice):
            del lista_nueva[par_cercano[0][0]._indice]
            del lista_nueva[par_cercano[0][1]._indice]
        else:
            del lista_nueva[par_cercano[0][1]._indice]
            del lista_nueva[par_cercano[0][0]._indice]
        return (par_cercano[0], lista_nueva, par_cercano[1])
