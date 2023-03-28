from db import BD
import tratamento_json
from grafos.graph import *

def encontrando_vertices(frase:str):
    result_vertices = []
    if "Entity" in frase:
        result_vertices.append("Entity")

    if "File" in frase:
        result_vertices.append("File")

    if "Type" in frase:
        result_vertices.append("Type")
    return result_vertices

def encontrando_rel(frase:str):
    result_rel = []
    if "Pertence" in frase:
        result_rel.append("Pertence")
    if "É" in frase:
        result_rel.append("É")
    return result_rel



def Check_Controller(vertice:list, rel:list):

    if len(vertice) == 3 and len(rel) == 2:
        return check_tudo()

    elif len(vertice) == 1 and len(rel) == 0:
        if vertice[0] == "Entity":
            return grafoEntidade(checando_Entidade_semJson())
        elif vertice[0] == "File":
            return grafoFile(checando_file())
        elif vertice[0] == "Type":
            return grafoType(checando_Type())
        
    #primeiro caso de pesquisa (TUDO)
def check_tudo():
    bd = BD()
    return  bd.Query_tudo()
            
    #caso entity
def checando_Entidade():
    bd = BD()
    return tratamento_json.json_entidade(bd.Query_Entity())

def checando_Entidade_semJson():
    bd = BD()
    return bd.Query_Entity()

    #caso file
def checando_file():
    bd = BD()
    return bd.Query_File()

    #caso Type
def checando_Type():
    bd = BD()
    return bd.Query_Type()


