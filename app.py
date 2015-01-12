# coding: utf-8

import logging
logging.basicConfig(level=logging.DEBUG)

import cloudcode
import leancloud
from leancloud import Object
from leancloud import Query
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request


APP_ID = 'yjgzl6w8n7qi4wgums8ayq8om8ltsz0zzppzfjb2bf95zcmz'
MASTER_KEY = '6xaz1p9nhru35qpewd2bxnklxbv2vs59pjtjx729emv6shii'

leancloud.init(APP_ID, MASTER_KEY)
app = Flask(__name__)


class Item(Object):
    pass


@app.route('/', methods=['GET'])
def index():
    items = Query('Item').descending('createdAt').find()
    return render_template('index.html', items=items)


@app.route('/', methods=['POST'])
def post_item():
    content = request.form['item']
    item = Item()
    item.set('content', content)
    item.save()

    return redirect('/')


if __name__ == '__main__':
    wsgi_func = cloudcode.wrap(app.wsgi_app)
    cloudcode.run('localhost', 5000, wsgi_func, use_reloader=True)
