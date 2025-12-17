import requests
import json

url = "https://dummyjson.com/products/category/smartphones"

response = requests.get(url)
data = response.json()

with open("data/raw/celulares_raw.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Datos guardados correctamente")





