from flask import Flask, request, render_template
from elections.vote import bp as vote_bp
from elections.db import db
from elections.config import SQLALCHEMY_URL

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_URL

db.init_app(app)

app.register_blueprint(vote_bp, url_prefix='/pages')
