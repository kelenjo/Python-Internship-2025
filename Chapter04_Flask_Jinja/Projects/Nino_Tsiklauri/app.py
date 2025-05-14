from flask import Flask, render_template

app = Flask(__name__)

products=[
    {"id": 0, "name":"ფრანით მორბენალი", "author":"ხალიდ ჰოსეინი", "price":"25", "img":"franit-morbenali.png"},
    {"id": 1, "name":"48 კანონი", "author":"რობერტ გრინი", "price":"40", "img":"dzalauflebis_48_kanoni.jpg"},
    {"id": 2, "name":"ატომური ჩვევები", "author":"ჯეიმს ქლიერი", "price":"35", "img":"atomuri_cvevebi.jpg"},
    {"id": 3, "name":"ხაფანგი 22", "author":"ჟოზეფ ჰელერის", "price":"30", "img":"xafangi22.png"}
]

@app.route("/")
def index():
    return render_template("index.html" , products=products)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/view/<int:product_index>")
def view_product(product_index):
    chosen_product = products[product_index]
    return render_template("view_product.html", product=chosen_product)

app.run(debug=True)