import json
from pathlib import Path

from flask import Blueprint, abort, redirect, render_template, url_for

dist = Path(__file__).resolve().parents[4] / 'front1' / 'dist'
index_bp = Blueprint(
    'index', __name__, template_folder=dist, static_folder=dist, static_url_path=''
)


@index_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')