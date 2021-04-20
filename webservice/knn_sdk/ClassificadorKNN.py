import sys
from types import prepare_class
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score
# teste
import matplotlib.pyplot as plt
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions
from matplotlib.colors import ListedColormap
import seaborn as sns



class Classificador:
    def __init__(self, arquivo_biometrico_cadastrados, amostra_digitacao, knn_model_test_ratio, neighbour_size):
        self.arquivo_biometrico_cadastrados = arquivo_biometrico_cadastrados    # Classes x Modelos
        self.amostra_digitacao = amostra_digitacao                              # Amostra a ser classificada
        self.knn_model_test_ratio = knn_model_test_ratio                        # Deve estar entre 0,0 e 1,0 e representar a proporção do conjunto de dados a ser incluído na divisão de teste.
        self.neighbour_size = neighbour_size                                    # Controla o embaralhamento aplicado aos dados antes de aplicar a divisão. Passe um int para saída reproduzível em várias chamadas de função. 

    def knn_euclidean(self):

        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados, keep_default_na=False)
        
        amostra = self.amostra_digitacao

        # Deverá ser alterado quando a quantidade do array for diferente de 121
        data = keystroke_data.iloc[:, 0:97]  

        # Classes para aplicação na aprendizagem supervisionada
        target = keystroke_data['CLASS']

        dataframe_amostra = pd.DataFrame.transpose(pd.DataFrame(amostra))

        data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=self.knn_model_test_ratio, random_state=10)

        knn_model = KNeighborsClassifier(n_neighbors=self.neighbour_size, metric="euclidean")

        knn_model.fit(data_train, target_train)

        inner_prediction = knn_model.predict(data_test)
        usuario_predict = knn_model.predict(dataframe_amostra)

        accuracy = accuracy_score(target_test, inner_prediction)

        print("################# Usuario predict:", usuario_predict)
        print("################# KNeighbors accuracy score : ", accuracy)

        return str(usuario_predict), str(accuracy)

    def knn_manhattan(self):
        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados, keep_default_na=False)
        
        amostra = self.amostra_digitacao

        # Deverá ser alterado quando a quantidade do array for diferente de 121
        data = keystroke_data.iloc[:, 0:97]  

        # Classes para aplicação na aprendizagem supervisionada
        target = keystroke_data['CLASS']

        dataframe_amostra = pd.DataFrame.transpose(pd.DataFrame(amostra))

        data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=self.knn_model_test_ratio, random_state=10)

        knn_model = KNeighborsClassifier(n_neighbors=self.neighbour_size, metric="manhattan")

        knn_model.fit(data_train, target_train)

        inner_prediction = knn_model.predict(data_test)
        usuario_predict = knn_model.predict(dataframe_amostra)

        accuracy = accuracy_score(target_test, inner_prediction)

        print("################# Usuario predict:", usuario_predict)
        print("################# KNeighbors accuracy score : ", accuracy)

        return str(usuario_predict), str(accuracy)

    def knn_manhattan_test(self):
        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados, keep_default_na=False)
        
        amostra = self.amostra_digitacao

        # Deverá ser alterado quando a quantidade do array for diferente de 121
        data = keystroke_data.iloc[:, 0:97]  

        # Classes para aplicação na aprendizagem supervisionada
        target = keystroke_data['CLASS']

        dataframe_amostra = pd.DataFrame.transpose(pd.DataFrame(amostra))

        data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=self.knn_model_test_ratio, random_state=10)

        knn_model = KNeighborsClassifier(n_neighbors=self.neighbour_size, metric="manhattan")

        knn_model.fit(data_train, target_train)

        inner_prediction = knn_model.predict(data_test)
        usuario_predict = knn_model.predict(dataframe_amostra)

        accuracy = accuracy_score(target_test, inner_prediction)

        print("################# Usuario predict:", usuario_predict)
        print("################# KNeighbors accuracy score : ", accuracy)
        
        return str(usuario_predict), str(accuracy)

        
    def knn_test(self):
        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados, keep_default_na=False)
        
        amostra = self.amostra_digitacao

        # Deverá ser alterado quando a quantidade do array for diferente de 121
        data = keystroke_data.iloc[:, 0:97]  

        # Classes para aplicação na aprendizagem supervisionada
        target = keystroke_data['CLASS']

        sample_text_row = pd.DataFrame.transpose(pd.DataFrame(amostra))

        knn_model = KNeighborsClassifier(n_neighbors=self.neighbour_size, metric="manhattan")

        knn_model.fit(data, target)

        predict_label = []
        for n in range(0,len(target)):
            inner_prediction = knn_model.predict(sample_text_row)
            predict_label.append(inner_prediction)
    

        acuracia = accuracy_score(target, predict_label)

        print("################# Usuario predict:", inner_prediction)
        print('[+] Accuracy - ', 100 * acuracia, '%')

        
        return str(inner_prediction), str(acuracia)