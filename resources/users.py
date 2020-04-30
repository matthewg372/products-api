import models
from flask import Blueprint, request, jsonify

users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def users_route():
	return 'connected to users'

