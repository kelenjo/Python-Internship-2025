from flask import Blueprint, render_template, flash, redirect, url_for, request
from src.view.user.forms import RegisterForm, LoginForm
from src.models.user import User
from flask_login import login_user, logout_user, login_required


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.email.data)
        print(form.password.data)
        flash("Sagol shen daregistrirdi", "info")
        print('ar xar')
        user = User(form.username.data, form.email.data, form.password.data)
        user.create()
        # return render_template('index.html')
    else:
        print('bad xar1')
        print(form.errors)
        print('bad xaar2')
    return render_template("user/register.html", form=form)


@user_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)

            next = request.args.get("next")

            if next:
                return redirect(next)
            flash("Logged in!", "success")
            return redirect(url_for("main.index"))
        else:
            flash("Username or Password is incorrect", "danger")

    return render_template("user/login.html", form=form)


@user_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@user_blueprint.route("/edit/<int:user_id>", methods=['GET', 'POST'])
@login_required
def edit(user_id):
    user = User.query.get(user_id)
    oldname = user.username
    form = RegisterForm(username=user.username, email=user.email, password=user.password)
    if form.validate_on_submit():
        user.edit(form)
        print(f"{oldname} has changed it own name to {user.username}")
    else:
        print(form.errors)
    return render_template("user/register.html", form=form)


@user_blueprint.route("/delete/<int:user_id>")
@login_required
def delete(user_id):
    usertodel = User.query.get(user_id)
    User.query.filter_by()
    print(usertodel)
    usertodel.delete()
    print(url_for("index"))
    return redirect(url_for("main.index"))