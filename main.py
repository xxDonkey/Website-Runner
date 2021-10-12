import os
import json
import requests
import dotenv

from typing import List
from flask import Flask, send_from_directory, abort, render_template, url_for

dotenv.load_dotenv()
USER = os.getenv("USER")

template_path = os.path.join(os.getcwd(), 'templates')
static_js_path = os.path.join(os.getcwd(), 'static/js')
static_css_path = os.path.join(os.getcwd(), 'static/css')

def fetch_repo(repo):
    link_stem = f'https://raw.github.com/{USER}/{repo}'


    # fetch and save  main.js
    req = requests.get(f'{link_stem}/main/main.js')
    with open(os.path.join(static_js_path, f'{repo}.js'), 'w') as f:
        f.write(req.text)

    # fetch and save  main.css
    req = requests.get(f'{link_stem}/main/main.css')
    with open(os.path.join(static_css_path, f'{repo}.css'), 'w') as f:
        f.write(req.text)
    
    # fetch index.html
    req = requests.get(f'{link_stem}/main/index.html')
    html = req.text

    # replace js link with Flask static link
    html = html.replace('main.js', url_for('static', filename=f'js/{repo}.js'))

    # replace css link with Flask static link
    html = html.replace('main.css', url_for('static', filename=f'css/{repo}.css'))

    # save index.html
    with open(os.path.join(template_path, f'{repo}.html'), 'w') as f:
        f.write(html)

app = Flask(__name__)

repos: List[str]
with open('repos.json') as f:
    repos = json.load(f)

@app.route('/')
def index():
    return render_template('Home-Page.html')

@app.route('/<page>')
def load_page(page):
    if page not in repos:
        abort(404)

    fetch_repo(page)
    return render_template(f'{page}.html')

