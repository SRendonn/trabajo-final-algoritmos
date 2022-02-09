from models.Punto import Punto
from typing import Any, List, Dict, Tuple
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
from math import ceil

class AgglomerativeClustering:

    def __init__(self, domiciliarios : List[Domiciliario], puntosEntrega : List[PuntoEntrega]) -> None:
        self._domiciliarios : List[Domiciliario] = domiciliarios
        self._puntos_entrega : List[PuntoEntrega] = puntosEntrega
        self._clusters : List[Any] = self._puntos_entrega[:]
        self._clusters_completos : List[Any] = []
        self._clusters_actuales : int = len(self._puntos_entrega)
        self._tamano_maximo : int = ceil(len(self._puntos_entrega) / len(self._domiciliarios))
        self._tupla_puntos_type = Tuple[Punto, Punto]

    def run(self) -> Dict[str,Any]:
        self.__get_clusters()
        return self.__response()

    def __get_clusters(self) -> None:
        while(self._clusters_actuales > len(self._domiciliarios)):
            try:
                pares_cercanos: Tuple[self._tupla_puntos_type, List[Punto], float] = Punto.pares_cercanos(self._clusters)
                self._clusters = pares_cercanos[1]
                punto_medio: Punto = Punto.get_punto_medio(list(pares_cercanos[0]), True)
                if punto_medio.get_tamano() >= len(self._domiciliarios):
                    self._clusters_completos.append(punto_medio)
                else:
                    self._clusters.append(punto_medio)
                self._clusters_actuales -= 1
            except Exception as e:
                print(e)


    def __response(self) -> List[Punto]:
        return self._clusters + self._clusters_completos