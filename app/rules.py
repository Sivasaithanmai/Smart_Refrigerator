from datetime import date, timedelta
from sqlalchemy.orm import Session
from . import models, schemas
def get_expiring_items(db: Session, days: int = 3):
    """
    Return all items that are expiring within the next `days`.
    Default is 3 days.
    """
    today = date.today()
    threshold = today + timedelta(days=days)
    items = db.query(models.Item).filter(
        models.Item.expiry_date != None,
        models.Item.expiry_date <= threshold
    ).all()
    
    return [
        {
            "id": item.id,
            "name": item.name,
            "quantity": item.quantity,
            "expiry_date": item.expiry_date.isoformat(),
            "category": item.category
        } 
        for item in items
    ]

def get_grocery_suggestions(db: Session, min_quantity: int = 1):
    """
    Suggest items to buy based on low stock (quantity <= min_quantity)
    """
    items = db.query(models.Item).filter(models.Item.quantity <= min_quantity).all()
    
    return [
        {
            "id": item.id,
            "name": item.name,
            "quantity": item.quantity,
            "expiry_date": item.expiry_date.isoformat() if item.expiry_date else None,
            "category": item.category
        } 
        for item in items
    ]


def categorize_items(db: Session):
    """
    Categorize items based on simple keywords in name.
    Updates the database directly.
    """
    all_items = db.query(models.Item).all()
    categories = {
        "dairy": ["milk", "cheese", "butter", "yogurt"],
        "vegetables": ["tomato", "onion", "spinach", "carrot"],
        "fruits": ["apple", "banana", "orange", "mango"],
        "beverages": ["juice", "coffee", "tea"]
    }

    for item in all_items:
        for cat, keywords in categories.items():
            if any(word.lower() in item.name.lower() for word in keywords):
                item.category = cat
                db.commit()
                break
