# 🚀 Como usar Volumes no Docker

## Criando um Volume Gerenciado pelo Docker

```
docker volume create meu_volume
```

2. Listando Volumes Existentes

```
docker volume ls
```

3. Inspecionando um Volume

```
docker volume inspect meu_volume
```

4. Usando um Volume em um Contêiner

```
docker run -d --name meu_volume -v meu-volume:/caminho/no/conteiner minha-imagem

ex:
docker run -d --name meu-container -v C:\AppData\://app/data nginx
```

```
docker exec -it ubuntu --name ubuntu /bin/bash
docker ps
docker attach ubuntu
```

> Se você digitar exit ou pressionar Ctrl + D dentro do contêiner, o processo principal do contêiner será encerrado, e o contêiner será parado.
> 
> Para evitar isso, use o atalho Ctrl + P + Ctrl + Q ou o método docker exec.



## Usando Bind Mounts

```
docker run -d --name meu-container -v /caminho/no/host:/caminho/no/conteiner minha-imagem
```

```
mkdir meu_app

echo "<h1>Olá, docker</h1>" > meu_app/index.html

docker run -d --name meu-nginx -v ${pwd}/meu_app:/usr/share/nginx/html -p

```

***Interpolação de variáveis de ambiente e ao uso de caminhos lógicos em comandos Docker***

>  ${PWD} para Mapear o Diretório Atual
> 
>  ${HOME} para Mapear o Diretório do Usuário
> 
>  $(pwd) no Linux e macOS


1. Removendo um Volume

```
docker volume rm meu-volume
```

7. Removendo Volumes Não Utilizados

```
docker volume prune
```

> O comando docker volume prune remove todos os volumes não utilizados no Docker. Um volume é considerado não utilizado se não estiver associado a nenhum contêiner em execução ou parado.


## Persistindo Dados em um Banco de Dados MySQL

1. Criando um Volume para o MySQL
```
docker volume create mysql-data
```

2. Executando um Contêiner MySQL com o Volume

```
docker run -d --name mysql-container -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=senha mysql:latest
```

3. Verificando Persistência de Dados

- Pare o contêiner:

```
docker stop mysql-container
```

- Reinicie o contêiner:

```
docker start mysql-container
```
