from fastapi import Depends,APIRouter,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import auth,models,schemas
from app.database import get_db


router=APIRouter(prefix="/auth")


@router.post('/register',response_model=schemas.UserOute,status_code=status.HTTP_201_CREATED)
def register_user(
    user_in:schemas.UserCreate,
    db:Session=Depends(get_db)):

    existing_user=db.query(models.User).filter(user_in.email==models.User.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Bu email allaqachon mavjud")
    

    new_user=models.User(
        full_name=user_in.full_name,
        email=user_in.email,
        phone=user_in.phone,
        address=user_in.address,
        hashed_pass=auth.hash_password(user_in.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




@router.post('/login',response_model=schemas.Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==form_data.username).first()

    if not user or not auth.verify_password(form_data.password,user.hashed_pass):
        raise HTTPException(status_code=401,detail="Email yoki parol xato")

    access_token=auth.create_access_token({"user_id":user.id})
    return schemas.Token(access_token=access_token)







    
