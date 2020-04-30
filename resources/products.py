import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# from flask_login import current_user

products = Blueprint('products', 'products')

@products.route('/', methods=['GET'])
def connected():
	return 'connected to Blueprint'


# @products.route('/', methods=['POST'])
# def create_products():
# 	payload = request.get_json()
# 	new_products = models.Product.create(
# 		name=payload['name'],
# 		user=current_user.id,
# 		flavors=payload['flavors'],
# 		quantity=payload['quantity'],
# 		price=payload['price']

# 	)
# 	product_dict = model_to_dict(new_products)
# 	return jsonify(
# 		data=product_dict,
# 		message="succesfully created product",
# 		status=200
# 	), 200