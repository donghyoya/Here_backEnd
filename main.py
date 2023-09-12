from fastapi import FastAPI
from domain.user.router import router as user_router
from domain.image.router import router as image_router
from domain.map.router import router as map_router
from domain.transaction.router import router as tran_router
app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(image_router,prefix="/image")
app.include_router(map_router,prefix="/map")
app.include_router(tran_router,prefix="/transaction")