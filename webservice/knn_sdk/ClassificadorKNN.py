
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
# teste
from sklearn.model_selection import cross_validate



class Classificador:
    def __init__(self, arquivo_biometrico_cadastrados, amostra_digitacao, knn_model_test_ratio, neighbour_size):
        self.arquivo_biometrico_cadastrados = arquivo_biometrico_cadastrados    # Classes x Modelos
        self.amostra_digitacao = amostra_digitacao                              # Amostra a ser classificada
        self.knn_model_test_ratio = knn_model_test_ratio                        # Deve estar entre 0,0 e 1,0 e representar a proporção do conjunto de dados a ser incluído na divisão de teste.
        self.neighbour_size = neighbour_size                                    # Controla o embaralhamento aplicado aos dados antes de aplicar a divisão. Passe um int para saída reproduzível em várias chamadas de função. 

    def knn_manhattan_holdout(self): # metricada é dada por holdout
        description = 'knn_manhattan_t'
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

        print("[+] Usuario predict:", usuario_predict)
        
        return str(usuario_predict), str(accuracy), description

        
    def knn_manhattan_sem_treino(self):
        description = 'knn_manhattan_s'
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

        print('[+] Usuario Predict - ', inner_prediction)
 
        return str(inner_prediction), str(acuracia), description

    def hyper_parameters_tuning(self):

        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados, keep_default_na=False)
        
        # Deverá ser alterado quando a quantidade do array for diferente de 121
        data = keystroke_data.iloc[:, 0:97]  

        # Classes para aplicação na aprendizagem supervisionada
        target = keystroke_data['CLASS']

        k_range = list(range(1,10))
        leaf_size = list(range(1,50))
        weight_options = ["uniform", "distance"]
        p=[1,2]

        param_grid = dict(leaf_size=leaf_size, n_neighbors=k_range, weights=weight_options, p=p)

        knn = KNeighborsClassifier()

        grid = GridSearchCV(knn, param_grid, scoring='accuracy')
        grid.fit(data,target)

        best_score = grid.best_score_
        best_params = grid.best_params_
        best_estimator = grid.best_estimator_

        print('[+] Best Score - ',best_score)
        print('[+] Best Params - ',best_params)
        print('[+] Best Estimator - ',best_estimator)
 
        return best_score, best_params, best_estimator

    def get_cv_score(self):
        description = 'knn_manhattan_score_teste'
        keystroke_data = pd.read_csv(self.arquivo_biometrico_cadastrados, keep_default_na=False)

        # Deverá ser alterado quando a quantidade do array for diferente de 121

        data = keystroke_data.iloc[:, 0:97]  

        # Classes para aplicação na aprendizagem supervisionada
        target = keystroke_data['CLASS']

        knn_model = KNeighborsClassifier(n_neighbors=self.neighbour_size, metric="manhattan")

        knn_model.fit(data, target)

        scores = cross_validate(knn_model, data, target, scoring=['accuracy']) # ROC_AUC
        score_result = scores['test_accuracy'].mean() * 100
        print('[+] Média Accuracy (test_accuracy): %.2f' % score_result)
 
        return score_result

    