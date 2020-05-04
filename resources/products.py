import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

products = Blueprint('products', 'products')

"""index for specific logged in people"""
@products.route('/users/<id>', methods=['GET'])
@login_required
def user_products_index(id):
	user_Product = models.User.get_by_id(id)
	current_user_product_dicts = [model_to_dict(product) for product in user_Product.products]
	print(current_user_product_dicts)
	for product_dict in current_user_product_dicts:
		product_dict['user'].pop('password')
	return jsonify(
		data= current_user_product_dicts,
		message= f"Successfully found {len(current_user_product_dicts)} products",
		status= 200
	), 200

""" get all products """
@products.route('/all', methods=['GET'])
def user_index():

	products = models.Product.select()
	product_dicts = [ model_to_dict(product) for product in products ]

	for product_dict in product_dicts:
		product_dict['user'].pop('password')


	return jsonify(product_dicts), 200


""" create products """
@products.route('/', methods=['POST'])
@login_required
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

""" delete specific products """
@products.route('/<id>', methods=['DELETE'])
@login_required
def delete_products(id):
	product_to_delete = models.Product.get_by_id(id)
	if current_user.id == product_to_delete.user.id:
		delete_query = models.Product.delete().where(models.Product.id == id)
		delete_query.execute()
		return jsonify(
			data={},
			message=f"succesfully deleted {id}",
			status=200
		), 200
	else:
		return jsonify(
			data={},
			message="you must be logged in to delete this",
			status=403
		), 403


""" update specific product """
@products.route('/<id>', methods=['PUT'])
@login_required
def update_product(id):
	payload = request.get_json()
	product_to_update = models.Product.get_by_id(id)
	if current_user.id == product_to_update.user.id:
		if 'name' in payload:
			product_to_update.name=payload['name']
		if 'flavors' in payload:
			product_to_update.flavors=payload['flavors']
		if 'quantity' in payload:
			product_to_update.quantity=payload['quantity']
		if 'price' in payload:
			product_to_update.price=payload['price']
		product_to_update.save()
		updated_product_dict = model_to_dict(product_to_update)
		updated_product_dict['user'].pop('password')
		return jsonify(
			data=updated_product_dict,
			message=f"succesfully updated {id}",
			status=200
		),200
	else:
		return jsonify(
			data={},
			message=f"you must be logged in to updated",
			status=403
		), 403









