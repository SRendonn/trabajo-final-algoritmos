from models.Punto import Punto
from typing import Any, List, Dict, Tuple
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
from math import ceil
import heapq

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
        self.__asignar_domiciliarios()
        return self.__response()



    def __get_clusters(self) -> None:

        def encontrar_par_fuerza_bruta(lista: List[Punto]) -> Tuple[self._tupla_puntos_type, List[Punto], float]:
            pares_cercanos: Tuple[self._tupla_puntos_type, List[Punto], float] = Punto.pares_cercanos(lista)
            
            print(pares_cercanos[0][0].get_tamano(),pares_cercanos[0][1].get_tamano(), self._tamano_maximo)
            print(pares_cercanos[0][0].get(), pares_cercanos[0][1].get())


            if pares_cercanos[0][0].get_tamano() + pares_cercanos[0][1].get_tamano() > self._tamano_maximo:
                if(len(pares_cercanos[1]) > 0):
                    lista_ordenada = Punto.lista_pares_cercanos(lista)
                    copia_lista_ordenada = lista_ordenada[:]
                    heapq.heapify(lista_ordenada)
                    while len(lista_ordenada) > 0:
                        mas_cercano = heapq.heappop(lista_ordenada)
                        if mas_cercano[1][0].get_tamano() + mas_cercano[1][1].get_tamano() <= self._tamano_maximo:
                            pares_cercanos.remove(mas_cercano[1][0])
                            pares_cercanos.remove(mas_cercano[1][1])
                            return ((mas_cercano[1][0], mas_cercano[1][1]), pares_cercanos, mas_cercano[0])
                    punto_medio = get_punto_medio(pares_cercanos[1])
                    punto_mas_cercano = Punto.get_punto_mas_cercano(punto_medio, pares_cercanos[1])

        
        def encontrar_par_raro(lista: List[Punto]) -> Tuple[self._tupla_puntos_type, List[Punto], bool]:
            pares_cercanos: List[self._tupla_puntos_type, List[Punto], float] = list(Punto.pares_cercanos(lista))

            print(pares_cercanos[0][0].get_tamano(),pares_cercanos[0][1].get_tamano(), self._tamano_maximo)
            print(pares_cercanos[0][0].get(), pares_cercanos[0][1].get())

            if pares_cercanos[0][0].get_tamano() + pares_cercanos[0][1].get_tamano() > self._tamano_maximo:
                R: bool = False
                L: bool = False
                if(pares_cercanos[0][0].get_tamano() <  pares_cercanos[0][1].get_tamano()):
                    punto_mayor_tamano = pares_cercanos[0][0]
                    resto = pares_cercanos[0][1].to_list()
                    L = True
                else:
                    punto_mayor_tamano = pares_cercanos[0][1]
                    resto = pares_cercanos[0][0].to_list()
                    R = True
                punto_mas_cercano, distancia = Punto.get_punto_mas_cercano(punto_mayor_tamano, resto)
                print('resto')
                del resto[punto_mas_cercano.get_index()]
                print(punto_mas_cercano.get_index())
                for i in resto:
                    print(i)
                print('punto cercano', punto_mas_cercano)
                if len(resto) > 1:
                    punto_medio_resto: Punto = Punto.get_punto_medio(list(resto), True)
                else:
                    punto_medio_resto: Punto = resto[0]
                pares_cercanos[1].append(punto_medio_resto)
                if L:
                    tupla = (pares_cercanos[0][0],punto_mas_cercano)
                    pares_cercanos[0] = tupla
                else:
                    tupla = (punto_mas_cercano, pares_cercanos[0][1])
                    pares_cercanos[0] = tupla
                return (pares_cercanos[0], pares_cercanos[1], False)

            else:
                return (pares_cercanos[0], pares_cercanos[1], True)
        

        while(self._clusters_actuales > len(self._domiciliarios)):
            print("------------", self._clusters_actuales)
            #print(self._clusters_actuales)
            try:
                #pares_cercanos = encontrar_par_raro(self._clusters)
                pares_cercanos: Tuple[self._tupla_puntos_type, List[Punto], float] = Punto.pares_cercanos(self._clusters)
                self._clusters = pares_cercanos[1]
                punto_medio: Punto = Punto.get_punto_medio(list(pares_cercanos[0]), True)
                if punto_medio.get_tamano() >= len(self._domiciliarios):
                    self._clusters_completos.append(punto_medio)
                else:
                    self._clusters.append(punto_medio)
                #self._clusters.append(punto_medio)
                #if(pares_cercanos[2]):
                self._clusters_actuales -= 1
            except Exception as e:
                print(e)


    def __asignar_domiciliarios(self) -> None:
        pass

    def __response(self) -> List[Punto]:
        return self._clusters + self._clusters_completos