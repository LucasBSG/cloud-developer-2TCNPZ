## Descrição

Este é um microserviço desenvolvido em Python usando Flask para gerenciar permissões de usuários. Ele permite verificar se um usuário tem permissão para realizar determinadas ações.

## Funcionalidades

- Definição de papéis com permissões específicas.

- Cadastro de usuários com diferentes papéis.

- API para verificar se um usuário tem determinada permissão.

## Estrutura do Código

- Role: Classe que define um papel e suas permissões.

- User: Classe que define um usuário e associa um papel a ele.

- users: Dicionário que armazena os usuários cadastrados.

- check_permission(username, permission): Endpoint para verificar permissões de um usuário.

## Como Executar

- Rodando localmente

- Instale as dependências:

'''
pip install flask
'''

Execute o aplicativo:

python app.py

- Acesse a API para verificar permissões:

curl http://localhost:5000/permissoes/admin_user/delete

- Rodando com Docker

Construa a imagem Docker:

'''
docker build -t permissoes-services .
'''

Execute o contêiner:

'''
docker run -d -p 5000:5000 --name microservico permissoes-services
'''

## Exemplo de Uso

Se um usuário tiver permissão, a API retornará:

{
  "user": "admin_user",
  "permission": "delete",
  "allowed": true
}

Caso contrário:

{
  "user": "common_user",
  "permission": "delete",
  "allowed": false
}