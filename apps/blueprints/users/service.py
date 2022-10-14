import json
import os
import requests
from .models import User


class UserService:
    url = 'https://gorest.co.in/public/v2/users'
    access_token = 'Bearer ' + os.environ.get('ACCESS_TOKEN')
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': access_token}

    @classmethod
    def get_all(cls, page_number):
        page_param = {'page': page_number}
        response = requests.get(cls.url, headers=cls.headers, params=page_param)
        users = None
        try:
            response.raise_for_status()
            users = [cls.from_json(user_json) for user_json in response.json()]
        except requests.HTTPError as e:
            pass
        finally:
            return users

    @classmethod
    def get_by_id(cls, user_id):
        response = requests.get(f'{cls.url}/{user_id}', headers=cls.headers)
        user = None
        try:
            response.raise_for_status()
            user = cls.from_json(response.json())
        except requests.HTTPError as e:
            pass
        finally:
            return user

    @classmethod
    def add_user(cls, user):
        user_json = cls.to_json(user)
        response = requests.post(cls.url, headers=cls.headers, json=user_json)
        response.raise_for_status()

    @classmethod
    def update_user(cls, user):
        user_json = cls.to_json(user)
        response = requests.put(f'{cls.url}/{user.user_id}', headers=cls.headers, json=user_json)
        response.raise_for_status()

    @classmethod
    def delete_by_id(cls, user_id):
        response = requests.delete(f'{cls.url}/{user_id}', headers=cls.headers)
        response.raise_for_status()

    @classmethod
    def get_page_count(cls):
        response = requests.get(cls.url, headers=cls.headers)
        pages = 1
        try:
            response.raise_for_status()
            pages = response.headers['X-Pagination-Pages']
        except requests.HTTPError as e:
            pass
        finally:
            return pages

    @staticmethod
    def to_json(user):
        data = {k: getattr(user, k, None) for k, v in user.__class__.__dict__.items() if isinstance(v, property)}
        return json.dumps(data)

    @staticmethod
    def from_json(user_json):
        user = User()
        _ = [setattr(user, k, v) for k, v in user_json.items() if hasattr(user, k)]
        return user
