from flask import Flask, request, jsonify

app = Flask(__name__)

produtos=[[0, "Abacate", 14.99, "Frutas"], [20, "Bomba de Hidrogenio", 15.99, "Informatica"], [50, "Caco de Vidro", 16.99, "Informatica"]]

@app.route("/produtos")
def home():
    categoria=request.args.get("categoria")
    produtosEx=[]
    if categoria:
            for i in produtos:
                if i[3].lower() == categoria.lower():
                    result={
                    "id": i[0],
                    "nome": i[1],
                    "preco": i[2],
                    "categoria": i[3]
                    }
                    produtosEx.append(result)
            return jsonify(produtosEx)
    else:
        infoProdutos = {
                "1": {
                    "id": produtos[0][0],
                    "nome": produtos[0][1],
                    "curso": produtos[0][2],
                    "idade": produtos[0][3]
                },
                "2": {
                    "id": produtos[1][0],
                    "nome": produtos[1][1],
                    "curso": produtos[1][2],
                    "idade": produtos[1][3]
                },
                "3": {
                    "id": produtos[2][0],
                    "nome": produtos[2][1],
                    "curso": produtos[2][2],
                    "idade": produtos[2][3]
                }
                
            }
        return jsonify(infoProdutos)


@app.route("/produtos/<int:id>")
def busca_id(id):
    for i in produtos:
        if i[0] == id:
            result=i
    return result

app.run(debug=True)