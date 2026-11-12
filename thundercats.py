"""
PONTIFICIA UNIVERSIDAD JAVERIANA
FACULTAD DE INGENIERÍA Y CIENCIAS
ÁRBOLES Y GRÁFOS 2026-2
PROFESORES: CARLOS RAMÍREZ R. Y CARLOS DELGADO S.
PROYECTO FINAL DEL CURSO
----
Realizado por
Nicolas Carrillo Romo
Nicolle Ureña de Garcia
"""

from sys import stdin
from heapq import heappush,heappop
INF = float('inf')

def dijkstra(G, s):
    dist = [INF for _ in range(len(G))]
    dist[s] = 0
    pqueue = list()
    heappush(pqueue, (dist[s], s))
    while len(pqueue) != 0:
        du, u = heappop(pqueue)
        if dist[u] == du:
            for v, duv in G[u]:
                if du + duv < dist[v]:
                    dist[v] = du + duv
                    heappush(pqueue, (dist[v], v))
    return dist

def calcTime(distVector, speedMut):
    time = [-1 for _ in range(len(distVector))]
    for i in range(len(distVector)):
        time[i] = (distVector[i]/speedMut)
    return time

def minMaxSpeed(G, exits, vMut, iniLion, iniMut):
    ans = -1
    dMut = dijkstra(G, iniMut)
    tMut = calcTime(dMut, vMut)
    ## Hasta aqui tenemos 2 vectores dMut y tMut, cada uno contiene la distancia y tiempo de llegada
    ## de los mutantes hacia todos los nodos
    return ans

def main():
    T = int(stdin.readline())
    while T:
        N,M,K,V = map(int,stdin.readline().split())
        intersc = [[] for i in range(N+1)]
        exits = []
        while M:
            A,B,D = map(int,stdin.readline().split())
            D = (D*100)/1000
            intersc[A].append((B,D))
            intersc[B].append((A,D))
            M -= 1
        S, R = map(int,stdin.readline().split())
        e = map(int,stdin.readline().split())
        for i in e:
            exits.append(i)
        T -= 1
        if (R in exits and len(exits)==1) or S == R:
            ans = -1
        elif S in exits:
            ans = 0
        else:
            ans = minMaxSpeed(intersc, exits, V, S, R)
        if ans >= 0:
            print(f"Lion-O can escape at a speed of {ans:.6f} km/h!")
        else:
            print("Mumm-Ra captures Lion-O!")
main()