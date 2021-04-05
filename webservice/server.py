
# IMPORTS DE LIBS PROPRIAS
from database.db_connect import drop_db, create_db, add_user_and_passw, check_user_and_passw

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import numpy as np
import csv


from flask import Flask, render_template, request, jsonify
import pandas as pd
import csv

BASE_USER = [-0.127,-0.434,-0.112,-0.401,-0.513,-0.115,-0.617,-0.125,-0.307,-0.432,-0.166,-0.507,-0.1,-0.145,-0.245,-0.097,-0.094,-0.085,-0.412,-0.497,-0.172,-0.117,-0.124,-0.307,-0.431,-0.085,-0.123,-0.129,-0.381,-0.51,-0.139,-0.186,-0.118,-0.158,-0.276,-0.377,-0.024,-0.168,-0.197,-0.365,-0.358,-0.063,-0.176,-0.207,-0.383,-0.156,-0.117,-0.105,-0.14,-0.245,-0.264,-0.082,-0.175,-0.131,-0.306,-0.101,-0.224,-0.08,-0.272,-0.352,-0.187,-0.195,-0.118,-0.214,-0.332,-0.099,-0.09,-0.101,-0.031,-0.132,-0.188,-0.035,-0.134,-0.197,-0.331,-0.096,-0.209,-0.099,-0.465,-0.564,-0.596,-0.069,-0.14,-0.202,-0.342,-0.139,-0.336,-0.476,-0.14,-0.077,-0.138,-0.023,-0.121,-0.012,-0.133,-0.087,-0.072,-0.122,-0.314,-0.436,-0.138,-0.088,-0.115,-0.182,-0.297,-0.064,-0.167,-0.1,-0.008,-0.108,-0.105,-0.04,-0.136,-0.084,-0.22,-0.151,-0.074,-0.09,-0.593,-0.683,-0.063]
BIOMETRIA_PATH = '../sdk_lib/sdk/biometrias/' # Pasta onde será salvo os dados .csv
drop_db() # Deleta o banco caso exista
create_db() # Cria o banco de dados SQLite
model = KNeighborsClassifier(n_neighbors=1)


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('./login/login.html')

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
		dataframe = pd.DataFrame(data)
		path = BIOMETRIA_PATH + str(user_id) + ".csv"
		try: 
			dataframe.to_csv(path, header=False, index=False)
			return jsonify({'biometric_cod': 'Success'})
		except:
			print("Não foi possivel gerar o arquivo .csv")

@app.route('/login', methods = ['GET'])
def login():
	return render_template('./login/login.html')

@app.route('/login/auth1', methods = ['POST']) # Rota para a primeira autenticação
def auth1():
	response = dict(request.get_json())
	username  = response['username']
	password = response['password']
	print()

	id, result, user_id = check_user_and_passw(username, password)

	if result:
		return jsonify({'auth1_code': 'success', 'id_usuario': user_id})
	else:
		if id == 3:
			return jsonify({'auth1_code': 'UsernameNotExist'})
		elif id == 1:
			return jsonify({'auth1_code': 'PasswordIsWrong'})

@app.route('/login/auth2', methods = ['POST']) # Rota para a primeira autenticação
def auth2():
	response = dict(request.get_json())
	typing_data  = response['typing_data']
	user_id = response['user_id']
	print(typing_data)
	print(user_id)
	data = read_csv_return_data(str(user_id))
	print('##### USUARIO DO CSV',data)
	resultado = verificar_usuario(typing_data, data)

	return jsonify({'isValid': resultado})


def read_csv_return_data(id):
	data_usuario_cadastrado = []
	with open('../sdk_lib/sdk/biometrias/' + str(id) + '.csv', encoding='utf-8') as arquivo_referencia:
  		tabela = csv.reader(arquivo_referencia, delimiter=',')
  		for linha in tabela:
			  data_usuario_cadastrado.append(float(linha[0]))
	return data_usuario_cadastrado


def verificar_usuario(user_validar, user_cadastrado):
	merge = []
	merge.append(user_cadastrado)
	merge.append(BASE_USER)
	print(merge)

	dados = ([-0.116, -0.161, -0.26, -0.099, -0.056, -0.109, -0.107, -0.092, -0.021, -0.113, -0.097, -0.04, -0.089, -0.132, -0.221, -0.1, -0.253, -0.111, -0.053, -0.164, -0.144, -0.044, -0.088, -0.14, -0.228, -0.089, -0.056, -0.117, -0.092, -0.209, -0.195, -0.044, -0.061, -0.105, -0.031, -0.041, -0.041, -0.129, -0.107, -0.236, -0.179, -0.041, -0.08, -0.126, -0.206, -0.083, -0.051, -0.077, -0.139, -0.216, -0.273, -0.059, -0.124, -0.028, -0.152, -0.085, -0.135, -0.064, -0.004, -0.068, -0.064, -0.048, -0.097, -0.14, -0.237, -0.104, -0.028, -0.092, -0.057, -0.149, -0.134, -0.055, -0.115, -0.133, -0.248, -0.087, -0.044, -0.096, -0.076, -0.172, -0.166, -0.034, -0.079, -0.132, -0.211, -0.068, -0.049, -0.12, -0.071, -0.077, -0.059, -0.04, -0.028, -0.068, -0.036, -0.021, -0.068, -0.104, -0.156, -0.26, -0.092, -0.012, -0.092, -0.134, -0.226, -0.06, -0.107, -0.155, -0.048, -0.02, -0.085, -0.02, -0.103, -0.012, -0.115, -0.093, -0.04, -0.095, -0.124, -0.219, -0.054], [-0.127, -0.434, -0.112, -0.401, -0.513, -0.115, -0.617, -0.125, -0.307, -0.432, -0.166, -0.507, -0.1, -0.145, -0.245, -0.097, -0.094, -0.085, -0.412, -0.497, -0.172, -0.117, -0.124, -0.307, -0.431, -0.085, -0.123, -0.129, -0.381, -0.51, -0.139, -0.186, -0.118, -0.158, -0.276, -0.377, -0.024, -0.168, -0.197, -0.365, -0.358, -0.063, -0.176, -0.207, -0.383, -0.156, -0.117, -0.105, -0.14, -0.245, -0.264, -0.082, -0.175, -0.131, -0.306, -0.101, -0.224, -0.08, -0.272, -0.352, -0.187, -0.195, -0.118, -0.214, -0.332, -0.099, -0.09, -0.101, -0.031, -0.132, -0.188, -0.035, -0.134, -0.197, -0.331, -0.096, -0.209, -0.099, -0.465, -0.564, -0.596, -0.069, -0.14, -0.202, -0.342, -0.139, -0.336, -0.476, -0.14, -0.077, -0.138, -0.023, -0.121, -0.012, -0.133, -0.087, -0.072, -0.122, -0.314, -0.436, -0.138, -0.088, -0.115, -0.182, -0.297, -0.064, -0.167, -0.1, -0.008, -0.108, -0.105, -0.04, -0.136, -0.084, -0.22, -0.151, -0.074, -0.09, -0.593, -0.683, -0.063])
	classes = ([1, 0])

	dados_array = np.array(dados)
	classes_array = np.array(classes)

	dados_final = dados_array.reshape(-1, 1)
	classes_final = classes_array.reshape(-1, 1)


	desconhecido_array = np.array(user_validar)
	desconhecido_final = desconhecido_array.reshape(-1, 1)

	model.fit(dados_final, classes_final)
	print('MODELO MONTADO')

	previsoes = model.predict([desconhecido_final])
	
	return jsonify({'resultado': previsoes}) 



# Server Start
if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True, port=3000)
