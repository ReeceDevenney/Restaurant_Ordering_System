from fastapi.testclient import TestClient
from ..controllers import promotions as controller
from ..main import app
import pytest
from ..models import promotions as model
from ..schemas.promotions import PromotionCreate, PromotionUpdate, Promotion

# Create a test client for the app
client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_promotion(db_session):
    # Create a sample promotion data
    promotion_data = {
        "code": "PROMO2024",
        "discount": 20.0,
        "isActive": True,
        "expirationDate": '2024-12-30 00:00:00'
    }
    promotion_object = PromotionCreate(**promotion_data)
    created_promotion = controller.create_promotion(db_session, promotion_object)

    # Assertions
    assert created_promotion is not None
    assert created_promotion.code == promotion_data["code"]
    assert created_promotion.discount == promotion_data["discount"]
    assert created_promotion.isActive == promotion_data["isActive"]


def test_get_promotion_by_code(db_session, mocker):
    # Create a sample promotion to add to the mock DB
    promotion_data = {
        "code": "PROMO2024",
        "discount": 20.0,
        "isActive": True,
        "expirationDate": '2024-12-30 00:00:00'
    }
    promotion_object = Promotion(**promotion_data)

    # Mock the database behavior
    mock_query = mocker.Mock()
    mock_query.filter.return_value.first.return_value = promotion_object
    db_session.query.return_value = mock_query

    # Call the controller function
    retrieved_promotion = controller.get_promotion_by_code(db_session, "PROMO2024")

    # Assertions
    assert retrieved_promotion is not None
    assert retrieved_promotion.code == promotion_data["code"]
    assert retrieved_promotion.discount == promotion_data["discount"]
    assert retrieved_promotion.isActive == promotion_data["isActive"]
    assert str(retrieved_promotion.expirationDate) == promotion_data["expirationDate"]


def test_update_promotion(db_session, mocker):
    # Create a sample promotion to add to the mock DB
    promotion_data = {
        "code": "PROMO2024",
        "discount": 20.0,
        "isActive": True,
        "expirationDate": '2024-12-30 00:00:00'
    }
    promotion_object = Promotion(**promotion_data)

    # Updated promotion data
    update_data = {
        "discount": 25.0,
        "isActive": False,
        "expirationDate": '2024-12-31 00:00:00'
    }
    update_object = PromotionUpdate(**update_data)

    # Mock the database behavior
    mock_query = mocker.Mock()
    mock_query.filter.return_value.first.return_value = promotion_object
    db_session.query.return_value = mock_query

    # Call the controller function
    updated_promotion = controller.update_promotion(db_session, "PROMO2024", update_object)

    # Assertions
    assert updated_promotion is not None
    assert updated_promotion.code == promotion_data["code"]
    assert updated_promotion.discount == update_data["discount"]
    assert updated_promotion.isActive == update_data["isActive"]
    assert str(updated_promotion.expirationDate) == update_data["expirationDate"]


def test_delete_promotion(db_session, mocker):
    promotion_data = {
        "code": "PROMO2024",
        "discount": 20.0,
        "isActive": True,
        "expirationDate": '2024-12-30 00:00:00'
    }
    promotion_object = model.Promotion(**promotion_data)

    # Mock the database behavior
    mock_query = mocker.Mock()
    mock_query.filter.return_value.first.return_value = promotion_object
    db_session.query.return_value = mock_query

    # Mock delete behavior
    db_session.delete = mocker.Mock()
    db_session.commit = mocker.Mock()

    # Call the controller function
    controller.delete_promotion(db_session, "PROMO2024")

    # Assertions
    assert db_session.delete.call_count == 1
    assert db_session.commit.call_count == 1
    db_session.delete.assert_called_with(promotion_object)
