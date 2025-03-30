 
 # Criando e Iniciando o MySQL no Docker
Agora, subimos o banco de dados com Docker e montamos o volume para rodar os scripts automaticamente:

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
docker attach ecommerce-mysql
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

❌ docker attach → Não funciona bem para MySQL, pois anexa ao processo do servidor.
🔹 IMPORTANTE: O docker attach pode exibir os logs do processo principal do container. No caso do MySQL, você pode não ter um shell interativo.



```
use ecommerce_db;

show tables;

select * from clientes;
```