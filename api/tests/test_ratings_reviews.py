from fastapi.testclient import TestClient
from ..controllers import ratings_reviews as controller
from ..main import app
import pytest
from ..models import ratings_reviews as model
from ..schemas import ratings_reviews as schema

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_rating_review(db_session):
    # Create a sample rating and review data
    rating_review_data = {
        "rating": 4.5,
        "review": "Great product, highly recommend!",
        "item_id": 1
    }

    # Call the API endpoint to create a rating/review
    response = client.post("/ratings_reviews/", json=rating_review_data)

    # Assertions
    assert response.status_code == 200
    assert response.json()["rating"] == 4.5
    assert response.json()["review"] == "Great product, highly recommend!"
    assert response.json()["item_id"] == 1


def test_read_all_rating_reviews(db_session):
    # Mock data to return when reading all ratings/reviews
    mock_ratings_reviews = [
        {"rating": 5.0, "review": "Excellent!", "item_id": 1},
        {"rating": 3.0, "review": "Okay, could be better", "item_id": 2}
    ]

    # Mock the controller to return the mock data
    controller.read_all = lambda db: mock_ratings_reviews

    # Call the API endpoint to fetch all ratings/reviews
    response = client.get("/ratings_reviews/")

    # Assertions
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["rating"] == 5.0
    assert response.json()[1]["review"] == "Okay, could be better"


def test_read_one_rating_review(db_session):
    # Mock data to return for a specific rating/review by item_id
    mock_rating_review = {"rating": 4.0, "review": "Good, but could improve.", "item_id": 1}

    # Mock the controller to return the mock data
    controller.read_one = lambda db, item_id: mock_rating_review

    # Call the API endpoint to fetch a specific rating/review by item_id
    response = client.get("/ratings_reviews/1")

    # Assertions
    assert response.status_code == 200
    assert response.json()["rating"] == 4.0
    assert response.json()["review"] == "Good, but could improve."
    assert response.json()["item_id"] == 1


def test_update_rating_review(db_session):
    # Create a sample updated rating and review data
    updated_data = {
        "rating": 4.0,
        "review": "Updated review text.",
        "item_id": 1  # Assuming you're updating the rating/review for item with id 1
    }

    # Mock the controller update function to return the updated data
    controller.update = lambda db, request, item_id: {**updated_data, "item_id": item_id}

    # Call the API endpoint to update the rating/review
    response = client.put("/ratings_reviews/1", json=updated_data)

    # Assertions
    assert response.status_code == 200
    assert response.json()["rating"] == 4.0
    assert response.json()["review"] == "Updated review text."
    assert response.json()["item_id"] == 1


def test_delete_rating_review(db_session):
    # Mock the controller delete function to return a success message
    controller.delete = lambda db, item_id: {"message": "Rating/Review deleted successfully"}

    # Call the API endpoint to delete a rating/review by item_id
    response = client.delete("/ratings_reviews/1")

    # Assertions
    assert response.status_code == 200
    assert response.json()["message"] == "Rating/Review deleted successfully"


def test_get_worst_dishes(db_session):
    # Mock the controller get_worst_dishes function to return a filtered list
    mock_worst_dishes = [
        {"rating": 2.5, "review": "Not great.", "item_id": 1},
        {"rating": 3.0, "review": "Below average.", "item_id": 2}
    ]

    # Mock the controller function
    controller.get_worst_dishes = lambda db, threshold: mock_worst_dishes

    # Call the API endpoint to fetch worst dishes with a threshold of 3.0
    response = client.get("/ratings_reviews/worst?threshold=3.0")

    # Assertions
    assert response.status_code == 200
    assert len(response.json()) == 2  # Expecting two dishes below the threshold
    assert response.json()[0]["rating"] == 2.5
    assert response.json()[1]["review"] == "Below average."
