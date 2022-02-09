from fastapi import APIRouter
from config.db import conn
from models.User import User as UserModel
from schemas.User import User, UserUpdate
from cryptography.fernet import Fernet
from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session

session = Session()

user = APIRouter()
key = Fernet.generate_key()
func = Fernet(key)


@user.get('/users')
def get_users():
    return conn.execute(select(UserModel)).fetchall()


@user.post('/users')
def create_user(payload: User):
    new_user = {
        "names": payload.names,
        "lastnames": payload.lastnames,
        "phone": payload.phone,
        "email": payload.email,
        "password": func.encrypt(payload.password.encode("utf-8"))
    }
    conn.execute(insert(UserModel).values(new_user))
    return

    # return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{id}")
def get_user(id: str):
    found_user = conn.execute(select(UserModel).where(UserModel.id == id)).first()
    return found_user


@user.delete("/users/{id}")
def delete_user(id: str):
    user_deleted = conn.execute(select().where(UserModel.id == id)).first()
    conn.execute(delete(UserModel).where(UserModel.id == id))
    return user_deleted


@user.put("/users/{id}", tags=["users"], response_model=User, description="Update user by id")
def update_user(id: str, payload: UserUpdate):
    user_payload = payload.dict()
    session.query(UserModel).filter_by(id=id).update(user_payload)
    # conn.execute(select(UserModel).where(UserModel.id == id)).first()
    return conn.execute(select(UserModel).where(UserModel.id == id)).first()
