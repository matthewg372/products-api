from flask import Flask, jsonify, g
import models
import os
from resources.products import products
from resources.users import users
from resources.likes import likes
from flask_login import LoginManager
from flask_cors import CORS 




DEBUG=True
PORT=8000

app = Flask(__name__)
app.secret_key = "ajhskdjasdhkasdjhkaiudhajugjhgdjhsgfhgjskdhjkfhjashd"
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	try:
		return models.User.get_by_id(user_id)
	except models.DoesNotExist:
		return None 
@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data={'error': 'user not logged in'},
		message="you must be logged in to do this",
		status=401
	),401


cors = CORS(products, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(likes, origins=['http://localhost:3000'], supports_credentials=True)
cors = CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(products, url_prefix='/api/v1/products')
app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(likes, url_prefix='/api/v1/likes')

@app.before_request 
def before_request():
	print("you should see this before each request") 
	g.db = models.DATABASE
	g.db.connect()

@app.after_request 
def after_request(response):
	print("you should see this after each request") 
	g.db.close()
	return response 


if 'ON_HEROKU' in os.environ: 
	print('\non heroku!')
	models.initialize()

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
