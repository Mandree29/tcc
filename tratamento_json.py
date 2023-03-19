import json


def json_entidade(resutado_parcial:list):
    resultado_final = []
    for x in resutado_parcial:
        x = {'nome': x}
        resultado_final.append(x)
    resultado_final = json.dumps(resultado_final)
    return resultado_final
