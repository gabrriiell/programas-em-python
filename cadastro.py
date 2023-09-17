import requests
dados = {}
requisicao = requests.get('https://cientes-391cf-default-rtdb.firebaseio.com/.json')
dado = requisicao.json()
        
c = str(input("já é cadastrado [S/N]:"))

if c == 'n':
    dados["nome"] = str(input("Nome: "))  
    dados["senha"] = str(input("Senha: ")) 
    url = 'https://cadastro-6164e-default-rtdb.firebaseio.com/'
    
    requests.post(url, json = dados)
    dados.clear


elif c == "s":
    nome = str(input("nome "))
    senha = (input("senha "))
    user = False
    
    for k, v in dado.items():
      if v["nome"] == nome and v['senha'] == senha:
        print(f'bem vindo de volta {nome}')
        user = True
    
    if not user:
        print("Nome de usuário ou senha incorretos.")
