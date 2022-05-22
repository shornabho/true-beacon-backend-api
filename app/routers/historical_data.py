from datetime import date, datetime
from typing import Dict, List, Tuple
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import DateTime, between, func
from sqlalchemy.orm import Session

from app.database import get_database_session
from app.models.historical_data import HistoricalPrice

router = APIRouter(prefix="/historical-data")


@router.get("/", status_code=status.HTTP_200_OK)
def get_historical_data(symbol: str, from_date: datetime, to_date: datetime, db: Session = Depends(get_database_session)) -> List[HistoricalPrice]:
    """Controller method to get historical price data filtered by @symbol from @from_date to @to_date.

    Args:
        symbol (str): Stock market symbol to filter the price by.
        from_date (datetime): Starting date for the price history.
        to_date (datetime): End date for the price history.
        db (Session, optional): Dependency Injection for database connection.

    Returns:
        List[HistoricalPrice]: List of Historical Price of @symbol stocks from @from_date to @to_date.
    """

    prices = db.query(HistoricalPrice).filter(HistoricalPrice.symbol == symbol).filter(between(HistoricalPrice.date, from_date, to_date)).all()

    return prices


@router.get("/symbols", status_code=status.HTTP_200_OK)
def get_historical_data_symbols(db: Session = Depends(get_database_session)) -> List[str]:
    """Controller method to get all possible symbols available in the database for Historical Price data.

    Args:
        db (Session, optional): Dependency Injection for database connection.

    Returns:
        List[str]: List of symbols of stocks available in the database.
    """

    # Get all distinct symbols
    symbols = db.query(HistoricalPrice.symbol).select_from(HistoricalPrice).distinct(HistoricalPrice.symbol).all()

    # Convert array of object to array of strings
    symbols = [symbol["symbol"] for symbol in symbols]

    return symbols


@router.get("/date-limits", status_code=status.HTTP_200_OK)
def get_date_limits(db: Session = Depends(get_database_session)) -> Dict[str, DateTime]:
    """Controller method to get the minimum and maximum dates between which Historical Price data is available in the database.

    Args:
        db (Session, optional): Dependency Injection for database connection. 

    Raises:
        HTTPException: Status Code 404 NOT Found when no data is found in the database.

    Returns:
        Dict[str, DateTime]: Returns a dict (JSON Object) with minDate and maxDate keys.
    """

    # Get minimum and maximum dates in the database
    response = db.query(func.min(HistoricalPrice.date), func.max(HistoricalPrice.date)).select_from(HistoricalPrice).first()

    # If no rows in the db, query will return None
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data in the database.")

    minDate, maxDate = response

    return {"minDate": minDate, "maxDate": maxDate}
