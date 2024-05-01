"""
Startup da aplicação.
"""
import logging
import os



from app import create_app

root_logger = logging.getLogger("core")

APP_ENV = os.getenv("APP_ENV", 'Development')

application = create_app('ais_server.config.default.' + APP_ENV)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=False, port=5000, use_reloader=True)
