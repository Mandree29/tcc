from pyvis.network import Network
import sys
sys.path.append('..')
from db import *


def grafoEntidade(): #metodo utilizado quando a escolha dos vertices tiver tamanho 1 (apenas Entidade) e sem nenhum relacionamento
    pagina = 'grafo.html'
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista = bd.Query_Entity()
    for n in lista:
        g.add_node(n, color="purple")
    g.show(pagina)
    return None


def grafoFile(): # metodo acionado quando a escolha dos vertices tiver tamanho 1 (apenas o file selecionado) e relacionamento tamanho 0 (sem relacionamento)
    pagina = 'grafo.html'
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista = bd.Query_File()
    for n in lista:
        g.add_node(n, color="blue")
    g.show(pagina)
    return None

def grafoType(): # metodo acionado quando a escolha dos vertices tiver tamanho 1 (apenas o type selecinado) e o relacionamento tiver tamnho 0 (sem relacionamento)
    pagina = 'grafo.html'
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista = bd.Query_Type()
    for n in lista:
        g.add_node(n, color="red")
    g.show(pagina)
    return None

def grafoEntidadeFile_semRel(): # Método acionado quando a ecolha dos vertices está com tamanho 2 (selecionado Entity e File) e o relacionamento tiver tamanho 0, ou seja nada selecionado
    pagina = "grafo.html"
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista1 = bd.Query_Entity()
    bd = BD()                  # tive que estanciar de novo porque cada metodo fecha a conexão (sessão com o banco de dados)
    lista2 = bd.Query_File()
    for n in lista1:
        g.add_node(n, color="purple")
    for n in lista2:
        g.add_node(n, color="blue")
    g.show(pagina)
    return None

def grafoEntidadeType_semRel():
    pagina = "grafo.html"
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista1 = bd.Query_Entity()
    bd = BD()                  # tive que estanciar de novo porque cada metodo fecha a conexão (sessão com o banco de dados)
    lista2 = bd.Query_Type()
    for n in lista1:
        g.add_node(n, color="purple")
    for n in lista2:
        g.add_node(n, color="red")
    g.show(pagina)
    return None

def grafoFileType_semRel():
    pagina = "grafo.html"
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista1 = bd.Query_File()
    bd = BD()                  # tive que estanciar de novo porque cada metodo fecha a conexão (sessão com o banco de dados)
    lista2 = bd.Query_Type()
    for n in lista1:
        g.add_node(n, color="blue")
    for n in lista2:
        g.add_node(n, color="red")
    g.show(pagina)
    return None

def grafoTodosVertices_semRel(): # Função utilizada quando o vértice está com o tamanho 3 (todos os vértices selecionados) e relacionamento tamanho 0 (nada selecionado)
    pagina = "grafo.html"
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista1 = bd.Query_Entity()
    bd = BD()                  # tive que estanciar de novo porque cada metodo fecha a conexão (sessão com o banco de dados)
    lista2 = bd.Query_File()
    bd = BD()                  # tive que estanciar de novo porque cada metodo fecha a conexão (sessão com o banco de dados)
    lista3 = bd.Query_Type()
    for n in lista1:
        g.add_node(n, color="purple")
    for n in lista2:
        g.add_node(n, color="blue")
    for n in lista3:
        g.add_node(n, color="red")
    g.show(pagina)
    return None


def grafoPesquisaPorEntidade(entidade:str): # geração de grafo para pesquisa individuais de entidade na barra de pesquisa
    pagina = 'grafo.html'
    g = Network(width='500px', height='500px', notebook=True)
    bd = BD()
    lista = bd.Query_PorEntidade(entidade)
    g.add_node(lista[0][0], color='purple')
    g.add_node(lista[0][1], color='blue')
    g.add_node(lista[0][2], color='red')
    #adicionando a relação entre os nós
    g.add_edge(lista[0][0], lista[0][1], title="pertence", color='blue', arrowStrikethrough=True)
    g.add_edge(lista[0][0], lista[0][2], title="é", color='red', arrowStrikethrough=True)
    g.show(pagina)
    return None


