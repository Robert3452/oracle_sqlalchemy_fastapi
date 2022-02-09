from sqlalchemy.orm import Session
from models.Product import Product
from typing import List
from schemas.Product import Product as ProductSchema


def get_products(session: Session):
    return session.query(Product).all()


def get_product(session: Session, id: int) -> Product:
    product = session.query(Product).get(id)
    if product is None:
        return False
    return product


def create_product(session: Session, payload_prod: ProductSchema):
    product_info = session \
        .query(Product) \
        .filter(Product.name == payload_prod.name) \
        .first()
    if product_info is not None:
        return False

    new_product = Product(**payload_prod.dict())
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product


def update_product(session: Session, id: str, payload_prod):
    product = get_product(session, id)

    if product is None:
        return False

    product.name = payload_prod.name if payload_prod.name is not None else product.name
    product.price = payload_prod.price if payload_prod.price is not None else product.price
    product.stock = payload_prod.stock if payload_prod.stock is not None else product.stock
    product.long_description = payload_prod.long_description if payload_prod.long_description is not None else product.long_description
    product.image = payload_prod.image if payload_prod.image is not None else product.image

    session.commit()
    session.refresh(product)
    return product


def delete_product(session: Session, id: int):
    product = get_product(session, id)

    if product is None:
        return False

    session.delete(product)
    session.commit()

    return True
