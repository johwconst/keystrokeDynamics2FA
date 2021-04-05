import sys
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

class Classificador:
    def __init__(self, arquivo_biometrico_cadastrados, digitacao_amostra, knn_model_test_ratio, neighbour_size):
        self.arquivo_biometrico_cadastrados = arquivo_biometrico_cadastrados
        self.digitacao_amostra = digitacao_amostra
        self.knn_model_test_ratio = knn_model_test_ratio
        self.neighbour_size = neighbour_size

    def knn_euclidean(self):
        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados)
        amostra = self.digitacao_amostra

        data = keystroke_data.iloc[:, 0:121]

        target = keystroke_data['CLASS']

        sample_text_row = pd.DataFrame.transpose(pd.DataFrame(amostra))

        data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=self.knn_model_test_ratio, random_state=10)

        knn_model = KNeighborsClassifier(n_neighbors=self.neighbour_size, metric="euclidean")

        knn_model.fit(data_train, target_train)

        inner_prediction = knn_model.predict(data_test)

        outer_prediction2 = knn_model.predict(sample_text_row)

        print("################# Usuario:", outer_prediction2)
        accuracy = accuracy_score(target_test, inner_prediction)
        print("################# KNeighbors accuracy score : ", accuracy)
        
        return str(outer_prediction2), str(accuracy) 