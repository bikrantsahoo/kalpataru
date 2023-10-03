from flask import Flask, render_template
from src.routes import index, user_routes, alerts_routes, rules_routes, de_routes
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('base.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/400.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500


# Register the Blueprints
# app.register_blueprint(index.index_bp, url_prefix='/home')
app.register_blueprint(alerts_routes.alert_bp)
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(rules_routes.rule_bp)
app.register_blueprint(de_routes.de_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
