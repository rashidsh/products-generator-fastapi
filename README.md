# products-generator-fastapi

## Установка

1. Скачайте или клонируйте репозиторий

2. Установите [Python](https://www.python.org/downloads) версии 3.10 или выше

3. Установите необходимые модули:
    ```bash
    pip install -r requirements.txt
    ```

4. Установите [PostgreSQL](https://postgresql.org/download/) и создайте базу данных

5. Установите [Kafka](https://kafka.apache.org/quickstart) и запустите сервер

6. Создайте базу данных ClickHouse на [clickhouse.cloud](https://clickhouse.cloud)

7. Скопируйте файл ```.env.example``` в ```.env``` и заполните его, используя таблицу параметров ниже

8. Запустите генератор данных:
    ```bash
    python producer/main.py
    ```

9. Запустите рабочий процесс Faust, сохраняющий данные из Kafka в базу данных:
    ```bash
    python consumer/main.py
    ```

10. Запустите веб-сервер FastAPI:
    ```bash
    uvicorn web.main:app --reload
    ```

## Конфигурация

| Параметр            | Описание                                   |
|---------------------|--------------------------------------------|
| DB_URL              | Строка параметров подключения к PostgreSQL |
| DB_POOL_SIZE        | Размер пула соединений с БД                |
| SECRET_KEY          | Секретный ключ FastAPI                     |
| KAFKA_URL           | Строка параметров подключения к Kafka      |
| CLICKHOUSE_HOST     | Хост БД ClickHouse                         |
| CLICKHOUSE_PORT     | Порт БД ClickHouse                         |
| CLICKHOUSE_USERNAME | Имя пользователя БД ClickHouse             |
| CLICKHOUSE_PASSWORD | Пароль пользователя БД ClickHouse          |
| CLICKHOUSE_SECURE   | Подключаться к БД ClickHouse по https?     |
