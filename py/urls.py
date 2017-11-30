import py.view.index as index
import py.view.api as api
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="../templates", static_folder="../static")
Bootstrap(app)
# index view
app.add_url_rule('/', 'index', view_func=index.index, methods=['GET'])
# api view
app.add_url_rule('/test', view_func=api.test, methods=['POST'])
