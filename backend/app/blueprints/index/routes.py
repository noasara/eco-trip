import json
from pathlib import Path

from flask import Blueprint, abort, redirect, render_template, url_for

dist = Path(__file__).resolve().parents[4] / 'dist'
index_bp = Blueprint(
    'index', __name__, template_folder='templates', static_folder=dist, static_url_path=''
)


@index_bp.get('/')
def index():
    try:
        manifest = json.loads((dist / '.vite' / 'manifest.json').read_text(encoding='utf-8'))
    except FileNotFoundError:
        abort(503, description='Compile le frontend avec npm run build.')

    return render_template('index/accueil.html', react_entry=manifest['index.html'])


@index_bp.get('/accueil')
def accueil():
    return redirect(url_for('.index'))
