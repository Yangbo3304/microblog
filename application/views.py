# -*- coding: utf-8 -*-
from flask import render_template

from application import app


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    user = {'nickname': 'Miguel'}  # 伪造的用户
    # 伪造的帖子数组
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)
