from fastapi import FastAPI

from graphql_app import graphql_app
from models import models, database

app = FastAPI()
app.include_router(graphql_app, prefix="/api/graphql")


@app.on_event("startup")
async def startup_event():
    try:
        if not database.is_connected:
            await database.connect()
        await models.create_all()
    except Exception as e:  # noqa
        print(e)
        pass


@app.on_event("shutdown")
async def shutdown():
    try:
        if database.is_connected:
            await database.disconnect()
    except Exception:  # noqa
        pass
