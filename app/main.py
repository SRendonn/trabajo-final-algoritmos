from xml import dom
from models.Punto import Punto
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
from services.Generador import Generador
from services.AgglomerativeClustering import AgglomerativeClustering
from typing import Any, List, Dict
import random

from matplotlib import pyplot as plt

from sys import stdin, stdout

def graficar(punto: Punto, color):
    for sub_punto in punto.get_conexiones():
        graficar(sub_punto, color)

    if len(punto.get_conexiones()) == 0:
        plt.plot(punto.get_x(), punto.get_y(), marker="o", color=color)


def main():

    numero_domiciliarios: int = 10
    numero_puntos_entrega: int = 100
    generador: Generador = Generador(numero_domiciliarios, numero_puntos_entrega)

    datos: Dict[str, Any] = generador.run()

    domiciliarios: List[Domiciliario] = datos['domiciliarios']
    puntos_entrega: List[PuntoEntrega] = datos['puntos_entrega']

    puntos: List[Punto] = domiciliarios + puntos_entrega


    #puntos_x_y = map(lambda x: [x.get()], puntos_entrega)

    #print(list(puntos_x_y))

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

    agglomerative_clustering = AgglomerativeClustering(domiciliarios, puntos_entrega)

    clusters = agglomerative_clustering.run()
        

    plt.xlim(0, 11)
    plt.ylim(0, 11)
    plt.gca().set_aspect('equal', adjustable='box')

    for punto in clusters:
        r = random.random()
        b = random.random()
        g = random.random()

        color = (r, g, b)

        graficar(punto,color)
    

    for punto in domiciliarios:
       coordenadas = punto.get()
       plt.plot(coordenadas[0], coordenadas[1], marker="X", color="black")

    domiciliarios_por_asignar = domiciliarios[:]

    while len(domiciliarios_por_asignar) > 0:
        distancias = [[x, i, Punto.get_punto_mas_cercano(x, clusters)] for i,x in enumerate(domiciliarios_por_asignar)]
        maximo_minimo = max(distancias, key=lambda x: x[2][1])

        x_values = [maximo_minimo[0].get_x(), maximo_minimo[2][0].get_x()]
        y_values = [maximo_minimo[0].get_y(), maximo_minimo[2][0].get_y()]
        plt.plot(x_values, y_values, color="black")

        plt.plot(maximo_minimo[2][0].get_x(), maximo_minimo[2][0].get_y(), marker="*", color='black')

        del domiciliarios_por_asignar[maximo_minimo[1]]
        del clusters[maximo_minimo[2][0].get_index()]

    plt.show()


if __name__ == "__main__":
    main()

