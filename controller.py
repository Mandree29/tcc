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

    if len(vertice) == 3 and len(rel) == 2:  # caso em que está tudo preenchido 3 vertices e 2 relacionamentos
        return check_tudo()

    elif len(vertice) == 1 and len(rel) == 0: # caso em que a lista de vertice está com tamanho 1 (apenas um valor selecionado) e 0 de relacionamentos
        if vertice[0] == "Entity":            # apenas o valor entidade
            return grafoEntidade()            
        elif vertice[0] == "File":            # apenas o valor file
            return  grafoFile()  
        elif vertice[0] == "Type":            # apenas o valor Type
            return grafoType()

    elif len(vertice) == 2 and len(rel) == 0: # caso em que a lista de vertice está com tamnho 2 (dois tipos de vertices selecionados) e 0 de relacionamentos
        if  "Type" not in vertice:            # caso seleção dos vertices Entity e File
            return grafoEntidadeFile_semRel()  
        elif "File" not in vertice:           # caso de seleção do vertices Entidade e Type
            return grafoEntidadeType_semRel()
        elif "Entity" not in vertice:         # caso de seleção dos vertices File Type
            return grafoFileType_semRel()

    elif len(vertice) == 3 and len(rel) == 0: # caso em que a lista vertice está com tamanho 3 (todos os nós selecionados) e 0 de relacionamentos
        return grafoTodosVertices_semRel()
        
    #primeiro caso de pesquisa (TUDO)
def check_tudo():
    bd = BD()
    return  bd.Query_tudo()
            
    #caso entity
def checando_Entidade(): # função utilizada para alimentar a pesquisa automática da barra de pesquisa NÃO PODE APAGAR
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


