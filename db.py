from lib2to3.pgen2 import driver
from msilib.schema import Class
from neo4j import GraphDatabase


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


