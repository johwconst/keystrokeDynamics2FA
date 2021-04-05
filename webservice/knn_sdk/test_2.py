import sys
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

keystroke_data = pd.read_csv('heart.csv')
amostra = "-0.093,-0.124,-0.212,-0.088,-0.039,-0.1,-0.124,-0.096,-0.016,-0.112,-0.148,-0.04,-0.133,-0.308,-0.441,-0.14,-0.1,-0.131,0,-0.131,-0.07,-0.052,-0.104,-0.156,-0.26,-0.073,-0.027,-0.112,-0.346,-0.458,-0.199,-0.576,-0.153,-0.375,-0.528,-0.185,-0.369,-0.164,-0.172,-0.336,-0.348,-0.04,-0.173,-0.36,-0.533,-0.14,-0.116,-0.132,-0.145,-0.277,-0.272,-0.064,-0.181,-0.128,-0.309,-0.168,-0.608,-0.121,-0.119,-0.24,-0.216,-0.071,-0.153,-0.383,-0.536,-0.132,-0.119,-0.146,-0.108,-0.254,-0.22,-0.044,-0.164,-0.268,-0.432,-0.088,-0.093,-0.111,-0.265,-0.376,-0.369,-0.056,-0.148,-0.209,-0.357,-0.091,-0.104,-0.252,-0.148,-0.096,-0.112,-0.033,-0.152,-0.02,-0.172,-0.109,-0.095,-0.135,-0.501,-0.636,-0.1,-0.144,-0.14,-0.276,-0.416,-0.104,-0.217,-0.12,-0.188,-0.308,-0.204,-0.008,-0.194,-0.155,-0.349,-0.306,-0.045,-0.161,-0.344,-0.505,-0.127"

data = keystroke_data.iloc[:, 0:121]
le = preprocessing.LabelEncoder()

target = keystroke_data['CLASS']

sample_text_row = pd.DataFrame.transpose(pd.DataFrame(amostra.split(",")))

data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.2, random_state=10)

knn_model = KNeighborsClassifier(n_neighbors=3, metric="euclidean")

knn_model.fit(data_train, target_train)

inner_prediction = knn_model.predict(data_test)

outer_prediction2 = knn_model.predict(sample_text_row)

print(outer_prediction2)

print("KNeighbors accuracy score (inner): ", accuracy_score(target_test, inner_prediction))