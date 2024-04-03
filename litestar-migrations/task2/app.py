from litestar import Litestar, get


@get("/")
async def litestar_hello_world() -> str:
    return "Hello, World!"


app = Litestar([litestar_hello_world])
