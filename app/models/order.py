from pydantic import BaseModel


##################
# Request Models #
##################


class PlaceOrderModel(BaseModel):
    """

    Request model for purchasing a stock.

    Attributes:
    -----------
    symbol (String): Stock market symbol of the listing.

    price (Float): Price of the stock unit.

    quantity (Float): Number of stock units requested.


    """

    symbol: str
    price: float
    quantity: float
