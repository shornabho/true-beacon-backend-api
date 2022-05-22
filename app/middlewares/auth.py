from fastapi import Request, HTTPException, WebSocket, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import get_database_session
from app.models.user import User

from app.utils.auth import decodeJwt

class JWTBearer(HTTPBearer):
    """    
    Custom Authentication middleware on top of HTTPBearer class for validating Bearer JSON Web Tokens in the Authorization header of API requests.
    """

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> User:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, detail="Invalid authentication scheme.")

            # Parse JWT Payload
            payload = decodeJwt(credentials.credentials)

            # If invalid payload, i.e., invalid JWT
            if not payload:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token.")

            # Check if user exists in db
            try: 
                db = next(get_database_session())
                user = db.query(User).filter(User.username == payload['username']).first()

            except Exception as e: 
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unknown error occurred")

            finally:
                db.close()

            if not user:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token.")
            
            return user

                
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")




async def authenticateWebsocketConnection(websocket: WebSocket, token: str):

    # Parse JWT Payload
    payload = decodeJwt(token)

    # If invalid token structure
    if not payload:
        await websocket.close(code=403, reason="Invalid token.")
        return

    # Check if user exists in db
    try: 
        db = next(get_database_session())
        user = db.query(User).filter(User.username == payload['username']).first()

    except Exception as e: 
        await websocket.close(code=403, reason="Invalid token.")
        return False

    finally:
        db.close()

    if not user:
        await websocket.close(code=403, reason="Invalid token.")
        return False
    
    return True