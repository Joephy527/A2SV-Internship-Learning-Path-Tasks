import uuid
from app.models.users_models import UserCreate, UserUpdate
from app.utils.users_crud import create_user
from app.utils.auth import create_access_token


def test_user_create(client):
    response = client.post(
        "users/create/",
        json={
            "username": "test create",
            "email": "k@gmail.com",
            "password": "test_password",
            "name": "test_name",
            "bio": "test_bio",
            "role": "user",
        },
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["username"] == "test create"


def test_user_create_existing_username(client):
    response = client.post(
        "users/create/",
        json={
            "username": "test create",
            "email": "existing_email@gmail.com",
            "password": "test_password",
            "name": "test_name",
            "bio": "test_bio",
            "role": "user",
        },
    )
    assert response.status_code == 400

    response_json = response.json()

    assert response_json["detail"] == "Username already registered"


def test_user_create_missing_username(client):
    response = client.post(
        "users/create/",
        json={
            "email": "missing_username@gmail.com",
            "password": "test_password",
            "name": "test_name",
            "bio": "test_bio",
            "role": "user",
        },
    )
    assert response.status_code == 422


def test_read_user_existing_user(client, create_test_user):

    response = client.get(f"/users/{create_test_user.user_id}")

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["user_id"] == str(create_test_user.user_id)
    assert response_json["username"] == create_test_user.username
    assert response_json["email"] == create_test_user.email
    assert response_json["password"] == create_test_user.password
    assert response_json["role"] == create_test_user.role
    assert response_json["bio"] == create_test_user.bio


def test_read_user_non_existing_user(client):
    test_user_id = uuid.uuid4()

    response = client.get(f"/users/{test_user_id}")

    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_read_users_me(client, current_user):
    response = client.get(
        "users/me", headers={"Authorization": f"Bearer {current_user}"}
    )

    assert response.status_code == 200

    response_json = response.json()

    response_json["username"] == "test_user"


def test_update_existing_user(client, create_test_user, current_user):
    updated_data = UserUpdate(
        username="new_username",
        email="new_email@example.com",
        password="new_password",
        name="New Name",
        bio="New bio",
        profile_picture="new_profile_picture.jpg",
        role="user",
    )

    response = client.put(
        f"/users/{create_test_user.user_id}",
        json=updated_data.model_dump(),
        headers={"Authorization": f"Bearer {current_user}"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["username"] == updated_data.username


def test_update_existing_user_invalid_token(client, create_test_user, current_user):
    updated_data = UserUpdate(
        username="new_username",
        email="new_email@example.com",
        password="new_password",
        name="New Name",
        bio="New bio",
        profile_picture="new_profile_picture.jpg",
        role="user",
    )

    response = client.put(
        f"/users/{create_test_user.user_id}",
        json=updated_data.model_dump(),
        headers={"Authorization": f"Bearer {current_user}ds"},
    )

    assert response.status_code == 401


def test_update_existing_user(client, create_test_user, current_user):
    response = client.delete(
        f"/users/{create_test_user.user_id}",
        headers={"Authorization": f"Bearer {current_user}"},
    )

    assert response.status_code == 200
