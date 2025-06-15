import os

from dotenv import load_dotenv

from apps import create_app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
