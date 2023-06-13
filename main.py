import matplotlib.pyplot as plt
import networkx as nx
from statistics import mean




def read_dataset(path, delimiter=" "):
    # Reading given dataset for drawing graph
    g = nx.read_edgelist(path, create_using=nx.Graph(), nodetype=int, delimiter=delimiter)
    return g


def Erdos_Renyi(n,p):
    #Creating Erdos_Renyi network
    g = nx.erdos_renyi_graph(n, p, seed=None, directed=False)
    return g

def local_clustering_coefficient(g):
    #Calculating each node's LCC
    lcc = nx.clustering(g)
    return lcc

def graph_degrees(g):
    # Calculating each node's degree
    degrees = {node: val for (node, val) in g.degree()}
    return degrees

def group(key, value, iterable):
    groups = {}
    for i in iterable:
        groups[key(i)] = groups.get(key(i), []) + [value(i)]
    return groups


def main():
    #barabasi 3.2
    #p = <k>(n-1)
    #n = 500, <k> = 0.8, 1, 8, p(a)=399.2 p(b)=499 p(c)=3992
    ER = Erdos_Renyi(500,399.2)
    nx.draw(ER, with_labels=False, node_size=15, width=0.009, node_color='blue')
    plt.show()



    #first part
    g = read_dataset("Twitter_edges.txt", " ")
    print(nx.info(g))
    nx.draw(g, with_labels=False, node_size=15,width=0.2, node_color='blue')
    plt.show()


    #second part
    n = len(g.nodes)
    ERG = Erdos_Renyi(n,0.1)
    nx.draw(ERG, with_labels=False, node_size=15,width=0.006, node_color='blue')
    plt.show()

    #third part
    lcc = local_clustering_coefficient(g
    degrees = graph_degrees(g)
    print("Degrees of each node is = ",degrees)
    print ("Local Clustering Coefficient of each node is = ",lcc)

    cs_by_k = [(k, lcc[node]) for node, k in degrees.items()]

    z = group(lambda z: z[0], lambda z: z[1], cs_by_k)
    c_by_k = [(k, mean(cs)) for k, cs in z.items()]

    ks, cs = zip(*c_by_k)
    print(c_by_k)
    print(ks, cs)
    x = ks
    y = cs


    plt.scatter(x, y, c="r", alpha=0.4, marker='.', label="Twitter")
    plt.xlim()
    plt.ylim()
    plt.xlabel("k")
    plt.ylabel("C(k)")
    plt.title("Clustering Coefficient")
    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    main()
