

##Pre-Workout Products By Stores/ Models
```
class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	bussiness=Charfield()
	class Meta:
		database = DATABASE

class Products(Model):
	user = ForeignKeyField(User, backref='products')
	name=CharField()
	flavors=CharField()
	quantity=BitField()
	price=Bitfield
	class Meta:
		database


```

```
url              |	httpVerb| result
_____________________________________
/api/products    | GET     | returns all products
/api/products    | POST    | new product created
/api/products/id | GET     | shows users products
/api/products/id | Put     | update a product
/api/products/id | DELETE  | delete a product


url              |	httpVerb| result
_____________________________________
/api/users       | POST    | register a user
/api/users       | POST    | login user
/api/users       | GET     | logout user
```

<img src="images/IMG_1020.JPG"/>
<img src="images/IMG_1021.JPG"/>
