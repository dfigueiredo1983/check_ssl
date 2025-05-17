FROM nginx:alpine

# Remove o config padrão
RUN rm /etc/nginx/conf.d/default.conf

# Copia o seu arquivo de configuração customizado
COPY default.conf /etc/nginx/conf.d/
