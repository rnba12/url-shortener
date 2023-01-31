from flask import Flask, request, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from model import Link

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/short', methods=['GET', 'POST'])
def short():
    if request.method == 'POST':
        long_url = request.form['long_url']
        link = Link(
            url=long_url,
            short_url='short_url'
        )
        db.session.add(link)
        db.session.commit()
        return render_template('short.html', long_url=long_url, short_url=f'new url')
    else:
        return redirect('/')

@app.errorhandler(exceptions.NotFound)
def handler_404(err):
    return redirect('/')
