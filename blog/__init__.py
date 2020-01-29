import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRECT_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'db.sqlite3')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return "HOME"

    from . import db
    db.init_app(app)

    from . import post
    app.register_blueprint(post.bp)

    return app