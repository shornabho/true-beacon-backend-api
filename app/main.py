import random
import asyncio

from fastapi import Depends, FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from app import models
from app.database import engine, get_database_session
from app.middlewares.auth import authenticateWebsocketConnection
from app.utils.helpers import loadHistoricalDataToDatabase

from app.routers import user, portfolio, historical_data, order

# Setup FastAPI Application
app = FastAPI()

# Add CORS Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Database Models
models.user.Base.metadata.create_all(bind=engine)
models.historical_data.Base.metadata.create_all(bind=engine)

# Load Dummy Historical Data in Database from CSV File
loadHistoricalDataToDatabase()

# Test welcome endpoint
@app.get("/")
def index():
    return {"Welcome": "True Beacon API"}

# Add Routers to Segregate API endpoints
app.include_router(historical_data.router)
app.include_router(user.router)
app.include_router(portfolio.router)
app.include_router(order.router)


# Websocket Routes
@app.websocket('/ws')
async def websocket_latest_price(websocket: WebSocket, token: str, db: Session = Depends(get_database_session)):
    """Controller method for dummy websocket endpoint to render random data for holdings and their prices.

    Args:
        websocket (WebSocket): The WebSocket connection object.
        token (str): Bearer access token of the user.
        db (Session, optional): Dependency Injection for database connection..
    """

    # Authenticate Websocket Connection
    if (not await authenticateWebsocketConnection(websocket, token)):
        return

    # Wait for connections
    await websocket.accept()

    try:

        while True:
            # Send data every 15 seconds
            await asyncio.sleep(15)

            # Send randomly generated data for demo purposes
            await websocket.send_json([
                {
                    "tradingsymbol": "GOLDBEES",
                    "exchange": "BSE",
                    "isin": "INF204KB17I5",
                    "quantity": 2,
                    "authorised_date": "2021-06-08 00:00:00",
                    "average_price": random.uniform(40, 50),
                    "last_price": random.uniform(40, 50),
                    "close_price": random.uniform(40, 50),
                    "pnl": random.uniform(-10, 10),
                    "day_change": random.uniform(-5, 5),
                    "day_change_percentage": random.uniform(-5, 5)
                },
                {
                    "tradingsymbol": "IDEA",
                    "exchange": "NSE",
                    "isin": "INE669E01016",
                    "quantity": 5,
                    "authorised_date": "2021-06-08 00:00:00",
                    "average_price": random.uniform(8, 12),
                    "last_price": random.uniform(8, 10),
                    "close_price": random.uniform(8, 10),
                    "pnl": random.uniform(-10,10),
                    "day_change": random.uniform(-5, 5),
                    "day_change_percentage": random.uniform(-5, 5)
                }
            ])

    except WebSocketDisconnect:
        print("Client disconnected")   
    except: 
        await websocket.close()
