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


@products.route('/<id>', methods=['DELETE'])
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

@products.route('/<id>', methods=['PUT'])
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









