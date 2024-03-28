import uuid
from datetime import datetime
from uuid import UUID

from app.schema import Comment
from app.models.comments_models import CommentCreate, CommentUpdate
from app.utils.comment_crud import create_comment, edit_comment, delete_comment
from app.models.blogs_models import BlogCreate
from app.utils.blogs_crud import create_blog


def test_create_comment(db_session, create_test_user):
    # Create a test user_id and blog_id
    user_id = create_test_user.user_id

    blog_data = BlogCreate(
        title="test_blog_for_comment_utils",
        content="test_blog_for_coment_utils_content",
    )

    blog = create_blog(db=db_session, blog=blog_data, user_id=user_id)

    blog_id = blog.blog_id

    # Create a test comment
    comment_data = CommentCreate(content="Test comment")

    # Call create_comment function
    new_comment = create_comment(db_session, user_id, blog_id, comment_data)

    # Assert that the comment is created
    assert isinstance(new_comment, Comment)
    assert new_comment.user_id == user_id
    assert new_comment.blog_id == blog_id
    assert new_comment.content == comment_data.content
    assert isinstance(new_comment.created_at, datetime)
    assert isinstance(new_comment.updated_at, datetime)


def test_edit_comment(db_session, create_test_user):
    test_user_id = create_test_user.user_id

    blog_data = BlogCreate(
        title="test_blog_for_comment_utils",
        content="test_blog_for_coment_utils_content",
    )

    blog = create_blog(db=db_session, blog=blog_data, user_id=test_user_id)

    blog_id = blog.blog_id

    test_comment = Comment(
        user_id=test_user_id,
        blog_id=blog_id,
        content="Test comment",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    db_session.add(test_comment)
    db_session.commit()

    updated_content = "Updated comment content"
    updated_data = CommentUpdate(content=updated_content)

    edited_comment = edit_comment(
        db_session, test_comment.comment_id, test_user_id, updated_data
    )

    assert edited_comment.content == updated_content


def test_edit_nonexisting_comment(db_session, create_test_user):
    test_user_id = create_test_user.user_id

    blog_data = BlogCreate(
        title="test_blog_for_comment_utils",
        content="test_blog_for_coment_utils_content",
    )

    blog = create_blog(db=db_session, blog=blog_data, user_id=test_user_id)

    blog_id = blog.blog_id

    test_comment_id = uuid.uuid4()

    updated_content = "Updated comment content"
    updated_data = CommentUpdate(content=updated_content)

    edited_comment = edit_comment(
        db_session, test_comment_id, test_user_id, updated_data
    )

    assert edited_comment is None


def test_delete_comment(db_session, create_test_user):
    test_user_id = create_test_user.user_id

    blog_data = BlogCreate(
        title="test_blog_for_comment_utils",
        content="test_blog_for_coment_utils_content",
    )

    blog = create_blog(db=db_session, blog=blog_data, user_id=test_user_id)

    blog_id = blog.blog_id

    test_comment = Comment(
        user_id=test_user_id,
        blog_id=blog_id,
        content="Test comment",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    db_session.add(test_comment)
    db_session.commit()

    # Call delete_comment function
    deleted_comment = delete_comment(db_session, test_comment.comment_id, test_user_id)

    # Assert that the comment is deleted
    assert deleted_comment is not None
    assert deleted_comment.comment_id == test_comment.comment_id
    assert deleted_comment.user_id == test_user_id


def test_nonexisting_comment(db_session, create_test_user):
    test_user_id = create_test_user.user_id

    blog_data = BlogCreate(
        title="test_blog_for_comment_utils",
        content="test_blog_for_coment_utils_content",
    )

    blog = create_blog(db=db_session, blog=blog_data, user_id=test_user_id)

    blog_id = blog.blog_id

    test_comment_id = uuid.uuid4()

    deleted_comment = delete_comment(db_session, test_comment_id, test_user_id)

    assert deleted_comment is None
