 
 # Criando e Iniciando o MySQL no Docker
Agora, montaremos o volume e subiremos o banco de dados com Docker:


```bash
docker volume create ecommerce-mysql-data
```

```bash
docker run -d --name ecommerce-mysql \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=ecommerce_db \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=pass \
  -p 3307:3306 \
  -v ecommerce-mysql-data:/var/lib/mysql \
  mysql:8.0

```

```bash
docker cp /Users/camanducci/fiap/cloud-developer-2TCNPZ/projetos/e-commerce/database/init.sql ecommerce-mysql:/docker-entrypoint-initdb.d/init.sql
```

```bash
docker exec -it ecommerce-mysql bash
```

```bash
mysql -u root -p

```

```sql
use ecommerce_db;
show tables;
source /docker-entrypoint-initdb.d/init.sql;
```

```bash
docker exec -it ecommerce-mysql mysql -u root -p
```

## Ou Copiar script e rodar no banco de dados "mysql>"

```sql
use ecommerce_db;

show tables;

select * from clientes;
```

>> Subindo script do banco automaticamente.


```
docker run -d   --name ecommerce-mysql   -e MYSQL_ROOT_PASSWORD=root   -e MYSQL_DATABASE=ecommerce_db   -e MYSQL_USER=user   -e MYSQL_PASSWORD=pass   -p 3307:3306   -v //c/Users/caman/projetos/cloud-developer-2TCNPZ/database/init.sql:/docker-entrypoint-initdb.d/init.sql   mysql:8.0
``` 

```
docker exec -it ecommerce-mysql mysql -u root -p
```

```
docker exec -it ecommerce-mysql bash
```

```
docker inspect --format '{{.Config.Cmd}}' ecommerce-mysql

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ecommerce-mysql

```

```
docker logs ecommerce-mysql
```

✅ docker exec -it ecommerce-mysql bash → Melhor opção para acessar o shell do container.

✅ docker exec -it ecommerce-mysql mysql -u root -p → Acesso direto ao MySQL.

```
docker exec -it ecommerce-mysql mysql -u root -p ecommerce_db < /Users/camanducci/fiap/cloud-developer-2TCNPZ/projetos/e-commerce/database/init.sql
```


 # Exemplo passo a passo de uso do docker tag:

## Passo 1: Crie uma conta no Docker Hub
Primeiro, você precisa de uma conta no Docker Hub. Se ainda não tiver uma, crie em https://hub.docker.com/.

## Passo 2: Faça login no Docker Hub
Se você já tem uma conta no Docker Hub, basta fazer login no seu terminal usando o comando:

```
docker login
```

Isso pedirá seu nome de usuário e senha. Após autenticação bem-sucedida, você poderá realizar operações de push e pull no Docker Hub.

## Passo 3: Crie sua imagem Docker
Se você já tem um container rodando e deseja fazer push dele para o Docker Hub, primeiro é necessário criar a imagem a partir do seu container. Suponha que você tenha um container chamado ecommerce-mysql.

Para criar uma imagem a partir do seu container, use o comando:

```
docker commit ecommerce-mysql your-username/ecommerce-mysql:v1
```

Aqui, your-username/ecommerce-mysql:v1 é o nome e a tag da sua imagem. Substitua your-username pelo seu nome de usuário do Docker Hub.

## Passo 4: Tag da imagem para o Docker Hub
Caso você já tenha criado a imagem localmente e queira enviá-la ao Docker Hub, certifique-se de taguear sua imagem corretamente com o nome do repositório do Docker Hub.

A tag é composta pelo seu nome de usuário no Docker Hub, seguido do nome do repositório e a tag da versão. Para taguear a imagem:

```
docker tag ecommerce-mysql your-username/ecommerce-mysql:v1
```

##  Criação manual (mais comum)
Acesse hub.docker.com, vá em:

→ Repositories → Create Repository
Escolha:

Nome (ex: minha-api)

Visibilidade (público ou privado)

Aqui, substitua your-username pelo seu nome de usuário e v1 pela versão desejada.

## Passo 5: Realize o Push da Imagem para o Docker Hub
Depois de fazer a tag da imagem, você pode push ela para o Docker Hub com o seguinte comando:

```
docker push your-username/ecommerce-mysql:v1
```

Isso enviará sua imagem para o Docker Hub e ela ficará disponível publicamente (ou privativamente, dependendo das configurações do seu repositório).

## Passo 6: Verifique a imagem no Docker Hub
Após o push, você pode verificar sua imagem acessando o Docker Hub, no painel de controle da sua conta. A imagem estará disponível no repositório que você especificou.

## Passo 7: Baixar (pull) a imagem em outro lugar
Agora que sua imagem está no Docker Hub, você pode usá-la em qualquer outro lugar. Para baixar a imagem, use:

```
docker pull your-username/ecommerce-mysql:v1
```

Isso irá baixar a imagem para o seu sistema local.

## Passo 8: Rodar o container a partir da imagem do Docker Hub
Depois de fazer o pull da imagem em outro sistema ou máquina, você pode rodar um container a partir dela:

```
docker run -d --name ecommerce-mysql -p 3307:3306 your-username/ecommerce-mysql:v1
```

Isso irá rodar um container a partir da imagem que você enviou ao Docker Hub.