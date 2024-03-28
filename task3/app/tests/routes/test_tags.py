from app.utils.tags_crud import create_a_tag
from app.models.tag_models import TagCreate


def test_create_a_tag_by_admin(client, create_test_user_for_tag, current_user_for_tag):
    response = client.post(
        "/tags/",
        json={"tag_name": "Tag 1"},
        headers={"Authorization": f"Bearer {current_user_for_tag}"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["tag_name"] == "Tag 1"


def test_create_a_tag_by_user(
    client, create_test_user_for_tag_not_admin, current_user_for_tag_not_admin
):
    response = client.post(
        "/tags",
        headers={"Authorization": f"Bearer {current_user_for_tag_not_admin}"},
        json={"tag_name": "Unauthorized Tag"},
    )

    assert response.status_code == 403

    response_json = response.json()

    assert response_json["detail"] == "Only Admins Can Create a Tag"


def test_get_all_tags(client, db_session):
    tag2 = create_a_tag(db=db_session, tag_data=TagCreate(tag_name="Tag 2"))

    response = client.get("/tags/")

    assert response.status_code == 200

    response_json = response.json()

    assert response_json[0]["tag_name"] == "Tag 1"
    assert response_json[1]["tag_name"] == tag2.tag_name


def test_update_a_tag(client, current_user_for_tag):
    response = client.put(
        "/tags/Tag 1",
        headers={"Authorization": f"Bearer {current_user_for_tag}"},
        json={"update_tag_name": "update tag"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["tag_name"] == "update tag"


def test_update_a_tag_by_user(client, current_user_for_tag_not_admin):
    response = client.put(
        "/tags/Tag 1",
        headers={"Authorization": f"Bearer {current_user_for_tag_not_admin}"},
        json={"update_tag_name": "update tag"},
    )

    assert response.status_code == 403

    response_json = response.json()

    assert response_json["detail"] == "Only Admins Can Update a Tag"


def test_update_a_nonexisting_tag(client, current_user_for_tag):
    response = client.put(
        "/tags/Tag 1",
        headers={"Authorization": f"Bearer {current_user_for_tag}"},
        json={"update_tag_name": "update tag"},
    )

    assert response.status_code == 404

    response_json = response.json()

    assert response_json["detail"] == "Tag not Found"


def test_delete_a_tag(client, current_user_for_tag):
    response = client.delete(
        "/tags/Tag 2/",
        headers={"Authorization": f"Bearer {current_user_for_tag}"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["tag_name"] == "Tag 2"


def test_delete_a_tag_by_user(client, current_user_for_tag_not_admin):
    response = client.delete(
        "/tags/Tag 2/",
        headers={"Authorization": f"Bearer {current_user_for_tag_not_admin}"},
    )

    assert response.status_code == 403

    response_json = response.json()

    assert response_json["detail"] == "Only Admins Can Delete a Tag"


def test_delete_a_nonexisting_tag(client, current_user_for_tag):
    response = client.delete(
        "/tags/Tag 2/",
        headers={"Authorization": f"Bearer {current_user_for_tag}"},
    )

    assert response.status_code == 404

    response_json = response.json()

    assert response_json["detail"] == "Tag not Found"
