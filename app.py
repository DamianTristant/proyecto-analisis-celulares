from fastapi import FastAPI

app = FastAPI()

celulares = [
    {
        "id": 1,
        "marca": "Samsung",
        "modelo": "Galaxy S23",
        "precio": 1200,
        "almacenamiento_gb": 256
    },
    {
        "id": 2,
        "marca": "Apple",
        "modelo": "iPhone 14",
        "precio": 1500,
        "almacenamiento_gb": 128
    },
    {
        "id": 3,
        "marca": "Xiaomi",
        "modelo": "Redmi Note 12",
        "precio": 400,
        "almacenamiento_gb": 128
    }
]

@app.get("/")
def root():
    return {"message" : "API de celulares funcionando!"}

@app.get("/celulares")
def get_celulares():
    return celulares