
from templates.graph import grafo
from tratemento_string import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pesquisa", methods=['GET'])
def resultado():
    vertice = request.args.get('vertice')
    vertice = encontrando_vertices(vertice)
    rel = request.args.get('relacionamento')
    rel = encontrando_rel(rel)
    #prop = request.args.get('prop')
    #val = request.args.get('val')
    print(vertice)
    print(rel)

    ck = Check_Controller(vertice, rel)
    print(ck)


 



    # if len(lista_rel) == 0 and len(lista_vert) == 1:
    #     if lista_vert[0] == "Entity":
    #         pass

    # grafo()
    #return render_template("resultado.html",vertice=vertice, rel=rel, prop=prop, val=val)
    #return render_template("basic.html")
    #vertice=vertice, rel=rel, prop=prop, val=val, grafico = grafico

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
