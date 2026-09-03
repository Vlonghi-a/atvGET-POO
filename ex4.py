from flask import Flask, request, jsonify

app = Flask(__name__)

musicas=[[0, "Faroeste Caboclo", "Legiao Urbana", 1987], [7, "Tempo Perdido", "Legiao Urbana", 1986]]

@app.route("/musicas")
def home():
    artista=request.args.get("artista")
    artistasEx=[]
    if artista:
            for i in musicas:
                if i[2].lower() == artista.lower():
                    result={
                    "id": i[0],
                    "nome": i[1],
                    "artista": i[2],
                    "ano": i[3]
                    }
                    artistasEx.append(result)
            return jsonify(artistasEx)
    else:
        infoMusicas = {
                "1": {
                    "id": musicas[0][0],
                    "nome": musicas[0][1],
                    "artista": musicas[0][2],
                    "ano": musicas[0][3]
                },
                "2": {
                    "id": musicas[1][0],
                    "nome": musicas[1][1],
                    "artista": musicas[1][2],
                    "ano": musicas[1][3]
                }
            }
        return jsonify(infoMusicas)


@app.route("/musicas/<int:id>")
def busca_id(id):
    for i in musicas:
        if i[0] == id:
            result=i
    return result

app.run(debug=True)