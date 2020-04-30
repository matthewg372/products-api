from peewee import *
from flask_login import UserMixin



DATABASE = SqliteDatabase('products.sqlite')





class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	bussiness=CharField()
	class Meta:
		database = DATABASE

class Product(Model):
	user = ForeignKeyField(User, backref='products')
	name=CharField()
	flavors=CharField()
	quantity=IntegerField()
	price=FloatField()
	class Meta:
		database = DATABASE

class Like(Model):
	user = ForeignKeyField(User, backref='likes')
	product = ForeignKeyField(Product, backref='likes')
	likes=IntegerField()
	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Product, Like], safe=True)
	print('connected to models and tables')
	DATABASE.close()