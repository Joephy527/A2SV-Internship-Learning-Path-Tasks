import os
import sys
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

from app.routes.blogs import router as blogs_router
from app.routes.blog_tags import router as blog_tags_router
from app.routes.comments import router as comments_router
from app.routes.followers import router as followers_router
from app.routes.likes import router as likes_router
from app.routes.login import router as login_router
from app.routes.ratings import router as ratings_router
from app.routes.search import router as search_router
from app.routes.shares import router as shares_router
from app.routes.tags import router as tags_router
from app.routes.users import router as users_router

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

# if __name__ == "main":
#     load_dotenv()

#     # if len(sys.argv) > 1:
#     #     os.environ["ENVIRONMENT"] = sys.argv[1]

#     uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8080)
