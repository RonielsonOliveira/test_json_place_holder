import unittest
from random import choice

import requests
import json
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "", "", "json_scenarios")
sys.path.append(path_dir)

from json_scenarios.json_utils import *


class Profiles(unittest.TestCase):
    def setUp(self):
        self.url = 'https://jsonplaceholder.typicode.com'

    def test_1_get_posts(self):
        response_save = requests.get(f'{self.url}/posts')
        self.assertEqual(response_save.status_code, 200)
        json_data_posts = json.loads(response_save.text)
        print(json_data_posts)
        for postList_item in json_data_posts:
            self.assertIn('userId', postList_item)
            self.assertEqual(type(postList_item['userId']), int)
            self.assertIn('id', postList_item)
            self.assertEqual(type(postList_item['id']), int)
            self.assertIn('title', postList_item)
            self.assertEqual(type(postList_item['title']), str)
            self.assertIn('body', postList_item)
            self.assertEqual(type(postList_item['body']), str)


if __name__ == '__main__':
    unittest.main()
