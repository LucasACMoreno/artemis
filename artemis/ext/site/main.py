from flask import request, render_template
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/bandas")
def bandas():
    return render_template("bandas.html")

@bp.route("/welcome", methods=["POST"])
def welcome():
    return render_template("index.html", visitante=request.values['name'])

@bp.route("/admin")
def admin():
    return render_template("admin.html")