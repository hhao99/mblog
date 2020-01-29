import functools
from flask import (
    Blueprint,flash,g,current_app,redirect,render_template,
    request,session,url_for
)

from blog.db import get_db

bp = Blueprint('blog',__name__,url_prefix='/blog')

@bp.route('/',methods=['GET'])
def index():
    db = get_db()
    posts = db.execute(
        'select * from post'
    ).fetchall()
    return render_template('blog/index.html',posts=posts)

@bp.route('/<int:id>',methods=['GET'])
def post(id):
    db = get_db()
    post = db.execute(
        f'select * from post where id = {id}'
    ).fetchone()
    return render_template('blog/post.html',post=post)

@bp.route('/',methods=['POST'])
def new():
    title = request.form['title']
    body = request.form['body']
    get_db().execute(f'insert into post (title,body,author) values ("{title}","{body}","eric")')
    get_db().commit()
    return redirect(url_for('blog.index'))
