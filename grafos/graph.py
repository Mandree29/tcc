from pyvis.network import Network

def grafo():
    pagina ='grafo.html'
    g = Network()
    g.add_node(0)
    g.add_node(1)
    g.add_edge(0,1)
    g.show(pagina)
    return 'grafo.html'

def grafoPesquisaPorEntidade(lista:list):
    pagina = 'grafo.html'
    g = Network(width='500px', height='500px', notebook=True)
    g.add_nodes(lista[0])
    g.add_edge(lista[0][0], lista[0][1])
    g.add_edge(lista[0][0], lista[0][2])
    g.show(pagina)
    return None