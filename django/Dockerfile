FROM python:3.12-slim

# Cria diretório da aplicação
WORKDIR /app

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instala dependências do sistema (evita erros de build)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Atualiza o pip
RUN pip install --upgrade pip

# Copia apenas o requirements.txt inicialmente para aproveitar cache
COPY requirements.txt /app/

# Instala dependências Python
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Copia o restante do projeto
COPY . /app/

RUN python manage.py collectstatic --noinput

# Comando padrão de inicialização
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

# Rodando com gunicorn
CMD ["gunicorn", "check_ssl.wsgi:application", "--bind", "0.0.0.0:8080", "--workers", "3"]
