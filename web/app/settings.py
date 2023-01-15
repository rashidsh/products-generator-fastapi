from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    db_url: PostgresDsn
    db_pool_size: int
    secret_key: str

    clickhouse_host: str
    clickhouse_port: int
    clickhouse_username: str
    clickhouse_password: str
    clickhouse_secure: bool

    class Config:
        env_file = '.env'


settings = Settings()
