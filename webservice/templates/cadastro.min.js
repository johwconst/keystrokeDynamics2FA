var usuario_id;
var entrada_dados;
var digitacao_pattern = [];
var texto_input;
var texto_padrao = "com grandes poderes vem grandes responsabilidades";
const botao_cadastro = document.getElementById("btn_cadastrar");
const cadastro_sucesso = document.querySelector(".cadastro_sucesso");
const form = document.querySelector('.form');
const typing_form = document.querySelector('.typing-form');
const exist = document.querySelector('.user_already_exist');

function cadastro(){     
    $.ajax({
        type : 'POST',
        url : 'http://127.0.0.1:3000/usuario',
        contentType: 'application/json; charset=UTF-8',
        data : JSON.stringify({'username':username.value, 'password': password.value}),
        dataType : 'json',
          success: function(rdata){
              if(rdata['cadastro_cod']=='UserRegistrySuccess'){
                  usuario_id = rdata['id_usuario']
        console.log(usuario_id) 
        form.style.display = 'none'
        exist.style.display = 'none'
        typing_form.style.display = 'block'
              }
              else if(rdata['cadastro_cod']=='UsernameAlreadyExist'){
        console.log('Username já cadastrado..');
        const exist = document.querySelector('.user_already_exist');
        exist.style.display = 'block'
                    
              }
          }
      });
}

function text_onfocus(){
      now_1 = Date.now(); // PEGA HORA 1
      now_2 = Date.now(); // PEGA HORA 2
    }

function digitacao_keydown(){
      now_3 = Date.now();
      entrada_dados = (now_3 - now_1) / 1000; 
      digitacao_pattern.push(entrada_dados);
      verificaTexto();
    }

function digitacao_keyup() {
      now_4 = Date.now();
      entrada_dados = (now_4 - now_1) / 1000; 
      digitacao_pattern.push(entrada_dados); 
      verificaTexto()           
    }

function verificaTexto() {
      texto_input = document.getElementById("texto_input").value;
      if (texto_padrao == texto_input){
        document.getElementById("text_color").style.color="#19e030";
        botao_cadastro.disabled = false;
        console.log('digitado corretamente');
      }
      else {
        document.getElementById("text_color").style.color="#de213a";
        botao_cadastro.disabled = true;
        console.log('texto não correto')
      }
    }

function send_biometric(){
    typing_form.style.display = 'none'
    cadastro_sucesso.style.display = 'block'
    $.ajax({
        type : 'POST',
        url : 'http://127.0.0.1:3000/biometria',
        contentType: 'application/json; charset=UTF-8',
        data : JSON.stringify({'user_id':usuario_id, 'data':digitacao_pattern}),
        dataType : 'json',
          success: function(rdata){
              if(rdata['biometric_cod']=='Success'){
                  console.log('sucess')
              }
              else if(rdata['biometric_cod']=='Fail'){
        console.log('fail');
              }
          }
      });
  }