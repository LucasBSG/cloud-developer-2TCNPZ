# Desafio: Configuração e Teste de Múltiplos Serviços com Docker Compose

## Objetivo
O objetivo deste desafio é praticar o uso do `docker-compose.yml` e `docker-compose.override.yml` para configurar, rodar e testar múltiplos serviços em contêineres. Você deverá configurar os serviços de uma aplicação completa, incluindo o banco de dados MySQL e os seguintes serviços:

- `clientes-service` (já implementado, pode ser usado como base)
- `estoque-service`
- `frete-service`
- `items-service`
- `lojas-service`
- `produtos-service`

Ao final, todos os serviços devem estar funcionando e se comunicando corretamente.

---

## Requisitos

1. **Banco de Dados MySQL**:
   - Configure o serviço `db` no `docker-compose.yml` para rodar o MySQL.
   - Certifique-se de que o banco de dados está acessível para os outros serviços.

2. **Serviços da Aplicação**:
   - Use o `clientes-service` como base para configurar os outros serviços.
   - Cada serviço deve:
     - Ter um `Dockerfile` para construir sua imagem.
     - Estar exposto em uma porta específica para testes.
     - Utilizar volumes para persistência de dados ou logs, se necessário.
     - Estar conectado à mesma rede (`ecommerce-network`).

3. **Configuração de Desenvolvimento**:
   - No arquivo `docker-compose.override.yml`, configure:
     - Variáveis de ambiente específicas para desenvolvimento (ex.: `DEBUG=true`).
     - Montagem de volumes para facilitar o desenvolvimento (ex.: código-fonte local montado no contêiner).

4. **Testes**:
   - Suba os contêineres com o comando `docker-compose up --build`.
   - Teste cada serviço individualmente:
     - Verifique se o banco de dados está acessível.
     - Teste as APIs dos serviços (ex.: usando `curl` ou Postman).
   - Certifique-se de que os serviços conseguem se comunicar entre si.

---

## Passos para Realizar o Desafio

1. **Configuração do `docker-compose.yml`**:
   - Adicione todos os serviços necessários.
   - Configure o banco de dados MySQL.
   - Certifique-se de que todos os serviços estão conectados à mesma rede.

2. **Configuração do `docker-compose.override.yml`**:
   - Adicione configurações específicas para o ambiente de desenvolvimento, como volumes e variáveis de ambiente.

3. **Construção e Execução**:
   - Suba os contêineres com o comando:
     ```bash
     docker-compose up --build
     ```
   - Verifique se todos os serviços estão rodando com:
     ```bash
     docker ps
     ```

4. **Testes**:
   - Teste o banco de dados:
     ```bash
     mysql -h 127.0.0.1 -P 3307 -u root -p
     ```
   - Teste os serviços da aplicação acessando suas APIs (ex.: `http://localhost:<porta>`).

5. **Finalização**:
   - Após os testes, encerre os contêineres com:
     ```bash
     docker-compose down
     ```

---

## Critérios de Avaliação

1. Todos os serviços estão configurados corretamente no `docker-compose.yml` e `docker-compose.override.yml`.
2. Os contêineres sobem sem erros.
3. Cada serviço está acessível e funcional.
4. Os serviços conseguem se comunicar entre si.
5. O uso correto de volumes e variáveis de ambiente no ambiente de desenvolvimento.

---

## Dicas

- Use o `clientes-service` como base para criar os outros serviços.
- Utilize logs para depurar problemas:
  ```bash
  docker-compose logs -f