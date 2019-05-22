#from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

class ItemInput(EmbeddedDocument):
    name = fields.StringField(requiredQuerySet=True)
    value = fields.DynamicField(required=True)

class Item(Document):
    title = fields.StringField(required=True, null=True)
    link = fields.StringField(required=True, null=True)
    description = fields.StringField(required=True, null=True)
