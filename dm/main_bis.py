import create_graphs as cg
import search
import timeit
import networkx as nx
import matplotlib.pyplot as plt

# main pour utliser le fichier search

algo_informe = [search.greedy_best_first_graph_search]

algo_non_informe = [search.depth_first_graph_search, search.uniform_cost_search, search.breadth_first_graph_search, search.astar_search, search.recursive_best_first_search]


G = cg.create_graph("sgb128_dist.txt", limit=300)
nx.draw(G)
plt.draw()
plt.show()
nx.write_gml(G, "sgb128_dist-300.gml")

name = cg.get_name()
dico = cg.graph_to_dict(G)

probleme = search.GraphProblem(0, 41, search.UndirectedGraph(dico))

for function in algo_non_informe:
    start_time = timeit.default_timer()
    result = function(probleme)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print(f"{function.__name__}: {execution_time} seconds")


for function in algo_informe:
    start_time = timeit.default_timer()
    result = function(probleme, search.GraphProblem.h)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print(f"{function.__name__}: {execution_time} seconds")

