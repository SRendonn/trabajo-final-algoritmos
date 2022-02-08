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

        self._clusters_actuales : int = len(self._puntos_entrega)
        self._tamano_maximo : int = ceil(len(self._puntos_entrega) / len(self._domiciliarios))

        self._tupla_puntos_type = Tuple[Punto, Punto]



    def run(self) -> Dict[str,Any]:
        self.__get_clusters()
        self.__asignar_domiciliarios()
        return self.__response()


    def __get_clusters(self) -> None:
        def get_punto_medio(tupla_puntos: self._tupla_puntos_type) -> Punto:
            punto_1: Punto = tupla_puntos[0]
            punto_2: Punto = tupla_puntos[1]

            punto_medio: Punto = Punto(
                (punto_1.get_x() + punto_2.get_x())/2,
                (punto_1.get_y() + punto_2.get_y())/2,
                list(tupla_puntos)
            )

            return punto_medio     

        clusters_pendientes : List[Punto]

        pares_cercanos: Tuple[self._tupla_puntos_type, float] = Punto.pares_cercanos(self._clusters)
        
        #while(self._clusters_actuales > len(self._puntos_entrega)):
        #   pares_cercanos: Tuple[self._tupla_puntos_type, float] = Punto.pares_cercanos(self._clusters)

           



    def __asignar_domiciliarios(self) -> None:
        pass

    def __response(self) -> Dict[str,Any]:
        response = {
            None
        }
        return response