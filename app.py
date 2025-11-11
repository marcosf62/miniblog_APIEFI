from flask import Flask
from extensions import db, migrate, jwt
from config import Config
from models import User, Post, Comment

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from views.auth_views import RegisterAPI, LoginAPI
    app.add_url_rule("/api/register", view_func=RegisterAPI.as_view("register_api"))
    app.add_url_rule("/api/login", view_func=LoginAPI.as_view("login_api"))

    # Rutas de Posts y Comments
    from views.post_views import PostListAPI, PostDetailAPI
    from views.comment_views import CommentListAPI
    
    # Posts
    app.add_url_rule("/api/posts", view_func=PostListAPI.as_view("post_list_api"))
    app.add_url_rule("/api/posts/<int:post_id>", view_func=PostDetailAPI.as_view("post_detail_api"))

    # Comments
    app.add_url_rule("/api/posts/<int:post_id>/comments", view_func=CommentListAPI.as_view("comment_list_api"))

    return app

app = create_app()
