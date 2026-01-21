from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date
from app.database import engine, get_db
from app.models import Base
from app.services import item_service

app = FastAPI()

Base.metadata.create_all(bind=engine)

class ItemIn(BaseModel):
    title: str
    count: int
    expires_on: date
    type: str

@app.post("/inventory")
def create_inventory_item(payload: ItemIn, db: Session = Depends(get_db)):
    return item_service.add_item(db, payload)

@app.get("/inventory")
def fetch_inventory(db: Session = Depends(get_db)):
    return item_service.fetch_all(db)

@app.get("/inventory/alerts")
def fetch_expiry_alerts(db: Session = Depends(get_db)):
    return item_service.expiry_alerts(db)

@app.get("/inventory/suggestions")
def fetch_purchase_suggestions(db: Session = Depends(get_db)):
    return item_service.purchase_suggestions(db)
