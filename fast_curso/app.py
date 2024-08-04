from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_curso.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


# UserSchema é o de entrada e o UserPublic é o de saída
@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get("/users/", response_model=UserList)
def get_user():
    return {"users": database}


@app.get("/users/{user_id}", response_model=UserPublic)
def get_one_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="User not found")

    user_with_id = database[user_id - 1]
    return user_with_id


@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    # Se o usuário não existir exponha um erro ao usuário
    if user_id < 1 or user_id > len(database):
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="User not found")

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="User not found")

    user_with_id = {}
    database[user_id - 1] = user_with_id
    del database[user_id - 1]
    return {"message": "Usuário deletado com sucesso!"}
