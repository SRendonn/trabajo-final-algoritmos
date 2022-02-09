from xml import dom
from models.Punto import Punto
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
from services.Generador import Generador
from services.AgglomerativeClustering import AgglomerativeClustering
from typing import Any, List, Dict
import random

from matplotlib import pyplot as plt

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

