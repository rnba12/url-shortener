from flask import Flask, request, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/short', methods=['GET', 'POST'])
def short():
    if request.method == 'POST':
        long_url = request.form['long_url']
        return render_template('short.html', long_url=long_url, short_url=f'new url')
    else:
        return redirect('/')

@app.errorhandler(exceptions.NotFound)
def handler_404(err):
    return redirect('/')
