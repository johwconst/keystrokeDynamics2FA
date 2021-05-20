# TecladoBiométrico - 2FA ⌨️

<p align="center">
  <img src="webservice/static/img/logo.png" />
</p>

O projeto TecladoBiometrico trata-se de um protótipo que faz o uso da dinâmica de digitação como segundo fator na autenticação do usuário. 

Autenticação com base na dinâmica de digitação não requer nenhum hardware adicional para sua implementação e fornece uma camada extra de segurança, portanto, possui um menor custo e maior segurança em comparação com os sistemas convencionais. Neste protótipo, utiliza-se algoritmo de aprendizado de máquina KNN utilizado na classificação do conjunto de dados de digitação dos usuários, onde por meio do mesmo foi possivel obter resultados promissores com taxas de accuracy de 88% para o conjunto de dados de 20 usuários testados. 

## Instalação

Requisitos: 
* Python 3.7.2

Instalando bibliotecas: 
~~~python
pip install -r requetiments.txt
~~~

## Executando o projeto
~~~python
python server.py
~~~

Após a aplicação estará acessivel pelo endereço: *127.0.0.1:3000*
