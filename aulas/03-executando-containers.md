
# Instalação e Olá Mundo no Docker

## Instalando o Docker

1. **No Linux**:
   ```bash
   sudo apt-get update
   sudo apt-get install docker.io


   No Windows/Mac:

Baixe o Docker Desktop no site oficial: https://www.docker.com.


## 🐳 Primeiros Passos com Docker
Antes de criar o microserviço, vamos aprender alguns comandos básicos do Docker.

### 1️⃣ **Verificar a instalação do Docker**
```bash
docker --version
```

### 2️⃣ **Rodar o container Hello World**
```bash
docker run hello-world
```
📌 Esse comando baixa e executa um container simples que imprime "Hello World" no terminal.

### 3️⃣ **Listar containers em execução**
```bash
docker ps
```

### 4️⃣ **Listar todos os containers (inclusive os parados)**
```bash
docker ps -a
```

### 5️⃣ **Remover um container**
```bash
docker rm <CONTAINER_ID>
```

### 6️⃣ **Baixar uma imagem sem rodá-la**
```bash
docker pull nginx
```

### 7️⃣ **Rodar um container interativamente**
```bash
docker run -it ubuntu bash
```
📌 Isso inicia um container Ubuntu e abre um terminal dentro dele.

### 8️⃣ **Parar um container em execução**
```bash
docker stop <CONTAINER_ID>
```
