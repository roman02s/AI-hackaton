# API service

Этот модуль представляет собой сервис, который обеспечивает основную логику сервиса.

## Установка и запуск

Для запуска сценария требуется в ```config.env``` записать переменные окружения:
```bash
dbname={dbname}
dbuser={dbuser}
dbpassword={dbpassword}
dbhost={dbhost}
dbport={dbport}
API_KEY={API_KEY}
REPLICATE_API_TOKEN={REPLICATE_API_TOKEN}
```


Для установки и запуска, выполните следующие команды:

1. Соберите Docker образ:
   ```
   sudo docker build -t api:{version} .
   ```

2. Запустите Docker контейнер:
   ```
   sudo docker run -d --restart unless-stopped -p {port}:8000 -t --name api_service api:{version}
   ```

## Конфигурация

Для настройки api сервиса, отредактируйте файл `config.env`, который находится в корневой директории проекта. В этом файле вы можете указать токен вашего Telegram бота и другие параметры.

