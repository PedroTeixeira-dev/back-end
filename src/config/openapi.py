from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag

tag = Tag(name='book', description="Some Book")

api = APIBlueprint(
    '/book',
    __name__,
    url_prefix='/api',
    abp_tags=[tag],
)
