# retornos por URI
# necessário instalação do Postman
# Fabio Santos


# versão 1
from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def ola():
  return 'Hello, word'


if __name__=="__main__":
  app.run()



versão 2 
# com filtro de número inteiro no  app.rout 
from flask import Flask
app = Flask(__name__)


@app.route("/<int:numero>", methods=['GET','POST'])
def ola(numero):
  return 'Olá mundo {}'.format(numero)


# pode alterar nome da variavel para o nome do arquivo .py
if __name__=="__main__":
  app.run(debug=True)


# versão 3 
# Voltando soma em formato Json
from flask import Flask, jsonify, request
import json


app = Flask(__name__)


@app.route('/<int:id>')
def pessoa(id):
  soma = 1 + id
  return jsonify({'id':id, 'nome':'Fabio Santos', 'profissao': 'Desenvolvedor'})


@app.route('/soma', methods=['POST','GET'])
def soma():
  if request.method == 'POST':
    dados = json.loads(request.data)
    total = sum(dados['valores'])
  elif request.method == 'GET':
    total = 10 + 10
  return jsonify({'soma' :total})


if __name__=='__main__':
  app.run(debug=True)