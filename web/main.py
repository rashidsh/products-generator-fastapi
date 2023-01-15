from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.routers.routers import router
from app.settings import settings

app = FastAPI()
app.include_router(router)

register_tortoise(
    app,
    db_url=settings.db_url,
    modules={'models': ['app.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
