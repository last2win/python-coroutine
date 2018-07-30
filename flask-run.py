# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:02:10 2018

@author: peter
"""

from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def index():
    time.sleep(3)
    return 'Hello!'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
