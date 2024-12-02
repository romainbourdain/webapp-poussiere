from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.explorer import explorer_bp
    app.register_blueprint(explorer_bp)

    return app
