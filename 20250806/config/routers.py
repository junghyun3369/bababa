from fastapi import APIRouter
from config.urls import urls
api_config = {
    "title":"UV API",
    "version":"0.0.1",
    "docs_url":"/api_docs",
    "redoc_url":None
}
# ctr1_config = {
#     "router": root.ctr1,
#     "prefix":"/docs",
#     "tags": ["기능1"]
# }
# ctr2_config = {
#     "router": root.ctr1,
#     "prefix":"/docs",
#     "tags": ["기능2"]
# }

ctrs = []
for link in urls:
  ctr = APIRouter()
  router = {
    "prefix":link["prefix"],
    "tags":link["tags"],
	}
  for item in link["urls"]:
  	ctr.add_api_route(**item)
      
router["router"] = ctr
ctrs.append(router)  
# [ctr1_config, ctr2_config]
