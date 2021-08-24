# Keystrokes Dynamics To 2FA  (KDT-2FA)⌨️

<p align="center">
  <img src="webservice/static/img/logo.png" />
</p>

The Biometric Keyboard project is a prototype that uses typing dynamics as a second factor in user authentication.

Authentication based on typing dynamics does not require any additional hardware for its implementation and provides an extra layer of security, therefore, it has a lower cost and greater security compared to conventional systems. In this prototype, the KNN machine learning algorithm is used to classify the user's typing dataset, where it was possible to obtain promising results with accuracy rates of 88,99%, FAR 10,00% and FRR 8,33% for the final dataset. 

keywords: knn, keystrokes dynamics, typing dynamics, hyper parameters

## installation

requirements 
* Python 3.7.2

installed libraries: 
~~~python
pip install -r requetiments.txt
~~~

## Run project
~~~python
python server.py
~~~

After the application will be accessible by address: *127.0.0.1:3000*
