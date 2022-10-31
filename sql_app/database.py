import os
from pyparsing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER: str = os.getenv("DB_USER", "root")
DB_PASS: Optional[str] = os.getenv("DB_PASS")
DB_HOST: str = os.getenv("DB_HOST", "db")
DB_PORT: str = os.getenv("DB_PORT", "3306")
DB_NAME: str = os.getenv("DB_NAME", "booking")

SQLALCEMY_DATABASE_URL: str = {
    f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    if DB_PASS
    else f"mysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
}

engine = create_engine(
    SQLALCEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
