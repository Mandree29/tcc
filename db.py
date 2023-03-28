from lib2to3.pgen2 import driver
from msilib.schema import Class
from neo4j import GraphDatabase
import json


class BD:
    def __init__(self):
        self.driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j","dede182"))
        self.session = self.driver.session()

    def Query_tudo(self):
        lista = []
        query = "match (n) return n.name as objeto"
        results = self.session.run(query)
        for result in results:
            linha_obj = []
            linha_obj.append(result['objeto'])
            lista.append(linha_obj)
        self.session.close()
        return lista
    
    def Query_Entity(self):
        lista = []
        query = "match (e:Entity) return e.name as objeto"
        results = self.session.run(query)
        for result in results:
            lista.append(result['objeto'])
        self.session.close()
        return lista

    def Query_File(self):
        lista = []
        query = "match (f:File) return f.name as objeto"
        results = self.session.run(query)
        for result in results:
            lista.append(result['objeto'])
        self.session.close()
        return lista

    def Query_Type(self):
        lista = []
        query = "match (t:Type) return t.name as objeto"
        results = self.session.run(query)
        for result in results:
            lista.append(result['objeto'])
        self.session.close()
        return lista
    
# realizar a pesquisa para retornar todos os nomes dos vétices para ser utilizado na barra de pesquisa

# pesquisa por cada entidade


    def Query_PorEntidade(self, entidade:str):
        lista = []
        query = "match (f:File)<-[:Pertence]-(n:Entity)-[:`É`]->(t:Type) where n.name ='{}' return [n.name, f.name, t.name] as objeto".format(entidade)
        results = self.session.run(query)
        for result in results:
            lista.append(result['objeto'])
        self.session.close()
        return lista
