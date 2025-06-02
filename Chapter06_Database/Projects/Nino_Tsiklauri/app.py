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


################################
####        MODELS          ####
################################

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)

    def __repr__(self):
        return self.name


### ONE TO ONE RELATIONSHIP ###
class Person(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    birthday = db.Column(db.Date)
    idcard_id = db.Column(db.Integer, db.ForeignKey("id_cards.id"))

    id_card = db.relationship("IDCard", back_populates="person")

class IDCard(db.Model):
    __tablename__ = "id_cards"
    id = db.Column(db.Integer, primary_key=True)
    personal_number = db.Column(db.String)
    serial_number = db.Column(db.String)
    expiry_date = db.Column(db.Date)

    person = db.relationship("Person", back_populates="id_card", uselist=False)


### ONE TO MANY RELATIONSHIP ###
class University(db.Model):
    __tablename__ = "universities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    students = db.relationship("Student", back_populates="university")

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    university_id = db.Column(db.Integer, db.ForeignKey("universities.id"))

    university = db.relationship("University", back_populates="students")


### MANY TO MANY RELATIONSHIP ###
class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    movies = db.relationship("Movie", back_populates="actors", secondary="actor_movie")

class ActorMovie(db.Model):
    __tablename__ = "actor_movie"
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)

    actors = db.relationship("Actor", back_populates="movies", secondary="actor_movie")


################################
####        ROUTES          ####
################################

users = []


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

        new_product = Product(name=form.name.data, author=form.author.data, price=form.price.data, image=filename)
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
