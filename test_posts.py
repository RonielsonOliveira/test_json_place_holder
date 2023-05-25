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

    def test_2_post_posts(self):
        body = {
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }
        response_save = requests.post(f'{self.url}/posts',json=body)
        self.assertEqual(response_save.status_code, 201)
        json_data_posts = json.loads(response_save.text)
        print(json_data_posts)
        self.assertIn('title', json_data_posts)
        self.assertEqual(type(json_data_posts['title']), str)
        self.assertIn('body', json_data_posts)
        self.assertEqual(type(json_data_posts['body']), str)
        self.assertIn('id', json_data_posts)
        self.assertEqual(type(json_data_posts['id']), int)

    def test_3_get_posts_id(self):
        response_save = requests.get(f'{self.url}/posts/1')
        self.assertEqual(response_save.status_code, 200)
        json_data_posts = json.loads(response_save.text)
        print(json_data_posts)
        self.assertIn('userId', json_data_posts)
        self.assertEqual(type(json_data_posts['userId']), int)
        self.assertIn('id', json_data_posts)
        self.assertEqual(type(json_data_posts['id']), int)
        self.assertIn('title', json_data_posts)
        self.assertEqual(type(json_data_posts['title']), str)
        self.assertIn('body', json_data_posts)
        self.assertEqual(type(json_data_posts['body']), str)

    def test_4_get_posts_id_comments(self):
        response_save = requests.get(f'{self.url}/posts/1/comments')
        self.assertEqual(response_save.status_code, 200)
        json_data_posts = json.loads(response_save.text)
        print(json_data_posts)
        for postList_item in json_data_posts:
            self.assertIn('postId', postList_item)
            self.assertEqual(type(postList_item['postId']), int)
            self.assertIn('id', postList_item)
            self.assertEqual(type(postList_item['id']), int)
            self.assertIn('name', postList_item)
            self.assertEqual(type(postList_item['name']), str)
            self.assertIn('email', postList_item)
            self.assertEqual(type(postList_item['email']), str)
            self.assertIn('body', postList_item)
            self.assertEqual(type(postList_item['body']), str)

if __name__ == '__main__':
    unittest.main()
