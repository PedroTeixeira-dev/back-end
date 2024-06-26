from flask_openapi3 import OpenAPI, Info, Tag
from .sqlachemy import db, migrate
from .openapi import api


def create_app():
    info = Info(title="Minha API", version="1.0.0")

    app = OpenAPI(__name__, info=info)
    app.config.from_object("src.config.settings.Config")
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_api(api)
    return app
