from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("index.html",
                           alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                           numbers=["0", "1", "2", "3", "4","5", "6", "7", "8", "9"],
                           spaceArr=[""]
                           )
