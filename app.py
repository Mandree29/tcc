
from graph import grafo
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pesquisa", methods=['GET'])
def resultado():
    vertice = request.args.get('vertice')
    rel = request.args.get('relacionamento')
    prop = request.args.get('prop')
    val = request.args.get('val')
    print(type(vertice))
    print(type(prop))
    print(type(val))
    print(type(rel))

    grafico = grafo()

    


    return render_template("resultado.html", vertice=vertice, rel=rel, prop=prop, val=val, grafico = grafico)




if __name__ == "__main__":
    app.run()
