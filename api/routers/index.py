from . import orders, users, ratings_reviews, menu_items


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(users.router)
    app.include_router(ratings_reviews.router)
    app.include_router(menu_items.router)
