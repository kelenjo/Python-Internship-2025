from flask import Flask, render_template
from forms import RegisterForm
from os import path
from uuid import uuid4

app = Flask(__name__)
app.config["SECRET_KEY"] = "JBKCVKCKCJjvn46r76yuv8g98g7f@"
UPLOAD_PATH = path.join(app.root_path, "static", "upload")

products = [
    {"id": 0, "name": "ფრანით მორბენალი", "author": "ხალიდ ჰოსეინი", "price": "25", "img": "franit-morbenali.png"},
    {"id": 1, "name": "48 კანონი", "author": "რობერტ გრინი", "price": "40", "img": "dzalauflebis_48_kanoni.jpg"},
    {"id": 2, "name": "ატომური ჩვევები", "author": "ჯეიმს ქლიერი", "price": "35", "img": "atomuri_cvevebi.jpg"},
    {"id": 3, "name": "ხაფანგი 22", "author": "ჟოზეფ ჰელერის", "price": "30", "img": "xafangi22.png"}
]
users = []


@app.route("/")
def index():
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


@app.route("/view/<int:product_index>")
def view_product(product_index):
    chosen_product = products[product_index]
    return render_template("view_product.html", product=chosen_product)


app.run(debug=True)
