import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:1@localhost:5432/orderdb",
)

SECRET_KEY=os.getenv("SECRET_KEY","dars-uchun-maxfiy-kalit")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60


