# %%
from xml import dom
from models.Punto import Punto
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
from services.Generador import Generador
from services.AgglomerativeClustering import AgglomerativeClustering
from typing import Any, List, Dict

from matplotlib import pyplot as plt

from sys import stdin, stdout


def main():

    numero_domiciliarios: int = 5
    numero_puntos_entrega: int = 15
    generador: Generador = Generador(
        numero_domiciliarios, numero_puntos_entrega)

    datos: Dict[str, Any] = generador.run()

    domiciliarios: List[Domiciliario] = datos['domiciliarios']
    puntos_entrega: List[PuntoEntrega] = datos['puntos_entrega']

    puntos: List[Punto] = domiciliarios + puntos_entrega

    puntos_domiciliario_prueba = [
        Domiciliario(1, 1),
        Domiciliario(2.7, 10),
        Domiciliario(8, 10)
    ]

    puntos_entrega_prueba = [
        PuntoEntrega(1.4, 3),
        PuntoEntrega(3, 4),
        PuntoEntrega(4, 10),
        PuntoEntrega(1, 7),
        PuntoEntrega(1, 9),
        PuntoEntrega(7, 2),
        PuntoEntrega(7.2, 5),
        PuntoEntrega(6.5, 8)
    ]

    lista_completa_prueba = puntos_domiciliario_prueba + puntos_entrega_prueba

    """
    r = Punto.pares_cercanos(lista_completa_prueba)
    print(r[0][0])
    print(r[0][1])
    print(r[1])


    punto = (None, 999999999999999)
    for i in range(len(lista_completa_prueba)-1):
        for j in range(i + 1, len(lista_completa_prueba)):
            if Punto.distancia_entre_puntos(lista_completa_prueba[i], lista_completa_prueba[j]) < punto[1]:
                punto = ((lista_completa_prueba[i], lista_completa_prueba[j]), Punto.distancia_entre_puntos(lista_completa_prueba[i], lista_completa_prueba[j]))

    print(punto[0][0])
    print(punto[0][1])
    print(punto[1])
    """

    agglomerative_clustering = AgglomerativeClustering(puntos_domiciliario_prueba, puntos_entrega_prueba)

    agglomerative_clustering.run()
    

    for punto in domiciliarios:
        coordenadas = punto.get()
        plt.plot(coordenadas[0], coordenadas[1], marker="o", color="red")

    for punto in puntos_entrega:
        coordenadas = punto.get()
        plt.plot(coordenadas[0], coordenadas[1], marker="o", color="black")

    plt.show()


if __name__ == "__main__":
    main()

# %%