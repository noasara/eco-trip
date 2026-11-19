import os
from flask import Flask

def create_app():
	
	app = Flask(__name__, static_url_path='/static')
	
	app.config['DATABASE_PATH'] = os.path.join(app.root_path, 'ecotrip.db')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_PATH']
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	app.config['SESSION_COOKIE_SECURE'] = False # car on dev
	app.secret_key = 'ma cle secrete unique'

	from app.blueprints import index_bp, api_bp
	app.register_blueprint(index_bp)
	app.register_blueprint(api_bp, url_prefix='/api')
	
	return app