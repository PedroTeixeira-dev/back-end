from flask_openapi3 import Tag
from ..config.openapi import api


# api = APIBlueprint(
#     '/book',
#     __name__,
#     url_prefix='/api',
#     abp_tags=[tag],
# )

@api.get('/book')
def get_book():
    return {"code": 0, "message": "ok"}
