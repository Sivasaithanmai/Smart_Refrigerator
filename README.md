About the Project

FridgeSense is a project I built to make managing a fridge smarter and easier. It keeps track of all your items, alerts you when things are close to expiry, and suggests groceries when stock is low. The project uses Python, FastAPI, and SQLite for a clean, scalable backend.

Even without a web frontend, it’s fully interactive through a CLI, and all logic is separated from the interface so it could easily be extended to a web or mobile app in the future.

Key Features

Item Management: Add, list, update, and remove items in the fridge.

Expiry Alerts: Automatically detect items nearing expiry.

Grocery Suggestions: Get a list of items that are low on stock.

Local ML-ready Structure: Backend ready for integrating offline food recognition in the future.

API Endpoints: Fully functional FastAPI endpoints, documented with Swagger UI.

Persistent Database: All items stored in SQLite, so changes are saved.

Automated Tests: Backend logic and API endpoints tested using pytest.
