from flask import Flask, request

app = Flask(__name__)

memoria = {'contador': 0}

@app.post('/contador')
def novo_valor():
    value = request.get_json('número')
    memoria["counter"] = value['número']
    return "", 201

@app.get('/contador')
def get_valor():
    return {'número': memoria['contador']}, 200

@app.put('/contador/incrementa')
def incrementa():
    memoria["contador"] += 1
    return '', 202

@app.delete('/contador')
def delete():
    memoria['contador'] = 0
    return '', 202


if __name__ == '__main__':
    app.run(debug=True)