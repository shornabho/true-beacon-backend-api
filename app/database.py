from typing import Iterator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.constants import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_database_session() -> Iterator[Session]:
    """
    Database session generator. Used in Dependency Injection into controller method
    to establish and close connections from the SQLAlchemy connection pool.

    Yields:
        Session: A database session.
    """
    
    try: 
        db = SessionLocal()
        yield db
    finally:
        db.close()