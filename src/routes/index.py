from flask import Blueprint, render_template

index_bp = Blueprint("home", __name__)


@index_bp.route('/home')
def index():
    return render_template('template.html')
