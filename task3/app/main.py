from fastapi import FastAPI

from routes.blogs import router as blogs_router
from routes.blog_tags import router as blog_tags_router
from routes.comments import router as comments_router
from routes.followers import router as followers_router
from routes.likes import router as likes_router
from routes.login import router as login_router
from routes.ratings import router as ratings_router
from routes.search import router as search_router
from routes.shares import router as shares_router
from routes.tags import router as tags_router
from routes.users import router as users_router

app = FastAPI()

app.include_router(blogs_router)
app.include_router(blog_tags_router)
app.include_router(comments_router)
app.include_router(followers_router)
app.include_router(likes_router)
app.include_router(login_router)
app.include_router(ratings_router)
app.include_router(search_router)
app.include_router(shares_router)
app.include_router(tags_router)
app.include_router(users_router)
