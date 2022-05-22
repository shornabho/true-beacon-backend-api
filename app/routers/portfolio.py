from typing import Dict
from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.database import get_database_session
from app.middlewares.auth import JWTBearer, authenticateWebsocketConnection
from app.models.user import User
from app.utils.auth import decodeJwt

router = APIRouter(prefix="/portfolio")

@router.get('/holdings', status_code=status.HTTP_200_OK)
async def get_holdings(user: User = Depends(JWTBearer())) -> Dict:
    """Controller method to get all holdings for the current user - (Dummy endpoint).

    Args:
        user (User, optional): Dependency injection for authentication middleware.

    Returns:
        Dict: A dict (JSON Object) containing the list of holdings.
    """
    
    return {
        "status": "success",
        "data": [
            {
                "tradingsymbol": "GOLDBEES",
                "exchange": "BSE",
                "isin": "INF204KB17I5",
                "quantity": 2,
                "authorised_date": "2021-06-08 00:00:00",
                "average_price": 40.67,
                "last_price": 42.47,
                "close_price": 42.28,
                "pnl": 3.5999999999999943,
                "day_change": 0.18999999999999773,
                "day_change_percentage": 0.44938505203405327
            },
            {
                "tradingsymbol": "IDEA",
                "exchange": "NSE",
                "isin": "INE669E01016",
                "quantity": 5,
                "authorised_date": "2021-06-08 00:00:00",
                "average_price": 8.466,
                "last_price": 10,
                "close_price": 10.1,
                "pnl": 7.6700000000000035,
                "day_change": -0.09999999999999964,
                "day_change_percentage": -0.9900990099009866
            }
        ]
    }
