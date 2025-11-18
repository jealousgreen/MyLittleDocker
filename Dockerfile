FROM python:3.9-slim
LABEL authors="Dilara"
# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY requirements.txt .

# Устанавливаем зависимости без кеша
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь исходный код в контейнер
COPY . .

# Открываем порт 5000 внутри контейнера
EXPOSE 5000

# Команда по умолчанию: запускаем наше Flask-приложение
CMD ["python", "app.py"]