from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel
import json

app = FastAPI()


@app.get("/")
def get_health():
    return json.dumps({"status": "healthy"})


def main():
    engine = create_engine("sqlite:///users.db")
    SQLModel.metadata.create_all(engine)
