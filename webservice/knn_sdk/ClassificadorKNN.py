import sys
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

class Classificador:
    def __init__(self, arquivo_biometrico_cadastrados, amostra_digitacao, knn_model_test_ratio, neighbour_size):
        self.arquivo_biometrico_cadastrados = arquivo_biometrico_cadastrados    # Classes x Modelos
        self.amostra_digitacao = amostra_digitacao                              # Amostra a ser classificada
        self.knn_model_test_ratio = knn_model_test_ratio                        # Deve estar entre 0,0 e 1,0 e representar a proporção do conjunto de dados a ser incluído na divisão de teste.
        self.neighbour_size = neighbour_size                                    # Controla o embaralhamento aplicado aos dados antes de aplicar a divisão. Passe um int para saída reproduzível em várias chamadas de função. 

    def knn_euclidean(self):
        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados)
        
        amostra = self.amostra_digitacao

        # Deverá ser alterado quando a quantidade do array for diferente de 121
        data = keystroke_data.iloc[:, 0:121]  

        # Classes para aplicação na aprendizagem supervisionada
        target = keystroke_data['CLASS']

        sample_text_row = pd.DataFrame.transpose(pd.DataFrame(amostra))

        data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=self.knn_model_test_ratio, random_state=10)

        knn_model = KNeighborsClassifier(n_neighbors=self.neighbour_size, metric="manhattan")

        knn_model.fit(data_train, target_train)

        inner_prediction = knn_model.predict(data_test)

        outer_prediction2 = knn_model.predict(sample_text_row)

        print("################# Usuario predict:", outer_prediction2)
        accuracy = accuracy_score(target_test, inner_prediction)
        print("################# KNeighbors accuracy score : ", accuracy)
        
        return str(outer_prediction2), str(accuracy) 