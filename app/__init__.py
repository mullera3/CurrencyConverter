import os
from flask import Flask


class AppController(Flask):
    app = Flask(__name__)


app = AppController.app

from app import routes





