from flask import Flask, render_template, flash
from forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
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

    def delete(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/")
def index():
    products = Product.query.all()
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
        user = User(form.username.data, form.email.data, form.password.data)
        user.save()
        # return render_template('index.html')
    else:
        print(form.errors)
    return render_template("register.html", form=form)


@app.route("/view/<int:product_id>")
def view(product_id):
    product = Product.query.get(int(product_id))
    print(product)
    return render_template("view_product.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)
