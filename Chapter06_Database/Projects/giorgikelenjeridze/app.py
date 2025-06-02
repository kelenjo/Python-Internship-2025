from flask import Flask, render_template, flash, request, redirect, url_for
from forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://python_intern-user:Wyali!12345@localhost:5432/python_intern-db"
app.config['SECRET_KEY'] = "esrdhsetwfgawef"

db = SQLAlchemy(app)


class Product(db.Model):

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)

    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

    def __repr__(self):
        return f"This is {self.name} and costs {self.price}$"


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User name: {self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def edit(self, form):
        self.username = form.username.data
        self.password = form.password.data
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Person(db.Model):

    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    birthday = db.Column(db.Date)

    idcard_id = db.Column(db.Integer, db.ForeignKey("idcards.id"))

    idcard = db.relationship("IDcard")


class IDcard(db.Model):

    __tablename__ = "idcards"
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String)
    expiry_data = db.Column(db.Date)

    person = db.relationship("Person")


@app.route("/")
def index():
    products = Product.query.all()
    person = Person.query.get(1)
    print(person.idcard.person.name)
    return render_template("index.html", products=products)


@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.email.data)
        print(form.password.data)
        flash("Sagol shen daregistrirdi", "info")
        print('ar xar')
        user = User(form.username.data, form.email.data, form.password.data)
        user.save()
        # return render_template('index.html')
    else:
        print('bad xar1')
        print(form.errors)
        print('bad xaar2')
    return render_template("register.html", form=form)


@app.route("/edit/<int:user_id>", methods=['GET', 'POST'])
def edit(user_id):
    user = User.query.get(user_id)
    oldname = user.username
    form = RegisterForm(username=user.username, email=user.email, password=user.password)
    if form.validate_on_submit():
        user.edit(form)
        print(f"{oldname} has changed it own name to {user.username}")
    else:
        print(form.errors)
    return render_template("/register.html", form=form)


@app.route("/delete/<int:user_id>")
def delete(user_id):
    usertodel = User.query.get(user_id)
    User.query.filter_by()
    print(usertodel)
    usertodel.delete()
    print(url_for("index"))
    return redirect(url_for("index"))


@app.route("/view/<int:product_id>")
def view(product_id):
    product = Product.query.get(product_id)
    print(product)
    return render_template("view_product.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)

