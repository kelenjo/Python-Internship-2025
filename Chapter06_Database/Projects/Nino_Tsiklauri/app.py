from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, ProductForm
from os import path
from uuid import uuid4

app = Flask(__name__)
app.config["SECRET_KEY"] = "JBKCVKCKCJjvn46r76yuv8g98g7f@"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
UPLOAD_PATH = path.join(app.root_path, "static", "assets")

db = SQLAlchemy(app)

users = []

#### MODELS ####
class Product(db.Model):
    __tablename__ = "producs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)


@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", users=users, products=products)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        users.append({
            "username": form.username.data,
            "birthday": form.birthday.data,
            "gender": form.gender.data,
            "country": form.country.data
        })

        file = form.profile_image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))
        print("Everything is fine!")
    else:
        print(form.errors)
    return render_template("registration.html", form=form)


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        file = form.image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))

        new_product = Product(name=form.name.data, author=form.author.data,  price=form.price.data, image=filename)
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("create_product.html", form=form)


@app.route("/edit_product/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    product = Product.query.get(id)

    form = ProductForm(name=product.name, author=product.author, price=product.price)
    if form.validate_on_submit():
        product.name = form.name.data
        product.author = form.author.data
        product.price = form.price.data

        if form.image.data:
            file = form.image.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(UPLOAD_PATH, filename))

            product.image = filename

        db.session.commit()
        return redirect(url_for("index"))

    return render_template("create_product.html", form=form)


@app.route("/delete_product/<int:id>")
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/view/<int:product_id>")
def view_product(product_id):
    chosen_product = Product.query.get(product_id)
    return render_template("view_product.html", product=chosen_product)

if __name__ == "__main__":
    app.run(debug=True)
