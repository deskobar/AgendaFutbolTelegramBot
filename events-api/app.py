from fastapi import FastAPI

from graphql_app import graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/api/graphql")
