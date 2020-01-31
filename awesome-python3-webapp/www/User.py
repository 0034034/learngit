from orm import Model,StringField, IntegerField
import asyncio,logging
import aiomysql

class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key = True)
    name = StringField()

user = User(id=123,name='Michael')
yield from user.save()
users = User.findAll()
print(user['id'])
print(user.id)


