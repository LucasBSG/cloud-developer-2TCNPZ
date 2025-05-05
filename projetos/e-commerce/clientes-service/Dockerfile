# Etapa 1: build (isolada)
FROM python:3.9-slim AS builder

# Variáveis de ambiente para segurança e consistência
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copiar arquivos e instalar dependências em um ambiente virtual
COPY requirements.txt .
RUN pip install --upgrade pip && \
  pip install --prefix=/install -r requirements.txt

# Etapa 2: runtime enxuto
FROM python:3.9-slim

WORKDIR /app

# Copiar apenas dependências instaladas e o app
COPY --from=builder /install /usr/local
COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
