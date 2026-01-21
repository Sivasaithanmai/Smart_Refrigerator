from app.database import SessionLocal, Base, engine
from app import models
from datetime import date, timedelta
import random
Base.metadata.create_all(bind=engine)
db = SessionLocal()
db.query(models.Item).delete()
db.commit()
items_list = [
    ("Milk", "dairy"), ("Cheese", "dairy"), ("Butter", "dairy"), ("Yogurt", "dairy"),
    ("Tomato", "vegetable"), ("Onion", "vegetable"), ("Spinach", "vegetable"), ("Carrot", "vegetable"),
    ("Apple", "fruit"), ("Banana", "fruit"), ("Orange", "fruit"), ("Grapes", "fruit"),
    ("Chicken", "meat"), ("Eggs", "meat"), ("Fish", "meat"), ("Mutton", "meat"),
    ("Bread", "bakery"), ("Rice", "grain"), ("Flour", "grain"),
    ("Juice", "beverage"), ("Coffee", "beverage"), ("Tea", "beverage"),
    ("Chips", "snack"), ("Biscuits", "snack"), ("Pickle", "condiment"), ("Sauce", "condiment"),
    ("Frozen Vegetables", "frozen"), ("Ice Cubes", "frozen")
]
for i in range(100):
    name, category = random.choice(items_list)
    quantity = random.randint(0, 10)
    
    if category in ["dairy", "meat", "frozen"]:
        expiry_days = random.randint(1, 10)
    elif category in ["vegetable", "fruit"]:
        expiry_days = random.randint(2, 7)
    else:
        expiry_days = random.randint(5, 30)
    
    expiry_date = date.today() + timedelta(days=expiry_days)

    db_item = models.Item(
        name=f"{name} #{i+1}",
        quantity=quantity,
        expiry_date=expiry_date,
        category=category
    )
    db.add(db_item)
db.commit()
print("Database seeded with 100+ professional fridge items.")
