## Certificado SSL

## DJANGO




## DOCKER

# build
docker build -t <nome-imagem> .

# stop container
docker stop <id-ou-nome-do-container>

docker ps -q

# remover
docker rm $(docker ps -a -q) - remover os container
docker rmi $(docker images) - remove todas as imagens

# run
docker run nome-da-imagem
docker run -p 8080:8080 <nome-da-imagem>

# iterativo
docker exec -it <nome-ou-id-do-container> /bin/bash

# Logs
docker logs <nome-ou-id-do-container>

# Listas 
docker ps


## DOCKER-COMPOSE
docker-compose up --build
