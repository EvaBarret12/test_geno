# Используем базовый образ с установленным Python и Nginx
FROM python:3.9-slim

# Устанавливаем необходимые пакеты, включая Nginx
RUN apt-get update && apt-get install -y \
    nginx

# Копируем файл зависимостей Python
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем приложение
COPY app.py /app/app.py

# Копируем конфигурацию Nginx (если необходимо)
COPY nginx.conf /etc/nginx/nginx.conf

# Устанавливаем рабочую директорию
WORKDIR /app

# Открываем порты
EXPOSE 80

# Запускаем Nginx и приложение Python одновременно с помощью оболочки
CMD ["sh", "-c", "service nginx start && python /app/app.py"]

