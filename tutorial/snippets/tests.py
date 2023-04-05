from django.test import TestCase
from .models import Snippet
# Create your tests here.


class SnippetModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Snippet.objects.create(
            title='test_title',
            code='test_code',
            style='friendly',
            highlighted='x'
        )

    def test_title_label(self):
        snippet = Snippet.objects.get(id=3)
        field_label = snippet._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_cote_label(self):
        snippet = Snippet.objects.get(id=3)
        field_label = snippet._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    def test_title_max_length(self):
        snippet = Snippet.objects.get(id=3)
        max_length = snippet._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_highlighted_label(self):
        snippet = Snippet.objects.get(id=3)
        field_label = snippet._meta.get_field('highlighted').verbose_name
        self.assertEquals(field_label, 'highlighted')
