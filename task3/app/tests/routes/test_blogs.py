import uuid

from app.models.blogs_models import BlogCreate
from app.utils.blogs_crud import create_blog
from app.utils.auth import create_access_token


def test_create_blogs(client, create_test_user_for_blog, current_user_for_blog):
    response = client.post(
        "/blogs/create",
        json={"title": "test blog", "content": "test blog content"},
        headers={"Authorization": f"Bearer {current_user_for_blog}"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["title"] == "test blog"
    assert response_json["content"] == "test blog content"


def test_get_all_blogs(client, db_session, create_test_user_for_blog):
    blog_data = BlogCreate(
        title="test_blog",
        content="test_blog_content",
    )

    blog = create_blog(
        db=db_session, blog=blog_data, user_id=create_test_user_for_blog.user_id
    )

    response = client.get("/blogs/")

    assert response.status_code == 200

    response_json = response.json()

    assert response_json[0]["title"] == "test_blog"
    assert response_json[1]["title"] == "test blog"


def test_get_blog_by_id(client, db_session, create_test_user_for_blog):
    blog_data = BlogCreate(
        title="test_blog",
        content="test_blog_content",
    )

    blog = create_blog(
        db=db_session, blog=blog_data, user_id=create_test_user_for_blog.user_id
    )

    response = client.get(f"blogs/{blog.blog_id}")

    assert response.status_code == 200

    response_json = response.json()

    assert response_json[0]["title"] == "test_blog"


def test_get_nonexisting_blog_by_id(client, db_session, create_test_user_for_blog):
    test_blog_id = uuid.uuid4()

    response = client.get(f"blogs/{test_blog_id}")

    assert response.status_code == 404

    response_json = response.json()

    assert response_json["detail"] == "Blog not found"


def test_update_blog(
    client, db_session, create_test_user_for_blog, current_user_for_blog
):
    blog_data = BlogCreate(
        title="test_blog",
        content="test_blog_content",
    )

    blog = create_blog(
        db=db_session, blog=blog_data, user_id=create_test_user_for_blog.user_id
    )

    response = client.put(
        f"blogs/{blog.blog_id}",
        json={
            "title": "test_blog_update",
            "content": "test_blog_update_content",
        },
        headers={"Authorization": f"Bearer {current_user_for_blog}"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["title"] == "test_blog_update"


def test_update_nonexisting_blog_by_id(client, current_user_for_blog):
    test_blog_id = uuid.uuid4()

    response = client.put(
        f"blogs/{test_blog_id}",
        json={
            "title": "test_blog_update",
            "content": "test_blog_update_content",
        },
        headers={"Authorization": f"Bearer {current_user_for_blog}"},
    )

    assert response.status_code == 404

    response_json = response.json()

    assert response_json["detail"] == "Blog not found"


def test_update_blog_not_owner(
    client,
    db_session,
    create_test_user_for_blog,
    create_test_user_for_blog_not_owner,
    current_user_for_blog_not_owner,
):
    blog_data = BlogCreate(
        title="test_blog",
        content="test_blog_content",
    )

    blog = create_blog(
        db=db_session, blog=blog_data, user_id=create_test_user_for_blog.user_id
    )

    response = client.put(
        f"blogs/{blog.blog_id}",
        json={
            "title": "test_blog_update",
            "content": "test_blog_update_content",
        },
        headers={"Authorization": f"Bearer {current_user_for_blog_not_owner}"},
    )

    assert response.status_code == 403

    response_json = response.json()

    assert response_json["detail"] == "You are not the Owner of The Blog"


def test_delete_blog(
    client, db_session, create_test_user_for_blog, current_user_for_blog
):
    blog_data = BlogCreate(
        title="test_blog",
        content="test_blog_content",
    )

    blog = create_blog(
        db=db_session, blog=blog_data, user_id=create_test_user_for_blog.user_id
    )

    response = client.delete(
        f"blogs/{blog.blog_id}",
        headers={"Authorization": f"Bearer {current_user_for_blog}"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["title"] == "test_blog"


def test_delete_nonexisting_blog_by_id(client, current_user_for_blog):
    test_blog_id = uuid.uuid4()

    response = client.delete(
        f"blogs/{test_blog_id}",
        headers={"Authorization": f"Bearer {current_user_for_blog}"},
    )

    assert response.status_code == 404

    response_json = response.json()

    assert response_json["detail"] == "Blog not found"


def test_update_blog_not_owner(
    client,
    db_session,
    create_test_user_for_blog,
    create_test_user_for_blog_not_owner,
    current_user_for_blog_not_owner,
):
    blog_data = BlogCreate(
        title="test_blog",
        content="test_blog_content",
    )

    blog = create_blog(
        db=db_session, blog=blog_data, user_id=create_test_user_for_blog.user_id
    )

    response = client.delete(
        f"blogs/{blog.blog_id}",
        headers={"Authorization": f"Bearer {current_user_for_blog_not_owner}"},
    )

    assert response.status_code == 403

    response_json = response.json()

    assert response_json["detail"] == "You are not the Owner of The Blog"
