
# IMPORTS DE LIBS PROPRIAS
from database.db_connect import drop_db, create_db, add_user_and_passw, check_user_and_passw, get_user_id
from knn_sdk.ClassificadorKNN import Classificador

import csv
from flask import Flask, render_template, request, jsonify, url_for


TYPING_DATA_PATH = './database/biometria.csv' # Pasta onde será salvo os dados .csv e banco
app = Flask(__name__, static_folder='./static')

@app.route('/')
def home():
	return render_template('./home/home.html')

@app.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
	if request.method == 'GET':
		return render_template('./cadastro/cadastro.html')
	elif request.method == 'POST':
		response = dict(request.get_json())
		username  = response['username']
		password = response['password']
		id, result = add_user_and_passw(username, password)

		if result:
			return jsonify({'cadastro_cod': 'UserRegistrySuccess', 'id_usuario': id})
		else:
			return jsonify({'cadastro_cod': 'UsernameAlreadyExist'})


@app.route('/cadastro/biometria', methods = ['POST'])
def biometria():
	if request.method == 'POST':
		response = dict(request.get_json())
		user_id  = response['user_id']
		data = response['data']
		data.append(user_id) # adiciona o user id ao fim da lista
		try:
			with open(TYPING_DATA_PATH, 'a', newline='') as file:			
				writer = csv.writer(file)
				writer.writerow(data)

			return jsonify({'biometric_cod': 'Success'})
		except:
			return jsonify({'biometric_cod': 'Não foi possivel cadastrar os dados biometricos'})

@app.route('/treinar/biometria', methods = ['POST'])
def treinar():
	if request.method == 'POST':
		response = dict(request.get_json())
		username  = response['username']
		data = response['data']
		user_id = get_user_id(username)
		if user_id == None: #Caso seja digitado um usuario não cadastrado no treinamento, ainda ssim aproveitar os dados.
			user_id = 999 
		data.append(user_id) # adiciona o user id ao fim da lista
		try:
			with open(TYPING_DATA_PATH, 'a', newline='') as file:			
				writer = csv.writer(file)
				writer.writerow(data)

			return jsonify({'biometric_cod': 'Success'})
		except:
			return jsonify({'biometric_cod': 'Não foi possivel cadastrar os dados biometricos'})


@app.route('/login', methods = ['GET'])
def login():
	return render_template('./login/login.html')

@app.route('/login/auth1', methods = ['POST']) # Rota para a primeira autenticação
def auth1():
	response = dict(request.get_json())
	username  = response['username']
	password = response['password']

	id, result, user_id = check_user_and_passw(username, password)

	if result:
		return jsonify({'auth1_code': 'success', 'id_usuario': user_id})
	else:
		if id == 3:
			return jsonify({'auth1_code': 'UsernameNotExist'})
		elif id == 1:
			return jsonify({'auth1_code': 'PasswordIsWrong'})

@app.route('/login/auth2', methods = ['POST']) # Rota para a segunda autenticação
def auth2():
	response = dict(request.get_json())
	amostra_digitacao  = response['typing_data']
	user_id = response['user_id']
	
	classifica = Classificador(TYPING_DATA_PATH, amostra_digitacao, 0.7, 3)
	resultado = classifica.knn_test()

	print("Usuario real:", user_id,"Usuario Previsto:", resultado[0], "accuracy:", resultado[1])

	return jsonify({'predict': resultado[0], 'accuracy': resultado[1]})

@app.route('/treinar', methods = ['GET', 'POST'])
def treina_bio():
	if request.method == 'GET':
		return render_template('./treinamento/treinamento.html')

	
# Server Start
if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True, port=3000)
