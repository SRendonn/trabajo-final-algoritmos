from models.Punto import Punto
from typing import Any, List, Dict  
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
from math import ceil


class AgglomerativeClustering:

    def __init__(self, domiciliarios : List[Domiciliario], puntosEntrega : List[PuntoEntrega]) -> None:
        self._domiciliarios : List[Domiciliario] = domiciliarios
        self._puntos_entrega : List[PuntoEntrega] = puntosEntrega

        self._clusters : List[Any] = list(map(lambda x: [x], self._puntos_entrega))

        self._clusters_actuales : int = len(self._puntos_entrega)
        self._tamano_maximo : int = ceil(len(self._puntos_entrega) / len(self._domiciliarios))



    def run(self) -> Dict[str,Any]:
        self.__get_clusters()
        self.__asignar_domiciliarios()
        return self.__response()


    def __get_clusters(self) -> None:

        while(self._clusters > len(self._puntos_entrega)):
            pass

    def __asignar_domiciliarios(self) -> None:
        pass

    def __response(self) -> Dict[str,Any]:
        response = {
            None
        }
        return response