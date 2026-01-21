from sqlalchemy.orm import Session
from datetime import date
from app import models, schemas, rules

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        name=item.name,
        quantity=item.quantity,
        expiry_date=item.expiry_date,
        category=item.category
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session):
    return db.query(models.Item).all()

def get_expiring_items(db: Session, days: int = 3):
    return rules.get_expiring_items(db, days=days)

def get_grocery_suggestions(db: Session, min_quantity: int = 1):
    return rules.get_grocery_suggestions(db, min_quantity=min_quantity)
