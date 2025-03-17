# 🚀 Criando um Microserviço com Flask e Docker

## 🎯 Objetivo
Criar um microserviço simples em Python usando **Flask**, empacotá-lo em um container **Docker** e expô-lo na porta **5000**.

## 📌 Pré-requisitos
- Docker instalado ([Guia de instalação](https://docs.docker.com/get-docker/))
- Python 3.x instalado
- Editor de código (VS Code, PyCharm, etc.)

---

## 📂 Estrutura do Projeto
Crie uma pasta chamada `meu-microservico` e dentro dela crie os seguintes arquivos:

```bash
meu-microservico/
│-- app.py
│-- requirements.txt
│-- Dockerfile
```

### 📜 1. Criando o Microserviço `app.py`
Crie o arquivo `app.py` e adicione o seguinte código:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Microserviço rodando!"

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 📜 2. Criando o arquivo de dependências `requirements.txt`
Crie um arquivo chamado `requirements.txt` e adicione:

```
flask
```

Isso garante que o Docker instale as dependências corretamente.

### 📜 3. Criando o Dockerfile
Crie o arquivo `Dockerfile` com o seguinte conteúdo:

```dockerfile
# Usar uma imagem oficial do Python
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos para o container
COPY requirements.txt .
COPY app.py .

# Instalar as dependências
RUN pip install -r requirements.txt

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
```

---

## 🐳 Construindo e Rodando o Container

### 1️⃣ **Construir a imagem**
```bash
docker build -t meu-microservico .
```

### 2️⃣ **Rodar o container**
```bash
docker run -d -p 5000:5000 --name microservico meu-microservico
```

📌 **Explicação do parâmetro `-p 5000:5000`**:
- O primeiro `5000` é a porta no **host (seu computador)**.
- O segundo `5000` é a porta **dentro do container**.
- Se a porta **5000 já estiver em uso**, tente mudar para `-p 8080:5000` e acesse via `localhost:8080`.

### 3️⃣ **Testar os endpoints**
Abra o navegador ou use `curl` para testar:

- **Home:** `http://localhost:5000/`
- **Status:** `http://localhost:5000/status`

Ou via terminal:
```bash
curl http://localhost:5000/
curl http://localhost:5000/status
```

### 4️⃣ **Verificar logs do container**
```bash
docker logs microservico
```

### 5️⃣ **Parar e remover o container**
```bash
docker stop microservico && docker rm microservico
```

---

### 6️⃣ **Para ver e remover todas as imagens, você pode tentar**

- Ver todas as imagens no sistema

```bash
docker images -a
```

- Forçar a remoção das imagens não utilizadas
Se você quiser limpar todas as imagens que não estão sendo usadas por contêineres em execução:

```bash
docker image prune -a
```

- Esse comando remove todas as imagens não utilizadas por contêineres em execução, incluindo as que possuem tag.

Caso queira remover todas as imagens, execute:

```bash
docker rmi $(docker images -q) -f
```
O argumento -f força a remoção das imagens, mesmo se elas estiverem em uso.

---

### 7️⃣ **Criar e rodar um container simples (consumindo CPU e memória)**
- Crie um container que executa um loop infinito (usando a imagem alpine):

```bash
docker run -d --name stress-container alpine /bin/sh -c "while true; do :; done"
```

- Verificar o uso de recursos (CPU e memória)
Veja o uso de recursos do container em tempo real:

```bash
docker stats stress-container
```

- Limitar os recursos do container
Limitar o uso de CPU (por exemplo, limitar a 50% da CPU):

```bash
docker run -d --name limited-cpu --cpus="0.5" alpine /bin/sh -c "while true; do :; done"
```

- Limitar o uso de memória (por exemplo, limitar a 50MB de memória):

```bash
docker run -d --name limited-memory --memory="50m" alpine /bin/sh -c "while true; do :; done"
```

- Pausar o container
Pausa a execução de um container, suspende seu consumo de recursos (não consome CPU nem memória):

```bash
docker pause stress-container
```

- Retomar a execução do container pausado
Retoma a execução do container pausado:

```bash
docker unpause stress-container
```

- Parar o container
Finaliza o container, liberando recursos de forma controlada:

```bash
docker stop stress-container
```

- Iniciar um container parado
Inicia um container que foi parado anteriormente:

```bash
docker start stress-container
```
