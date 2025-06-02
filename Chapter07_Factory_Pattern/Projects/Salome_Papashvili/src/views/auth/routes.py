from uuid import uuid4
from os import path
from flask import Blueprint, render_template
from src.views.auth.forms import RegisterForm
from src.config import Config
auth_blueprint = Blueprint("auth", __name__)
users = []
@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        file = form.profile_image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(Config.UPLOAD_PATH, filename))

        users.append(
            {
                "username": form.username.data,
                "birthday": form.birthday.data,
                "gender": form.gender.data,
                "country": form.country.data,
                "profile_image": filename
            }
        )
    else:
        print(form.errors)
    return render_template("auth/register.html", form=form)


@auth_blueprint.route("/login")
def login():
    return render_template("auth/login.html")