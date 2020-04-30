from flask import Flask

from resources.products import products
import models


DEBUG=True
PORT=8000

app = Flask(__name__)

app.register_blueprint(products, url_prefix='/api/v1/products')


@app.route('/')
def helloWorld():
	return "hello"

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
