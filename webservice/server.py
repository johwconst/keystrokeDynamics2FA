from flask import Flask, render_template, redirect, request, url_for, jsonify





app = Flask(__name__)

@app.route('/')
def home() :
	return render_template('login.html')


if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=True, port=4000)
