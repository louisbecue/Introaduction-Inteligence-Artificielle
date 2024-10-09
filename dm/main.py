import create_graphs as cg
import algo as algo
import timeit
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


#les différents alogorithme
algo_informe = [algo.greedy_best_first_graph_search, algo.astar_search, algo.recursive_best_first_search]
algo_non_informe = [algo.depth_first_graph_search, algo.uniform_cost_search, algo.breadth_first_graph_search]

#création du graphe
G = cg.create_graph("sgb128_dist.txt", limit=300)
nx.draw(G)
plt.draw()
plt.show()
nx.write_gml(G, "sgb128_dist-300.gml")

depth_first_graph_search = []
uniform_cost_search = []
breadth_first_graph_search = []
greedy_best_first_graph_search = []
astar_search = []
recursive_best_first_search = []

#test des algorithmes pour la ville 0 jusqu'aux ville 1 a 128
for i in range(128):
    #calcul du temps d'éxcécutio,
    start_time = timeit.default_timer()
    algo.depth_first_graph_search(G, 0, i)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    float(execution_time)
    depth_first_graph_search.append(execution_time)

    start_time = timeit.default_timer()
    algo.uniform_cost_search(G, 0, i)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    float(execution_time)
    uniform_cost_search.append(execution_time)

    start_time = timeit.default_timer()
    algo.breadth_first_graph_search(G, 0, i)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    float(execution_time)
    breadth_first_graph_search.append(execution_time)

    start_time = timeit.default_timer()
    algo.greedy_best_first_graph_search(G, 0, i, algo.heuristic)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    float(execution_time)
    greedy_best_first_graph_search.append(execution_time)

    start_time = timeit.default_timer()
    algo.astar_search(G, 0, i, algo.heuristic)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    float(execution_time)
    astar_search.append(execution_time)
     
    start_time = timeit.default_timer()
    algo.recursive_best_first_search(G, 0, i, algo.heuristic)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    float(execution_time)
    recursive_best_first_search.append(execution_time)


x = list(range(128))
y1 = depth_first_graph_search
y2 = uniform_cost_search
y3 = breadth_first_graph_search
y4 = greedy_best_first_graph_search
y5 = astar_search
y6 = recursive_best_first_search

all = [y1, y2, y3, y4, y5, y6]

# création de graphes grace matplolib
fig, ax = plt.subplots()
ax.plot(x, y1, "-.", label="depth_first_graph_search")
ax.plot(x, y2, "-.", label="uniform_cost_search")
ax.plot(x, y3, "-.",label="breadth_first_graph_search")
ax.plot(x, y4, "-.", label="greedy_best_first_graph_search")
ax.plot(x, y5,"-.", label="astar_search")
ax.plot(x, y6, "-.",label="recursive_best_first_search")
ax.legend()
ax.set_ylabel("Temps (s)")
ax.set_xlabel("Ville")
plt.savefig('all_search.png')
plt.show()

#graphe pur chaque algo
fig, ax = plt.subplots()
ax.plot(x, y1, "-.")
ax.legend("depth_first_graph_search")
ax.set_ylabel("Temps (s)")
ax.set_xlabel("Ville")
plt.savefig('depth_first_graph_search.png')
plt.show()

fig, ax = plt.subplots()
ax.plot(x, y2, "-.")
ax.legend("uniform_cost_search")
ax.set_ylabel("Temps (s)")
ax.set_xlabel("Ville")
plt.savefig('uniform_cost_search.png')
plt.show()

fig, ax = plt.subplots()
ax.plot(x, y3, "-.")
ax.legend("breadth_first_graph_search")
ax.set_ylabel("Temps (s)")
ax.set_xlabel("Ville")
plt.savefig('breadth_first_graph_search.png')
plt.show()

fig, ax = plt.subplots()
ax.plot(x, y4, "-.")
ax.legend("greedy_best_first_graph_search")
ax.set_ylabel("Temps (s)")
ax.set_xlabel("Ville")
plt.savefig('greedy_best_first_graph_search.png')
plt.show()

fig, ax = plt.subplots()
ax.plot(x, y5, "-.")
ax.legend("astar_search")
ax.set_ylabel("Temps (s)")
ax.set_xlabel("Ville")
plt.savefig('astar_search.png')
plt.show()

fig, ax = plt.subplots()
ax.plot(x, y5, "-.")
ax.legend("recursive_best_first_search")
ax.set_ylabel("Temps (s)")
ax.set_xlabel("Ville")
plt.savefig('recursive_best_first_search.png')
plt.show()

#affichage des valeurs moyenne
for algo in all:
    print(f"{algo.__ne__}: temps moyen = {sum(algo)/len(algo)} seconds, temps maximum = {max(algo)} seconds, temps minimum = {min(algo)} seconds")