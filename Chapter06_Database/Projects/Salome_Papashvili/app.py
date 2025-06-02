from flask import Flask, render_template, redirect, url_for
from forms import RegisterForm, AddTourForm
from os import path
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "GJFKLDJKljklhhjkhjk@595jijkjd"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
UPLOAD_PATH = path.join(app.root_path, "static", "upload")

db = SQLAlchemy(app)
users = []


class Tour(db.Model):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    currency = db.Column(db.String)
    image = db.Column(db.String)
    duration = db.Column(db.String)

@app.route("/")
def index():
    return render_template("index.html", users=users)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/trips")
def trips():
    tours = Tour.query.all()
    return render_template("trips.html", tours=tours)

@app.route("/trips/<int:tour_id>")
def tour_detail(tour_id):
    chosen_tour = Tour.query.get(tour_id)
    return render_template("tour_detail.html", tour=chosen_tour)

@app.route("/add_tour", methods=["GET", "POST"])
def add_tour():
    form = AddTourForm()
    if form.validate_on_submit():
        file = form.image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))
        new_tour = Tour(country=form.country.data,
                        title=form.title.data,
                        description=form.description.data,
                        price=form.price.data,
                        currency=form.currency.data,
                        duration=form.duration.data,
                        image = filename)
        new_tour.image = filename
        db.session.add(new_tour)
        db.session.commit()
        return redirect(url_for("trips"))
    else:
        print(form.errors)
    return render_template("add_tour.html", form=form)

@app.route("/edit_tour/<int:tour_id>", methods=["GET", "POST"])
def edit_tour(tour_id):
    tour = Tour.query.get(tour_id)
    form = AddTourForm(country=tour.country,
                        title=tour.title,
                        description=tour.description,
                        price=tour.price,
                        currency=tour.currency,
                        duration=tour.duration)
    if form.validate_on_submit():
        tour.country = form.country.data
        tour.title = form.title.data
        tour.description = form.description.data
        tour.price = form.price.data
        tour.currency = form.currency.data
        tour.duration = form.duration.data

        if form.image.data:
            file = form.image.data
            _, extension = path.splitext(file.filename)
            filename = f"{uuid4()}{extension}"
            file.save(path.join(UPLOAD_PATH, filename))
            tour.image = filename
        db.session.commit()
        return redirect(url_for("trips"))
    return render_template("add_tour.html", form=form)


@app.route("/delete_tour/<int:tour_id>")
def delete_tour(tour_id):
    tour = Tour.query.get(tour_id)
    db.session.delete(tour)
    db.session.commit()
    return redirect(url_for("trips"))

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        file = form.profile_image.data
        _, extension = path.splitext(file.filename)
        filename = f"{uuid4()}{extension}"
        file.save(path.join(UPLOAD_PATH, filename))

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
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
