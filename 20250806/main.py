from fastapi import FastAPI
from config import routers
app = FastAPI(**routers.api_config)
for ctr in routers.ctrs:
    app.include_router(**ctr)


# from controller.root import ctr1, ctr2    
# app.include_router(**routers.ctr1_config)
# app.include_router(**routers.ctr2_config)
# app.include_router(ctr1,prefix="/ctr1",tags=["기능1"])
# app.include_router(ctr2)
# @app.get("/")
# def root():
#     return a