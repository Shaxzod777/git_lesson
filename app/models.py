from datetime import datetime
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Boolean,Float,String,Text,ForeignKey
from app.database import Base


class User(Base):
    __tablename__="user"
    id:Mapped[int]=mapped_column(primary_key=True)
    full_name:Mapped[str]=mapped_column(String(50))
    address:Mapped[str]=mapped_column(Text)
    phone:Mapped[str]=mapped_column(String(17))
    email:Mapped[str]=mapped_column(String(17),nullable=True)
    hashed_pass:Mapped[str]=mapped_column(String)


class Food(Base):
    __tablename__="food"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    price:Mapped[float]=mapped_column(Float,nullable=False)
    discount_price:Mapped[float]=mapped_column(Float,nullable=True)
    description:Mapped[str]=mapped_column(Text)
    is_avialable:Mapped[bool]=mapped_column(Boolean,default=True)


class Order(Base):
    __tablename__="order"
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey('user.id'))
    food_id:Mapped[int]=mapped_column(ForeignKey('food.id'))
    address:Mapped[str]=mapped_column(Text)
    total_price:Mapped[float]=mapped_column(Float,nullable=True)
    status:Mapped[str]=mapped_column(String(20),default="new")




    


   