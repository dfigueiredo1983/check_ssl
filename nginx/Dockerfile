FROM nginx:alpine

# Remove o config padrão
RUN rm /etc/nginx/conf.d/default.conf

# Copia seu config customizado
COPY default.conf /etc/nginx/conf.d/

# (Opcional) Copia arquivos estáticos, se não usar volumes
# COPY ../django/staticfiles/ /app/staticfiles/

# Define o diretório de arquivos estáticos (se necessário no container)
# RUN mkdir -p /app/staticfiles
