import os
from peewee import *
from flask_login import UserMixin
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ: 

  	DATABASE = connect(os.environ.get('postgres://jvngndowwvrhfa:f856fb05e20f3907d143d39899f4f7c8b1c560f14916a3e4f78c16ab7c1e4ccc@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d1hk2vj6c3v6c0'))
else:
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