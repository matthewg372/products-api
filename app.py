from flask import Flask

from resources.products import products
import models
from resources.users import users

from flask_login import LoginManager

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






app.register_blueprint(products, url_prefix='/api/v1/products')
app.register_blueprint(users, url_prefix='/api/v1/users')


@app.route('/')
def helloWorld():
	return "hello"

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
