from fastapi import fastAPI

app=FastAPI()

@app.get("/")
def index():
    return "Hola a todos, quieres saber de Pokemon"