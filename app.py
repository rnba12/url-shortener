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
from helper import shorten

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/short', methods=['GET', 'POST'])
def short():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short = shorten()
        link = Link(
            url=long_url,
            short_url=short
        )
        db.session.add(link)
        db.session.commit()
        return render_template('short.html', long_url=long_url, short_url=short)
    else:
        return redirect('/')
    

@app.route('/<string:url>', methods=['GET'])
def link(url):
    long_url = db.one_or_404(db.select(Link.url).filter_by(short_url=url))
    return redirect(long_url)

@app.errorhandler(exceptions.NotFound)
def handler_404(err):
    return redirect('/')

@app.errorhandler(exceptions.InternalServerError)
def handler_500(err):
    return redirect('/')

@app.errorhandler(exceptions.MethodNotAllowed)
def handler_400(err):
    return redirect('/')
      
if __name__ == "__main__":
    app.run(debug=True)