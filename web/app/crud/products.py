import clickhouse_connect

from app.settings import settings


class ProductsCRUD:
    def __init__(self):
        self.client = clickhouse_connect.get_client(
            host=settings.clickhouse_host,
            port=settings.clickhouse_port,
            username=settings.clickhouse_username,
            password=settings.clickhouse_password,
            secure=settings.clickhouse_secure,
        )

    def get_all(self, page, size):
        total = self.client.query('SELECT COUNT(*) FROM products').result_set[0][0]
        items = self.client.query(
            f'SELECT id, created_at, name, description, sku, price FROM products ORDER BY created_at DESC '
            f'LIMIT {size} OFFSET {size * (page - 1)}'
        ).named_results()

        return items, total


products_crud = ProductsCRUD()
