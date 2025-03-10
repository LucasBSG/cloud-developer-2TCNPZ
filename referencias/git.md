# Fluxo de Trabalho para os Alunos

1. Criar uma Branch: 
   Cada aluno deverá criar uma branch com o nome do nome-aluno ou nome-sobrenome-aluno para trabalhar no desafio:

```
git checkout -b ricardo-desafio-1
```

2. Trabalhar no Desafio:
O aluno navega até a pasta do desafio correspondente e criará a sua pasta (ex: cloud-developer-2TCNPZ/desafios/desafio3/alunos/ricardo).

**Cria os arquivos necessários (ex: Dockerfile, docker-compose.yml, etc.) dentro de sua pasta.**

3. Commit e Push:
O aluno faz commit das alterações:

```
git add .
git commit -m "Desafio 3 - Aluno 3"
```
E envia para o repositório remoto:

```
git push origin aluno-1-desafio-1
```

4. Criar um Pull Request (PR):

- O aluno deverá cria um PR para que o professor possa revisar o código.

- No PR, precisa descrever o que foi feito e se há algo que precisa de atenção.

1. Revisão e Feedback:

O professor revisa o código no PR, poderá comentar e solicita alterações, se necessário.

Após a aprovação, o professor faz o merge do PR no branch principal, caso necessário.

##  Sincronizar o Fork com o Repositório Original
Os alunos podem sincronizar seus forks com o repositório original para obter as atualizações mais recentes. Aqui estão os passos para fazer isso:

1. Adicionar o Repositório Original como um Remote:

No terminal, navegue até o diretório do repositório forkado.

Adicione o repositório original como um remote chamado upstream:

```
git remote add upstream https://github.com/seu-usuario/seu-repositorio.git
```

2. Verifique se o remote foi adicionado corretamente:

```
git remote -v
```
3. Buscar as Alterações do Repositório Original:

Para buscar as alterações mais recentes do repositório original:

```
git fetch upstream
```

4. Mesclar as Alterações no Fork:

Agora, mescle as alterações do repositório original no branch principal do fork (geralmente main ou master):

```
git checkout main  # ou master, dependendo do branch principal
git merge upstream/main
```

5. Enviar as Alterações para o Fork no GitHub:

Após mesclar, envie as alterações para o fork no GitHub:

```
git push origin main
```
