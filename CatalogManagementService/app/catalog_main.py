from fastapi import FastAPI
import uvicorn
from controller.catalog_controller import router

app = FastAPI()
app.include_router(router)