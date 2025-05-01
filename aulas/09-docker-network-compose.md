# Aula sobre Docker Networking e Docker Compose
## 1. Bridge (Padrão)

```bash
docker network create --driver bridge minha_bridge
```
> Características:
> 
> - Rede isolada padrão para containers
> 
> - Comunicação entre containers na mesma bridge
> 
> - NAT para acesso externo
> 
> Uso típico:
> 
> - Ambiente de desenvolvimento local
> 
> - Aplicações isoladas no mesmo host

## 2. Host

```bash
docker network create --driver host minha_host
```
> Características:
>
> - Remove o isolamento de rede do container
>
> - Container usa a stack de rede do host diretamente
>
> - Sem sobrecarga de NAT
>
> Uso típico:
>
> - Quando performance de rede é crítica
>
> - Aplicações que precisam de acesso direto a portas do host

## 3. Overlay

```bash
docker network create --driver overlay minha_overlay
```

> Características:
>
> - Conecta múltiplos daemons Docker (Swarm)
> 
> - Comunicação entre containers em hosts diferentes
> 
> - Criptografia opcional
> 
> Uso típico:
>
> - Ambientes distribuídos (Docker Swarm)
>
> - Comunicação entre serviços em clusters

## 4. Macvlan

```bash
docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 minha_macvlan
```

> Características:
> 
> - Atribui endereço MAC ao container
> 
> - Aparece como dispositivo físico na rede
> 
> - Sem NAT, máximo desempenho
> 
> Uso típico:
> 
> - Migração de workloads legados
> 
> - Quando containers precisam aparecer como hosts físicos

## 5. None

```bash
docker network create --driver none minha_none
```

> Características:
> 
> - Container sem interface de rede
> 
> - Isolamento total
> 
> Uso típico:
> 
> - Containers que não precisam de rede
> 
> - Processos batch/offline


## Quando usar cada tipo?

| Tipo      | Cenário Recomendado                      | Performance | Isolamento |
|-----------|------------------------------------------|-------------|------------|
| Bridge    | Desenvolvimento local, maioria dos casos | Médio       | Alto       |
| Host      | Aplicações performance crítica           | Máximo      | Mínimo     |
| Overlay   | Cluster Docker Swarm                     | Médio       | Alto       |
| Macvlan   | Containers que precisam de MAC real      | Máximo      | Médio      |
| None      | Containers sem necessidade de rede       | -           | Total      |

## Boas Práticas para Networking

### Desenvolvimento:
- Use redes bridge com nomes significativos
- Crie redes específicas para cada projeto

### Produção:
- Considere macvlan para cargas pesadas
- Overlay para ambientes distribuídos
- Evite rede host a menos que necessário

### Segurança:
- Isole redes por função (frontend, backend, db)
- Use redes internas para comunicação entre serviços
- Restrinja acesso externo quando possível

## Comandos de Rede no Docker

### Listar redes disponíveis
```bash
docker network ls
```
### Criar uma nova rede bridge
```bash
docker network create minha_rede
```
Cria uma nova rede bridge personalizada chamada "minha_rede"

### Executar containers em uma rede específica

```bash
docker run -d --name containerA --network minha_rede nginx
docker run -d --name containerB --network minha_rede nginx
```
- --network: Conecta o container à rede especificada
- Containers na mesma rede podem se comunicar pelo nome (DNS automático)

### Inspecionar uma rede

```bash
docker network inspect minha_rede
```
Mostra detalhes da rede, incluindo containers conectados e configurações IP

### Verificar IP de um container

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerA
```
Formatação personalizada para extrair apenas o endereço IP do container

### Testar conectividade entre containers

```bash
docker exec -it containerA /bin/bash

# Dentro do container:
apt-get update && apt-get install -y iputils-ping  # Instala o pacote ping

ping containerB
```
- Observação: A imagem oficial do Nginx é baseada em Debian e não vem com o ping instalado por padrão

- O pacote iputils-ping precisa ser instalado para usar o comando ping

- A comunicação pode ser testada tanto pelo nome do container quanto pelo IP

### Acessar um container em execução

```bash
docker exec -it containerA /bin/bash
```
Entra no container de forma interativa com terminal bash

## Docker Compose

Construir e iniciar serviços

```bash
docker-compose up --build
```

- --build: Constrói as imagens antes de iniciar os containers

### Ver logs dos serviços

```bash
docker-compose logs
```
- Mostra os logs de todos os serviços definidos no docker-compose.yml

## Gerenciamento de Código

### Atualizar repositório local

```bash
git pull
```

### Commitar e enviar alterações

```bash
git add .
git commit -a -m "Added docker-compose"
git 
```