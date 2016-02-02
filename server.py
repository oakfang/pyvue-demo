from flask import Flask
from facade import pyv
import views

pyv.pyv_loader.revoke()

app = Flask(__name__)


@app.route("/")
def index():
    return views.index(xrange(10))


@app.route("/foo")
def foo():
    return views.foo()


if __name__ == "__main__":
    app.run(debug=True)