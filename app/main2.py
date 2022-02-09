from math import ceil, sqrt, inf
from matplotlib import pyplot as plt
from services.Generador import Generador
from models.Punto import Punto
from models.Domiciliario import Domiciliario
from models.PuntoEntrega import PuntoEntrega
from typing import Any, List, Dict
import random

"""
Calcula los centroides para una lista de clusters

Complejidad: O(K*P)
K = clústers
P = total de puntos

Returns:
    Lista de centroides y lista de tamaño de los clusters
"""


def get_centroids(clusters):
    centroids = [0] * len(clusters)
    sizes = [0] * len(clusters)
    for i in range(len(clusters)):  # O(K)
        x = 0
        y = 0
        N = len(clusters[i])
        for point in clusters[i]:  # O(P_i)
            x += point[0]
            y += point[1]
        centroids[i] = (x/N, y/N)
        sizes[i] = N
    return centroids, sizes


"""
Calcula el centroide más cercano para cada uno de los centroides.

Complejidad: O(K^2)
K = clústers
"""


def get_closest_cluster(centroids, sizes, max_cluster_size):
    distances = [0 for x in centroids]
    for i in range(len(distances)):  # O(K)
        menor = inf
        k = 0
        for j in range(len(distances)):  # O(K)
            if j == i:
                continue
            else:
                dist = sqrt((centroids[i][0] - centroids[j][0])
                            ** 2 + (centroids[i][1] - centroids[j][1])**2)
                # and sizes[i] + sizes[j] <= max_cluster_size
                if dist <= menor:
                    menor = dist
                    k = j
        distances[i] = k
    return distances


"""
Función principal, retorna una lista donde cada elemento es un clúster.

Complejidad: O(K*P + K^2 + )

"""


def get_clusters(points: list, K: int):
    max_cluster_size = ceil(len(points)/K)

    clusters = points
    if len(clusters) <= K:
        return points

    # O(K*P)
    centroids, sizes = get_centroids(clusters)
    # O(K^2)
    closest_cluster = get_closest_cluster(centroids, sizes, max_cluster_size)
    new_clusters = []

    merged = set()
    for i in range(len(centroids)):  # O(N)
        a = centroids[i]
        b = centroids[closest_cluster[i]]
        if a not in merged and b not in merged:
            new_clusters.append(clusters[i] +
                                clusters[closest_cluster[i]])  # O(1) amortizado
            merged.add(a)  # O(1)
            merged.add(b)  # O(1)
        elif a not in merged and b in merged:
            new_clusters.append(clusters[i])
    return get_clusters(new_clusters, K)


def plot_clusters(clusters):
    for cluster in clusters:
        x = [c[0] for c in cluster]
        y = [c[1] for c in cluster]
        plt.scatter(x, y)
    plt.show()

numero_domiciliarios: int = 10
numero_puntos_entrega: int = 100
generador: Generador = Generador(numero_domiciliarios, numero_puntos_entrega)

datos: Dict[str, Any] = generador.run()

domiciliarios: List[Domiciliario] = datos['domiciliarios']
puntos_entrega: List[PuntoEntrega] = datos['puntos_entrega']

puntos: List[Punto] = domiciliarios + puntos_entrega

puntos_x_y = map(lambda x: [x.get()], puntos_entrega)

points = list(puntos_x_y)

plot_clusters(get_clusters(points, numero_domiciliarios))