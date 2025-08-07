# from fastapi import APIRouter
# from config.urls import urls

# ctr1 = APIRouter()
# for index in range(len(urls[0])):
#     ctr1.add_api_route(**urls[0][index])
    


# ctr1.add_api_route(**urls[0][0])
# ctr1.add_api_route(**urls[0][1])
# ctr1.add_api_route(**urls[0][2])
# ctr1.add_api_route(**urls[0][3])


# @ctr1.get(**urls[0]["get"])
# def root():
#     return{"test":"읽기"}
# @ctr1.post(**urls[0]["post"])
# def root():
#     return{"test":"수정"}
# @ctr1.put(**urls[0]["put"])
# def root():
#     return{"test":"입력"}
# @ctr1.delete(**urls[0]["delete"])
# def root():
#     return{"test":"삭제"}


# ctr1 = APIRouter(prefix="/ctr1")
# ctr2 = APIRouter(prefix="/ctr2")
# @ctr2.get("/")
# def test():
#     return{"test":2}
# @ctr2.get("/test")
# def test():
#     return{"test":"CTR2"}





# def root():
#     return{"test":1}