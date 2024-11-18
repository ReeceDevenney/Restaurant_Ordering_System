from . import orders, order_details, recipes, sandwiches, resources

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    users.Base.metadata.create_all(engine)
    payment_information.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    resource_management.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    ratings_reviews.Base.metadata.create_all(engine)
