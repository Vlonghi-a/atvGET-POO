from flask import Flask, request, jsonify

app = Flask(__name__)

alunos=[[1, "Joao", "TI", 15], [3, "Carlos", "TI", 14], [5, "Pedro", "MA", 17]]

@app.route("/alunos")
def home():
    nome=request.args.get("nome")
    if nome:
            for i in alunos:
                if i[1].lower() == nome.lower():
                    result={
                    "id": i[0],
                    "nome": i[1],
                    "curso": i[2],
                    "idade": i[3]
                    }
            return jsonify(result)
    else:
        infoAlunos = {
                "1": {
                    "id": infoAlunos[0][0],
                    "nome": infoAlunos[0][1],
                    "curso": infoAlunos[0][2],
                    "idade": infoAlunos[0][3]
                },
                "2": {
                    "id": infoAlunos[1][0],
                    "nome": infoAlunos[1][1],
                    "curso": infoAlunos[1][2],
                    "idade": infoAlunos[1][3]
                },
                "3": {
                    "id": infoAlunos[2][0],
                    "nome": infoAlunos[2][1],
                    "curso": infoAlunos[2][2],
                    "idade": infoAlunos[2][3]
                }
                
            }
        return jsonify(infoAlunos)


@app.route("/alunos/<int:id>")
def busca_id(id):
    for i in alunos:
        if i[0] == id:
            result=i
    return result

app.run(debug=True)