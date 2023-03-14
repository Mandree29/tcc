from pyvis.network import Network

def grafo():
    pagina ='basic.html'
    g = Network()
    g.add_node(0)
    g.add_node(1)
    g.add_edge(0,1)
    g.show(pagina)
    return 'basic.html'
