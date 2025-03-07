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
    && apt-get clean

# Baixar e instalar o wkhtmltopdf
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.bullseye_amd64.deb && \
    dpkg -i wkhtmltox_0.12.6.1-2.bullseye_amd64.deb && \
    apt-get install -f -y && \
    rm wkhtmltox_0.12.6.1-2.bullseye_amd64.deb

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