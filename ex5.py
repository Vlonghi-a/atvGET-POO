from flask import Flask, request, jsonify

app = Flask(__name__)

funcionarios=[[0, "John", "Designer", 5000], [15, "Bob", "Programador", 17000], [1, "Anderson", "Programador", 100000]]

@app.route("/funcionarios")
def home():
    cargo=request.args.get("categoria")
    funcionariosEx=[]
    if cargo:
            for i in funcionarios:
                if i[2].lower() == cargo.lower():
                    result={
                    "id": i[0],
                    "nome": i[1],
                    "cargo": i[2],
                    "salario": i[3]
                    }
                    funcionariosEx.append(result)
            return jsonify(funcionariosEx)
    else:
        infoFuncionarios = {
                "1": {
                    "id": funcionarios[0][0],
                    "nome": funcionarios[0][1],
                    "cargo": funcionarios[0][2],
                    "salario": funcionarios[0][3]
                },
                "2": {
                    "id": funcionarios[1][0],
                    "nome": funcionarios[1][1],
                    "cargo": funcionarios[1][2],
                    "salario": funcionarios[1][3]
                },
                "3": {
                    "id": funcionarios[2][0],
                    "nome": funcionarios[2][1],
                    "cargo": funcionarios[2][2],
                    "salario": funcionarios[2][3]
                }
                
            }
        return jsonify(infoFuncionarios)


@app.route("/funcionarios/<int:id>")
def busca_id(id):
    for i in funcionarios:
        if i[0] == id:
            result=i
    return result

app.run(debug=True)