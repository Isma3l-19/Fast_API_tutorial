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

# get all the products
@app.get("/products")
def get_all_products():
    return products

# getting product by id
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
        
    return "Product not found"

# Adding products
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


# updating products
@app.put("/products")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
    return "No product found"


# deleting products
@app.delete("/delete_product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product successfully deleted"
        
    return "Product not found"