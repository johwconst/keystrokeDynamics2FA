from database.db_connect import drop_db, create_db, add_user_and_passw, get_user_and_passw 
from flask import Flask, render_template, request, jsonify, current_app, g
from flask.cli import with_appcontext
import sqlite3
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neighbors import KNeighborsClassifier
from collections import Counter
from sklearn.metrics import accuracy_score
import pickle
import glob
import csv
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
create_db() # Cria banco SQL

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/cadastro')
def cadastro():
	return render_template('cadastro.html')

@app.route('/usuario', methods = ['GET', 'POST'])
def usuario():
	if request.method == 'POST':
		response = dict(request.get_json())
		username  = response['username']
		password = response['password']
		id, result = add_user_and_passw(username, password)

		if result:
			return jsonify({'cadastro_cod': 'UserRegistrySuccess', 'id_usuario': id})
		else:
			return jsonify({'cadastro_cod': 'UsernameAlreadyExist'})

@app.route('/biometria', methods = ['POST'])
def biometria():
	if request.method == 'POST':
		response = dict(request.get_json())
		user_id  = response['user_id']
		data = response['data']
		dataframe = pd.DataFrame(data)
		path = "biometic/" + str(user_id) + ".csv"
		try: 
			dataframe.to_csv(path, header=False, index=False)
			return jsonify({'biometric_cod': 'Success'})
		except:
			print("Não foi possivel gerar o arquivo .csv")

if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True, port=3000)

