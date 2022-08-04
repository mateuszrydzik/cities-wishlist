from typing import Text
from peewee import PostgresqlDatabase, Model, PrimaryKeyField, TextField, Field

database = PostgresqlDatabase(None)


class GeometryField(Field):
    field_type = 'geometry'
    db_field = 'geometry'


class AbstractModel(Model):
    id = PrimaryKeyField()

    class Meta:
        database = database


class User(AbstractModel):
    name = TextField(unique=True)
    password = TextField()

    class Meta:
        db_table = 'user'


class Place(AbstractModel):
    city = TextField()
    country = TextField()
    notes = TextField()
    geom = GeometryField()

    class Meta:
        db_table = 'place'
