
from grafos.graph import grafo
from tratemento_string import *
from flask import Flask, render_template, request
import json
from flask import request

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
    json.dumps(ck) 

    return render_template("index.html")

@app.route("/pesquisa/nomes", methods=['GET'])
def nomes_vertices():
    nomes = checando_Entidade()
    return nomes


@app.route("/pesquisa2", methods=["GET"])
def nome_entidade():
    ent = request.args.get('val')
    print(ent)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
