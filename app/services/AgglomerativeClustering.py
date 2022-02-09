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

        

        def encontrar_par(lista: List[Punto]) -> Tuple[self._tupla_puntos_type, List[Punto], float]:
            pares_cercanos: Tuple[self._tupla_puntos_type, List[Punto], float] = Punto.pares_cercanos(lista)
            if pares_cercanos[0][0].get_index() == pares_cercanos[0][1].get_index():
                raise Exception('Mismo punto')
            
            #print(pares_cercanos[0][0].get_tamano(),pares_cercanos[0][1].get_tamano(), self._tamano_maximo)
            #print(pares_cercanos[0][0].get(), pares_cercanos[0][1].get())

            if pares_cercanos[0][0].get_tamano() + pares_cercanos[0][1].get_tamano() > self._tamano_maximo:
                if(len(pares_cercanos[1]) > 0):
                    
                    R: bool = False
                    L: bool = False

                    if pares_cercanos[0][0].get_tamano() < self._tamano_maximo:
                        L = True
                        lista_L = pares_cercanos[1][:]
                        lista_L.append(pares_cercanos[0][0])
                        try:
                            pares_cercanos_L = encontrar_par(lista_L)
                        except Exception as e:
                            print(e)
                            L = False
                    
                    if pares_cercanos[0][1].get_tamano() < self._tamano_maximo:
                        R = True
                        lista_R = pares_cercanos[1][:]
                        lista_R.append(pares_cercanos[0][1])
                        try:
                            pares_cercanos_R = encontrar_par(lista_R)
                        except Exception as e:
                            print(e)
                            R = False
                    
                    if(L and R):
                        return min(pares_cercanos_L,pares_cercanos_R, key=lambda x: x[2])
                    elif L:
                        return pares_cercanos_L
                    elif R:
                        return pares_cercanos_R
                    else:
                        raise Exception('Ninguno cumple')
                else:
                    raise Exception('Ninguno cumple, busque punto medio')
            else:
                return pares_cercanos

        def get_punto_medio(puntos: List[Punto], asignar_conexiones: bool = False) -> Punto:

            suma_x: float = 0
            suma_y: float = 0

            tamano: int = 0

            for punto in puntos:
                suma_x += punto.get_x()
                suma_y += punto.get_y()
                tamano += punto.get_tamano()

            punto_medio: Punto = Punto(suma_x/2, suma_y/2, tamano=tamano)

            if asignar_conexiones:
                punto_medio.set_conexiones(puntos)
                
            return punto_medio

        while(self._clusters_actuales > len(self._domiciliarios)):
            print("------------")
            #print(self._clusters_actuales)
            try:
                pares_cercanos = encontrar_par(self._clusters)
                self._clusters = pares_cercanos[1]
                punto_medio: Punto = get_punto_medio(list(pares_cercanos[0]), True)
                self._clusters.append(punto_medio)
                self._clusters_actuales -= 1
            except Exception as e:
                print(e)


    def __asignar_domiciliarios(self) -> None:
        pass

    def __response(self) -> List[Punto]:
        return self._clusters