from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'gdwygd wgwhsd wjywueq ye827 93uqik'

    from .views import views
    app.register_blueprint(views, url)

    return app