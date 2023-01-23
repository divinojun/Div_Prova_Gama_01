"""
curl -X POST 'http://localhost:5000/soma' -H 'Content-type:
application/json' -d '{"x": 1, "y"; 2}'
A API /soma irá receber o valor x e somar com o valor y e retorná-lo em JSON no
seguinte formato:
{
"resultado": <valor do resultado>
}
Para o exemplo, acima iremos retornar:
{
"resultado": 3
}
Os valores de entrada, x e y são obrigatórios e devem ser números.
"""

print('-=-=-=-=-=-=-=-=PROVA DA GAMA-=-=-=-=-=-=-=-=')

from flask import Flask, request

app = Flask(__name__)

@app.post('/soma')
def soma():
    number = request.get_json()
    total = number.get("x") + number.get("y")
    print(f"Resultado {total}")
    return {"Resultado: ":total}
    

if __name__ == '__main__':
    app.run(debug=True)