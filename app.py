
from grafos.graph import grafoPesquisaPorEntidade, grafoTudo
from controller import *
from flask import Flask, render_template, request
import json
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    grafoTudo()
    return render_template("index.html")

@app.route("/pesquisa", methods=['GET'])
def resultado():
    vertice = request.args.get('vertice')
    vertice = encontrando_vertices(vertice)
    rel = request.args.get('relacionamento')
    rel = encontrando_rel(rel)
    print(vertice)
    print(rel)

    Check_Controller(vertice, rel) 

    return render_template("index.html")

@app.route("/pesquisa/nomes", methods=['GET'])
def nomes_vertices():
    nomes = checando_Entidade()
    return nomes


@app.route("/pesquisa2", methods=["GET"])
def nome_entidade():
    ent = request.args.get('val')
    grafoPesquisaPorEntidade(ent)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
