from typing import Dict
import uuid
from fastapi import APIRouter, Depends, status

from app.middlewares.auth import JWTBearer
from app.models.order import PlaceOrderModel
from app.models.user import User


router = APIRouter(prefix="/order")

@router.post('/place-order', status_code=status.HTTP_201_CREATED)
async def place_order(order: PlaceOrderModel, user: User = Depends(JWTBearer())) -> Dict:
    """Controller method to place an order to buy stock units (Dummy endpoint).

    Args:
        order (PlaceOrderModel): Order details.
        user (User, optional): Dependency injection for authentication middleware.

    Returns:
        Dict: A dict containing a success message and randomly generated order id.
    """
    
    return {
        "status": "success",
        "data": {
            "message": "Order Placed Successfully",
            "order_id": uuid.uuid4()
        }
    }