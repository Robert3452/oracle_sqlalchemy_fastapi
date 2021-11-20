from fastapi import APIRouter
from config.db import conn
from models.Product import products
from schemas.Product import Product as ProductSchema
from sqlalchemy import desc, asc

product = APIRouter()


@product.get('/products')
def get_products():
    return conn.execute(products.select().order_by(asc(products.c.id))).fetchall()


@product.post('/products')
def store_product(payload: ProductSchema):
    new_product = {
        "name": payload.name,
        "description": payload.description,
        "image": payload.image,
        "long_description": payload.long_description,
        "price": payload.price,
        "stock": payload.stock,
        "enabled": payload.enabled if payload.enabled is not None else True
    }
    conn.execute(products.insert().values(new_product))
    found_user = conn.execute(products.select().order_by(desc(products.c.id))).first()
    return found_user.id
