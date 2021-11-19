from fastapi import APIRouter
from config.db import conn
from models.User import users
from schemas.User import User
from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
func = Fernet(key)


@user.get('/users')
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post('/users')
def create_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": func.encrypt(user.password.encode("utf-8"))
    }
    conn.execute(users.insert().values(new_user))
    users.select().where()
    return

    # return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{id}")
def get_user(id: str):
    found_user = conn.execute(users.select().where(users.c.id == id)).first()
    return found_user


@user.delete("/users/{id}")
def delete_user(id: str):
    user_deleted = conn.execute(users.select().where(users.c.id == id)).first()
    conn.execute(users.delete().where(users.c.id == id))
    return user_deleted


@user.put("/users/{id}", tags=["users"], response_model=User, description="Update user by id")
def update_user(id: str, user: User):
    conn.execute(
        users.update()
            .values(name=user, email=user.email, password=user.password)
            .where(users.c.id == id)
    )
    return conn.execute(users.select().where(users.c.id == id)).first()
