
# IMPORTS DE LIBS PROPRIAS
from database.db_connect import drop_db, create_db, add_user_and_passw, check_user_and_passw

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import numpy as np
import csv

import sys
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


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
		data.append(user_id) # adiciona o user id ao fim da lista
		try:
			with open('heart.csv', 'a', newline='') as file:			
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

@app.route('/login/auth2', methods = ['POST']) # Rota para a primeira autenticação
def auth2():
	response = dict(request.get_json())
	typing_data  = response['typing_data']
	user_id = response['user_id']
	
	keystroke_data = pd.read_csv('heart.csv')
	amostra = typing_data
	data = keystroke_data.iloc[:, 0:121]

	target = keystroke_data['CLASS']

	sample_text_row = pd.DataFrame.transpose(pd.DataFrame(amostra))

	data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.2, random_state=10)

	knn_model = KNeighborsClassifier(n_neighbors=3, metric="euclidean")

	knn_model.fit(data_train, target_train)

	inner_prediction = knn_model.predict(data_test)

	outer_prediction2 = knn_model.predict(sample_text_row)

	print("################# Usuario:", outer_prediction2)
	accuracy = accuracy_score(target_test, inner_prediction)
	print("################# KNeighbors accuracy score : ", accuracy)
	
	return jsonify({'resultado': str(outer_prediction2), 'accuracy': accuracy}) 



# Server Start
if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True, port=3000)
