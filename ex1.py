from flask import Flask, request, jsonify

app = Flask(__name__)

filmes=[[1, "Matrix", "Lilly e Lana Wachowski", 1999], [10, "O Chamado", "Gore Verbinski", 2002]]

@app.route("/")
def home():
    cartaz = {
        "1": {
            "id": filmes[0][0],
            "nome": filmes[0][1],
            "diretor": filmes[0][2],
            "ano": filmes[0][3]
        },
        "2": {
            "id": filmes[1][0],
            "nome": filmes[1][1],
            "diretor": filmes[1][2],
            "ano": filmes[1][3]
        }
    }
    return jsonify(cartaz)

@app.route("/filmes/<int:id>")
def busca_id(id):
    for i in filmes:
        if i[0] == id:
            result=i
    return result

@app.route("/filmes")
def busca_nome():
    nome=request.args.get("nome")
    for i in filmes:
        if i[1].lower() == nome.lower():
            result={
                        "id": i[0],
                        "nome": i[1],
                        "diretor": i[2],
                        "ano": i[3]
                    }
    return jsonify(result)

app.run(debug=True)