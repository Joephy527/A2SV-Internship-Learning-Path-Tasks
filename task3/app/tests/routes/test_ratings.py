from app.utils.rating_crud import create_rating
from app.models.rating_models import RatingCreate
from app.models.blogs_models import BlogCreate
from app.utils.blogs_crud import create_blog


def test_create_a_rating(
    client,
    db_session,
    create_test_user_for_rating,
    create_test_blog_for_rating,
    current_user_for_rating,
):
    response = client.post(
        f"/ratings/{create_test_blog_for_rating.blog_id}",
        json={"rating": 4},
        headers={"Authorization": f"Bearer {current_user_for_rating}"},
    )

    assert response.status_code == 200

    response_json = response.json()

    assert response_json["rating"] == 4


# def test_update_a_rating(
#     client,
#     db_session,
#     create_test_user_for_rating,
#     current_user_for_rating,
# ):
#     blog_data = BlogCreate(
#         title="test_blog",
#         content="test_blog_content",
#     )

#     blog = create_blog(
#         db=db_session, blog=blog_data, user_id=create_test_user_for_rating.user_id
#     )

#     response = client.post(
#         f"/ratings/{blog.blog_id}",
#         json={"rating": 4},
#         headers={"Authorization": f"Bearer {current_user_for_rating}"},
#     )

#     response = client.put(
#         f"/ratings/{blog.blog_id}",
#         headers={"Authorization": f"Bearer {current_user_for_rating}"},
#         json={"rating": 1},
#     )

#     assert response.status_code == 200

#     response_json = response.json()

#     assert response_json["rating"] == 1


def test_update_a_rating_by_other_user(
    client,
    create_test_blog_for_rating,
    create_another_test_user_for_rating,
    current_another_user_for_rating,
):
    response = client.put(
        f"/ratings/{create_test_blog_for_rating.blog_id}",
        headers={"Authorization": f"Bearer {current_another_user_for_rating}"},
        json={"update_tag_name": "update tag"},
    )

    assert response.status_code == 404

    response_json = response.json()

    assert response_json["detail"] == "Rating not found for the specified blog"
