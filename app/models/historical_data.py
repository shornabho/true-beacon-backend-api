from sqlalchemy import Column, DateTime, Float, Integer, String
from app.database import Base


###################
# Database Models #
###################


class HistoricalPrice(Base):
    """

    Represents a single Historical Price entity in the database.

    Attributes:
    -----------
    id (Integer): Autoincrement ID of the entity.

    date (DateTime): Date of the price.

    price (Float): Price of the stock on the mentioned date.

    symbol (String): Stock market symbol the price refers to.

    """

    __tablename__ = "historical_price"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    price = Column(Float)
    symbol = Column(String)
