from typing import Any, List, Dict  
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
import random


class Generador:

    def __init__(self, numero_domiciliarios : int, numero_puntos_entrega : int) -> None:

        self._numero_domiciliarios = numero_domiciliarios
        self._numero_puntos_entrega = numero_puntos_entrega
        self._domiciliarios : List[Domiciliario] = []
        self._puntos_entrega : List[PuntoEntrega] = []


    def run(self) -> Dict[str,Any]:
        self.__get_domiciliarios()
        self.__get_puntos_entrega()
        return self.__response()
    
    def __get_domiciliarios(self) -> None:
        for _ in range(self._numero_domiciliarios):
            x = random.random()*100
            y = random.random()*100
            domiciliario = Domiciliario(x,y)
            self._domiciliarios.append(domiciliario)

    def __get_puntos_entrega(self) -> None:
        for _ in range(self._numero_puntos_entrega):
            x = random.random()*100
            y = random.random()*100
            punto_entrega = PuntoEntrega(x,y)
            self._puntos_entrega.append(punto_entrega)


    def __response(self) -> Dict[str,Any]:
        response = {
            'domiciliarios' : self._domiciliarios,
            'puntos_entrega' : self._puntos_entrega
        }
        return response