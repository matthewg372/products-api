import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

likes = Blueprint('likes', 'likes')

@likes.route('/all', methods=['GET'])
def all_likes():

	likes = models.Like.select()
	like_dicts = [ model_to_dict(like) for like in likes ]


	return jsonify(like_dicts), 200

@likes.route('/<id>', methods=['POST'])
def likes_test(id):
	payload = request.get_json()
	product_to_like = models.Product.get_by_id(id)
	new_like = models.Like.create(
		likes=payload['likes'],
		user=current_user.id,
		product=product_to_like
		)
	product_dict = model_to_dict(new_like)

	

	return jsonify(
		data=product_dict,
		messages="liked",
		status=200
	), 200
