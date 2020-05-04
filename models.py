from peewee import *
from flask_login import UserMixin
import os
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ: 
  	DATABASE = connect(os.environ.get('postgres://znusabyfibivje:9f7e38afbaa40dc8843f80d3fb3e9d81992774f69a9fcc9fa6a45598a961dee0@ec2-34-195-169-25.compute-1.amazonaws.com:5432/d9ve6uo8pq85dj'))
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