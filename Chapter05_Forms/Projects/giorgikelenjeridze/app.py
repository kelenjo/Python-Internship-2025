from flask import Flask, render_template, flash
from forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "esrdhsetwfgawef"

products = [
    {
        "id": 1,
        "name": "პატარა",
        "price": 11,
        "image": "shaurma.jfif",
        "description": "ლავაში, ღორის ხორცი 200გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
    },
    {
        "id": 2,
        "name": "სტანდარტი",
        "price": 13,
        "image": "shaurma.jfif",
        "description": "ლავაში, ღორის ხორცი 250გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
    },
    {
        "id": 3,
        "name": "დიდი",
        "price": 18,
        "image": "shaurma.jfif",
        "description": "ლავაში, ღორის ხორცი 300გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
    },
    {
        "id": 4,
        "name": "კოლა",
        "price": 3,
        "image": "cola.jfif",
        "description": "ცივი გაზიანი სასმელი, კოკა-კოლა 500მლ"
    },
    {
        "id": 5,
        "name": "სპრაიტი",
        "price": 3,
        "image": "sprite.jfif",
        "description": "ცივი გაზიანი სასმელი, სპრაიტი 500მლ"
    },
    {
        "id": 6,
        "name": "ბურგერი",
        "price": 10,
        "image": "burger.png",
        "description": "ბურგერის ბული, ღორის ხორცი 200გ, ყველი, პომიდორი, სალათის ფურცელი, კეტჩუპი, მაიონეზი"
    }
]


@app.route("/")
def index():
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
        # return render_template('index.html')
    else:
        print(form.errors)
    return render_template("register.html", form=form)


@app.route("/view/<int:product_id>")
def view(product_id):
    product = products[product_id]
    print(product)
    return render_template("view_product.html", product=product)


app.run(debug=True)
