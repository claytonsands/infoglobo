from django.test import TestCase
from infoglobo.models import Item


class TestItem(TestCase):
    def create_item(self, title='Title test', link='http://', description='Description test'):
        return Item.objects.create(title=title, link=link, description=description)

    def test_item_creation(self):
        i = self.create_item()
        self.assertTrue(isinstance(i, Item))
        self.assertEquals(i.__str__(), i.title)