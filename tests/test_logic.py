from app import rules
from app.database import SessionLocal

def test_expiring_items():
    db = SessionLocal()
    items = rules.get_expiring_items(db, days=7)
    assert all(item.expiry_date is not None for item in items)
def test_grocery_suggestions():
    db = SessionLocal()
    items = rules.get_grocery_suggestions(db)
    assert all(item.quantity < 1 for item in items)
