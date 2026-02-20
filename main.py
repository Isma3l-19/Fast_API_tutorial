from fastapi import FastAPI
from models import Product

app = FastAPI()

# landing page
@app.get("/")
def home():
    return "Welcome to the first tutorial"


products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop",description= "gaming laptop", price=999, quantity=6),
    Product(id=3, name="pen",description= "a blue ink pen", price=10, quantity=126),
    Product(id=4, name="table",description= "a wooden table", price=500, quantity=36)
]

# get products
@app.get("/products")
def get_all_products():
    return products