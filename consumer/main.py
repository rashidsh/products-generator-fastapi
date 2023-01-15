import clickhouse_connect
import faust
from pydantic import BaseSettings, KafkaDsn


class Settings(BaseSettings):
    kafka_url: KafkaDsn

    clickhouse_host: str
    clickhouse_port: int
    clickhouse_username: str
    clickhouse_password: str
    clickhouse_secure: bool

    class Config:
        env_file = '.env'


settings = Settings()

app = faust.App('myapp', broker=settings.kafka_url)
topic = app.topic('new_product')


class Product(faust.Record):
    name: str
    description: str
    sku: int
    price: int


def init_db():
    clickhouse_client.command('''
        CREATE TABLE IF NOT EXISTS products (
        id UUID, created_at DateTime DEFAULT now(), name String, description String, sku UInt32, price UInt32,
        PRIMARY KEY(id)
        ) ENGINE MergeTree
    ''')


@app.agent(topic)
async def new_product(products):
    async for product in products:
        clickhouse_client.command(f'''
            INSERT INTO products (id, name, description, sku, price) VALUES 
            (generateUUIDv4(), '{product['name']}', '{product['description']}', {product['sku']}, {product['price']})
        ''')


clickhouse_client = clickhouse_connect.get_client(
    host=settings.clickhouse_host,
    port=settings.clickhouse_port,
    username=settings.clickhouse_username,
    password=settings.clickhouse_password,
    secure=settings.clickhouse_secure,
)

init_db()
