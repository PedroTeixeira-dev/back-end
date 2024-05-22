from flask_openapi3 import Tag, APIBlueprint

tag = Tag(name='backlog', description="Some backlog")

backlog_api = APIBlueprint(
    '/backlog',
    __name__,
    url_prefix='/api',
    abp_tags=[tag],
)


@backlog_api.get('/backlog')
def get_backlog():
    return {"code": 0, "message": "ok"}
