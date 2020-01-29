import functools
from flask import (
    Blueprint,flash,g,current_app,redirect,render_template,
    request,session,url_for
)

from blog.db import get_db

bp = Blueprint('blog',__name__,url_prefix='/blog')

@bp.route('/',methods=['GET'])
def index():
    return render_template('blog/index.html')