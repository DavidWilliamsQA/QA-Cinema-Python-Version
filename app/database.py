from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST_NAME')}/{os.getenv('POSTGRES_DATABASE_NAME')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host=f"{os.getenv('POSTGRES_HOST_NAME')}",
#             database=f"{os.getenv('POSTGRES_DATABASE_NAME')}",
#             user=f"{os.getenv('POSTGRES_USERNAME')}",
#             password=f"{os.getenv('POSTGRES_PASSWORD')}",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("Database connected successfully!")
#         break
#     except Exception as error:
#         print()
#         print(error)
#         time.sleep(1)
