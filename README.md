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


## Comandos úteis
# Build e sobe em produção
docker-compose up -d --build

# Ver logs do Django (Gunicorn)
docker-compose logs -f django

# Ver logs do NGINX
docker-compose logs -f nginx

# Aplicar migrações
docker-compose exec django python manage.py migrate

# Criar superuser
docker-compose exec django python manage.py createsuperuser

# Verificar arquivos estáticos
docker-compose exec django ls /app/static/
docker-compose exec nginx ls /app/static/
