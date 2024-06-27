# FROM node:16-alpine
# WORKDIR /app
# COPY package*.json ./
# RUN npm ci
# COPY . .
# ENV PORT=3000
# EXPOSE $PORT
# CMD ["npm", "start"]


# Используем официальный образ Python 3.9
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы вашего приложения в рабочую директорию контейнера
COPY . .

# Указываем команду для запуска FastAPI-приложения с помощью Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
