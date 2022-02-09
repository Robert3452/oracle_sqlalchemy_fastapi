from fastapi import APIRouter, Depends
from config.db import get_db
from schemas.Product import Product as ProductSchema
from sqlalchemy.orm import Session
from controllers.product import get_product, create_product, get_products, delete_product, update_product
from typing import Any

router = APIRouter()

session: Session = Depends(get_db)


# API to get list of products info
@router.get('/products')
def list_products():
    prod_list = get_products(session)
    return prod_list


@router.post('/products')
def store_products(payload: ProductSchema):
    prod = create_product(session, payload)
    return prod


@router.put('/products/{id}')
def edit_product(id: str, payload: Any):
    # prod = update_product(session, id, payload)
    return {"message": id, "payload": payload}


@router.get('/products/{id}')
def show_product(id: int):
    prod = get_product(session, id)
    return prod


@router.delete('/products/{id}')
def delete_product(id: int):
    return delete_product(session, id)
