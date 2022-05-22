import time
import jwt

from app.constants import JWT_SECRET, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES


def signJwt(username: str) -> str:
    payload = {
        "username": username,
        "expires": time.time() + (60 * JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    accessToken = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        'access_token': accessToken,
        'token_type': 'bearer'
    }

def decodeJwt(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload if payload["expires"] >= time.time() else None
    except:
        return None

