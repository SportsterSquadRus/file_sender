from django.test import TestCase, RequestFactory, Client
from tempfile import TemporaryFile
from random import randint
from django.urls import resolve, reverse
from upload.views import FilesListView
from data.views import FilesListView as DrfListView
import json


class FileUploadTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_list_view(self):
        url = reverse('list_url')
        self.assertEqual(resolve(url).func.view_class, FilesListView)

    def test_view_get(self):
        request = self.factory.get('api/list')
        response = DrfListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_case(self):
        lst = list(map(str, [randint(1, 255) for i in range(10000)]))
        lst_str = ' '.join(lst)

        c = Client()
        url = reverse('upload_file')
        url_list = reverse('rest_list')

        with TemporaryFile() as f:
            f.write(lst_str.encode('utf-8'))
            f.seek(0)
            response = c.post(url, {'file': f})

        response_get = c.get(url_list)
        data = response_get.content.decode('utf-8')
        lst_from_server = json.loads(data)[0]['numbers']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(lst, lst_from_server)
