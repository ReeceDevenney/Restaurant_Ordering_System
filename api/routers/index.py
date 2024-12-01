from importlib import resources

from . import orders, users, ratings_reviews, menu_items, resource_management, recipes


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(users.router)
    app.include_router(ratings_reviews.router)
    app.include_router(menu_items.router)
    app.include_router(resource_management.router)
    app.include_router(recipes.router)
