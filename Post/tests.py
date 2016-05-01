from django.test import TestCase , Client
from Post.models import Post
from django.core.urlresolvers import  reverse

class PostTestCase(TestCase):

    def setup(self):
        Post.objects.create(title="Lorem Ipsum" , body="Lorem Ipsum")
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(200 , response.status_code)
