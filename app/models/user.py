from pydantic import BaseModel

from sqlalchemy import Column, Integer, String
from app.database import Base


##################
# Request Models #
##################


class UserRegisterModel(BaseModel):
    """

    Request model for registering a user.

    Attributes:
    -----------
    username (String): Unique username of the user.

    name (Float): User's full name.

    password (Float): Password for the user's account.


    """

    username: str
    name: str
    password: str


class UserLoginModel(BaseModel):
    """

    Request model for logging in a user.

    Attributes:
    -----------
    username (String): Unique username of the user.

    name (Float): User's full name.

    password (Float): Password for the user's account.


    """

    username: str
    password: str


###################
# Database Models #
###################


class User(Base):
    """

    Represents a single User entity in the database.

    Attributes:
    -----------
    id (Integer): Autoincrement ID of the User.

    username (String): Unique username of the user.

    name (Float): User's full name.

    password (Float): Password for the user's account.


    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)
