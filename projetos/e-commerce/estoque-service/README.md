# Estoque Service

Este microserviço é responsável por gerenciar o estoque de produtos no projeto de e-commerce.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask. Contém as rotas e a lógica para gerenciar o estoque de produtos.
- `Dockerfile`: Arquivo de configuração para criar a imagem Docker do microserviço.
- `requirements.txt`: Lista de dependências necessárias para rodar a aplicação Flask.

## Arquivos

### `app.py`

Este arquivo contém o código principal da aplicação Flask. Ele define as seguintes rotas:

- `/`: Retorna uma mensagem indicando que o serviço está funcionando.
- `/status`: Retorna o status do serviço.
- `/estoque`: Retorna uma lista de produtos disponíveis no estoque.

### `Dockerfile`

Este arquivo define como construir a imagem Docker para o microserviço. Ele inclui as seguintes etapas:

1. Usa uma imagem oficial do Python.
2. Define o diretório de trabalho no container.
3. Copia os arquivos `requirements.txt` e `app.py` para o container.
4. Instala as dependências listadas em `requirements.txt`.
5. Expõe a porta 8080.
6. Define o comando para rodar a aplicação.

### `requirements.txt`

Este arquivo lista as dependências necessárias para rodar a aplicação Flask. No caso, a única dependência é o Flask.

Exemplo de código:

```txt
flask
```

## Como Rodar o Serviço

### Localmente

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute a aplicação:
   ```bash
   python app.py
   ```

### Usando Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t estoque-img .
   ```

2. Rode o container:
   ```bash
   docker run -d -p 8080:8080 --name estoque-ctn estoque-img
   ```

## Endpoints

- **Home:** `GET /`
- **Status:** `GET /status`
- **Estoque:** `GET /estoque`

## Contribuições

Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

---

**Bons estudos!** 🎯🔥