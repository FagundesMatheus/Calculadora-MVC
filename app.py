from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from model import resolver

#CONTROLLER
app = Flask(__name__)
CORS(app, origins=["http://localhost:5000"])
@app.route('/')
def calculadora():
    return render_template('calculadora.html')

@app.route('/', methods=['POST'])
def calculadora_post():
    print('aaaa')
    content = request.json
    resposta = resolver(content['expressao'])
    return jsonify({"resposta": resposta})


if __name__ == '__main__':
    app.run()
