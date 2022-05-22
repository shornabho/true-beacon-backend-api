import csv
from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from app.database import get_database_session
from app.models.historical_data import HistoricalPrice


def loadHistoricalDataToDatabase():
    historicalPricesFile = open("./historical_prices.csv")
    
    rows = csv.reader(historicalPricesFile)

    historicalPrices: List[HistoricalPrice] = []

    for row in rows:

        # Ignore first row
        if row[0] == '': 
            continue

        date = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S%z")
        historicalPrices.append(HistoricalPrice(date=date, price=row[2], symbol=row[3]))

    historicalPricesFile.close()

    db: Session = next(get_database_session())
    db.query(HistoricalPrice).delete()
    db.bulk_save_objects(historicalPrices)
    db.commit()

    db.close()
