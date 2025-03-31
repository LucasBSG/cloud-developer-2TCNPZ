 
 # Criando e Iniciando o MySQL no Docker
Agora, montaremos o volume e subiremos o banco de dados com Docker:


```
docker volume create ecommerce-mysql-data
```

```
docker run -d --name ecommerce-mysql \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=ecommerce_db \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=pass \
  -p 3307:3306 \
  -v ecommerce-mysql-data:/var/lib/mysql \
  mysql:8.0

```

docker cp /Users/camanducci/fiap/cloud-developer-2TCNPZ/projetos/e-commerce/database/init.sql ecommerce-mysql:/docker-entrypoint-initdb.d/init.sql

docker exec -it ecommerce-mysql bash

docker exec -it ecommerce-mysql mysql -u root -p

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

```
use ecommerce_db;

show tables;

select * from clientes;
```