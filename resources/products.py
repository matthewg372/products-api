import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

products = Blueprint('products', 'products')

"""index for specific logged in people"""
@products.route('/', methods=['GET'])
def products_index():
	current_user_product_dicts = [model_to_dict(product) for product in current_user.products]
	for product_dict in current_user_product_dicts:
		product_dict['user'].pop('password')
	return jsonify(
		data= current_user_product_dicts,
		message= f"Successfully found {len(current_user_product_dicts)} products",
		status= 200
	), 200

@products.route('/', methods=['POST'])
def create_products():
	payload = request.get_json()
	new_products = models.Product.create(
		name=payload['name'],
		user=current_user.id,
		flavors=payload['flavors'],
		quantity=payload['quantity'],
		price=payload['price']

	)
	product_dict = model_to_dict(new_products)
	product_dict['user'].pop('password')
	return jsonify(
		data=product_dict,
		message="succesfully created product",
		status=200
	), 200