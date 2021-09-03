# Keystrokes Dynamics To 2FA  (KDT-2FA) ⌨️🔒

<p align="center">
  <img src="webservice/static/img/logo.png" />
</p>

keystrokeDynamics2FA is a prototype that uses typing dynamics as a second factor in user authentication.

Dynamic typing based authentication does not require any additional hardware for its implementation and provides an extra layer of security, therefore, it is cheaper and more secure compared to conventional systems. In this prototype, the KNN machine learning algorithm is used to classify the user's typing dataset, where it was possible to obtain promising results with hit rates of 88.99%, FAR 10.00% and FRR 8.33% for the final dataset.

Another evaluation carried out was the speed of access via typing dynamics compared to receiving codes via e-mail, which proved to be a faster alternative.

<p align="center">
  <img src="https://i.imgur.com/toiOxSM.gif" />
</p>

keywords: knn, keystrokes, typing dynamics, hyperparameters

## Typing Extraction ⌨️

The Figure shows the elements that compose the typing data, being characterized by p Thus p1 represents the first time the key was pressed. This is the current time of the press. After the key is released, p2 is obtained, storing the time the key was released. In this way, the keypress time or Dwell Time, identified by T, is done by subtracting the values of p1 and p2. Where, T1 represents the time of pressing the first key.

<p align="center">
<img src="https://i.imgur.com/aVYHhY1.png" alt="drawing" width="400"/>
</p>

So pressing the first key, the time of f is obtained. Where f1 represents the initial value of the flight time or Fligh Time, after the second key is pressed, the time of f2 representing the final time from pressing the first key to the second key pressed is obtained. At the end, the values are subtracted, obtaining the value of F. Where F1 presents the flight time or Flight Time between pressing the first key until the second key is pressed. In this way, the extraction of the next data according to its identifier is performed.


# Results 📊

After obtaining the parameters, the parameters were applied to the algorithm in a scenario. In this scenario, real users validated the prototype by performing authentication. Each user performed 3 accesses using their username and password registered in the previous step (registration) and 3 accesses with users and passwords of other users in the different data sets, of 20, 10 and 5 users. In this step, the selection of users in the dataset occurred through the researcher, the user who will access more users defined in the dataset for access being always defined.

Thus, for validation, 18 authentications were performed for each user, totaling 360 authentications in the prototype. After each authentication, the registration of the data obtained was carried out, and the analysis was carried out in order to identify whether the user was successful in the second authentication step or not, with the data researcher being registered in order to obtain the FAR and FRR values of the prototype . During the validation step, a failure in data collection was detected, leaving 5 users with 1 missing value in the semi-final column of the data set. obtaining the best parameters and accuracy of the classifier.

| Users Data (Users) | True Access | False Access | The amount of FAR | The amount of FRR | FAR (%) | FRR (%) | Accuracy |
| ------------------ | ----------- |  ----------- |  ---------------- |  ---------------- | ------- | ------- |  ------- |
|        20          |      60     |       60     |         6         |         7         | 10,00%  |  8,33%  |  88,99%  |
|        10          |      60     |       60     |         8         |         8         | 11,66%  | 11,66%  |  86,00%  |
|        5           |      60     |       60     |         3         |         3         | 5,00%   |  5,00%  |  96,00%  |



## Prototype vs E-mail Code 🔥

To validate the developed prototype, it was necessary to compare it with a service used for authentication in the second stage, choosing the option of verification by code via e-mail. The choice of this method was made due to the ease of sharing and obtaining measurements with users, that is, other types such as receiving the code via smartphone, which is difficult to compare and obtaining data through users, due to the need to have the smartphone's registration of each user.

![GIF tempo de Comparação](https://i.imgur.com/SGa0Iwq.gif)

Thus, through the application, 34 tests were performed, divided among 17 users. Each user was instructed to access the email service with the credentials provided by the researcher. The user performed first and second factor authentication on the email platform. After that, it was compared with accessing the prototype. All steps were followed by the researcher in order to obtain access time.

In this way, it was possible to evaluate the access time of 17 users, in the two systems compared. The result obtained in the second factor authentication via email had an average time of 24.4 seconds. However, no prototype proposed, the result averaged 12.98 seconds

# installation 🏃‍♂️

requirements 
* Python 3.7.2

installed libraries: 
~~~python
pip install -r requetiments.txt
~~~

## Run project 🏃‍♂️
~~~python
python server.py
~~~

After the application will be accessible by address: *127.0.0.1:3000*
