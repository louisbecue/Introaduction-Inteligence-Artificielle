import networkx as nx
import matplotlib.pyplot as plt
import search as se


# Fichiers de graphes sont ici : https://people.math.sc.edu/Burkardt/datasets/cities/cities.html


def create_graph(filename, limit=None):
    G = nx.Graph()
    source = 0 
    nb_nodes = None
    with open(filename) as f:
        for line in f:
            if not line.startswith("#"):
                dists = [int(i) for i in line.strip().split()]
                if nb_nodes == None:
                    nb_nodes = len(dists)
                if len(dists) != nb_nodes:
                    print("erreur", line)
                    continue
                # Je suppose que c'est bon
                for target, dist in enumerate(dists):
                    if source != target and (limit == None or limit > dist):
                        G.add_edge(source, target, weight=dist)
                source += 1
    return G


#transforme un graphe en dictionnaire
def graph_to_dict(graphe):
    res = nx.to_dict_of_dicts(graphe)
    for (node, dico) in res.items():
        for (v, i) in dico.items():
            res[node][v] = i['weight']
    return res
                    
#obtenier les position sous la forme d'un dictionnaire avec les coordonnées
def get_positon():
    res = {}
    i = 0
    with open("sgb128_xy.txt") as f:
        for line in f:
            if not line.startswith("#"):
                i += 1
                dists = [float(i) for i in line.strip().split()]
                res[i] = dists
    return res

# dictionnaires des noms des ville
def get_name():
    res = {}
    i = 0
    with open("sgb128_name.txt") as f:
        for line in f:
            if not line.startswith("#"):
                i += 1
                dists = [str(i) for i in line.strip().split()]
                res[i] = dists[0]
    return res

# pour rennomer les villes ( ne marche pas totalement)
def rename(dico, name):
    res = {}
    for i in range(1, len(dico)):
        tmp = {}
        for y in range(len(dico[i])):
            tmp = dico[i][i] 
        res[name[i]] = tmp
    return res