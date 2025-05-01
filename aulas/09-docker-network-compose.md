7257  docker network ls
 7259  docker network create minha_rede
 7260  docker network ls
 7261  docker run -d --name containerA --network minha_rede nginx
 7262  docker network
 7263  docker network ls
 7264  docker network inspect minha_rede
 7265  docker run -d --name containerB --network minha_rede nginx
 7266  docker network ls
 7267  docker ps
 7268  docker inspect -f {{range .NetworkSettings.Network}}{{.IPAddress}}{{end}}'
 7269  docker inspect -f {{range .NetworkSettings.Network}}{{.IPAddress}}{{end}}' containerA
 7270  docker inspect -f '{{range .NetworkSettings.Network}}{{.IPAddress}}{{end}}' containerA
 7271  docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerA
 7272  docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerB
 7273  docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerA
 7274  docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerB
 7275  docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerA
 7276  docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerB
 7277  docker exec -it containerA /bin/sh
 7278  docker exec -it containerA /bin/bash
 7279  l
 7280  cd fiap
 7281  ls
 7282  cd cloud-developer-2TCNPZ
 7283  git pull
 7284  code .
 7285  ls
 7286  cd projetos
 7287  ls
 7288  docker-compose
 7289  docker-compose up --build
 7290  docker-compose logs 
 7291  docker-compose up --build
 7292  pwd
 7293  ls
 7294  cd e-commerce
 7295  ls
 7296  docker-compose up --build
 7297  docker ps
 7298  git 
 7299  git status
 7300  git add .
 7301  git commit -a -m "Added docker-compose"
 7302  git push