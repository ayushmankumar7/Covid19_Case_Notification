from flask import Flask , render_template
from src.fetch_value import current


app = Flask(__name__)




@app.route("/")
def home():
    x, y = current()
    return render_template("index.html", international = x, india = y)
