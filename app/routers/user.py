from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import bcrypt

from app.database import get_database_session

from app.models.user import UserLoginModel, UserRegisterModel, User

from app.middlewares.auth import JWTBearer
from app.utils.auth import signJwt

router = APIRouter(prefix="/user")

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(response: Response, body: UserRegisterModel, db: Session = Depends(get_database_session)):
    """Controller method to register a new user.

    Args:
        response (Response): Response object provided by FastAPI
        body (UserRegisterModel): Accepted payload model for the POST request.
        db (Session, optional): Dependency Injection for database connection.

    Raises:
        HTTPException: Status Code 409 CONFLICT when user already exists in the database.

    Returns:
        Dict: A dict (JSON Object) containing username, name and the signed Json Web Token.
    """

    # Hash user input plain text password
    hashedPassword = bcrypt.hashpw(body.password.encode('utf-8'), bcrypt.gensalt())

    try: 
        # Save new user to db
        user = User(username=body.username, name=body.name, password=hashedPassword)
        db.add(user)
        db.commit()

        # Refresh after db update to get updated user instance
        db.refresh(user)

        # Sign JWT
        accessToken = signJwt(user.username)

        return {
            'status': 'success',
            'data': {
                'user': {
                    'username': user.username,
                    'name': user.name,
                },
                'token': accessToken
            }
        }

    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists.")

    finally: 
        db.close()
    

@router.post('/login', status_code=status.HTTP_200_OK)
async def login_user(body: UserLoginModel, db: Session = Depends(get_database_session)):
    """Controller method to login an existing user.

    Args:
        body (UserLoginModel): Accepted payload model for the POST request.
        db (Session, optional): Dependency Injection for database connection.

    Raises:
        HTTPException: Status Code 401 UNAUTHORIZED when credentials provided are incorrect.

    Returns:
        Dict: A dict (JSON Object) containing username, name and the signed Json Web Token.
    """

    # Fetch user by username
    user: User = db.query(User).filter(User.username == body.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")

    # Verify password
    isPasswordCorrect = bcrypt.checkpw(body.password.encode('utf-8'), user.password)
    if (not isPasswordCorrect):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    
    # Sign JWT
    accessToken = signJwt(user.username)

    return {
        'status': 'success',
        'data': {
            'user': {
                'username': user.username,
                'name': user.name,
            },
            'token': accessToken
        }
    }
    

@router.get('/profile', status_code=status.HTTP_200_OK)
async def get_user_profile(request: Request, db: Session = Depends(get_database_session), user: User = Depends(JWTBearer())):
    """Controller method to get the user's profile details - (Dummy endpoint).

    Args:
        request (Request):  Request object provided by FastAPI.
        db (Session, optional): Dependency Injection for database connection.
        user (User, optional): Authentication middleware for Authorization header verification 
                               and further returns the current user object to controller method body.

    Returns:
        Dict: A dict (JSON Object) containing the user profile information (Partly dummy response).
    """

    return {
        "status": "success",
        "data": {
            "user_id": user.username,
            "user_type": "individual",
            "email": "xxxyyy@gmail.com",
            "user_name": user.name,
            "broker": "ZERODHA"
        }
    }


    