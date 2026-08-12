from fastapi import APIRouter

user_router=APIRouter(prefix='/user')


@user_router.post('/create')
def create_user():
    return {"message":"Foydalanuvchi yaratildi"}

@user_router.get('/list')
def get_users():
    return {"message":"Barcha foydalanuvchilar"}


@user_router.get('/profile')
def get_user_profile():
    return {"message":"Foydalanuvchi profili"}