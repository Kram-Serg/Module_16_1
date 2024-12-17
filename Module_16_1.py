from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь №{user_id}'}


@app.get('/user/{user_name}/{user_age}')
async def info_user(user_name: str, user_age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {user_name}, возраст: {user_age}'}