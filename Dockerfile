# Usar uma imagem base com Python
FROM python:3.9-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    xvfb \
    fontconfig \
    libxrender1 \
    libxext6 \
    libssl3 \
    pandoc \
    wkhtmltopdf \
    && apt-get clean

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do aplicativo
COPY . .

# Expor a porta 5000 (porta padrão do Flask)
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]