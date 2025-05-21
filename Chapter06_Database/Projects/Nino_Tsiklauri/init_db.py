from app import app, db, Product

products = [
    {"id": 0, "name": "ფრანით მორბენალი", "author": "ხალიდ ჰოსეინი", "price": "25", "img": "franit-morbenali.png"},
    {"id": 1, "name": "48 კანონი", "author": "რობერტ გრინი", "price": "40", "img": "dzalauflebis_48_kanoni.jpg"},
    {"id": 2, "name": "ატომური ჩვევები", "author": "ჯეიმს ქლიერი", "price": "35", "img": "atomuri_cvevebi.jpg"},
    {"id": 3, "name": "ხაფანგი 22", "author": "ჟოზეფ ჰელერის", "price": "30", "img": "xafangi22.png"}
]

with app.app_context():
    db.create_all()

    for product in products:
        new_product = Product(name=product["name"], author=product["author"], price=product["price"], image=product["img"])
        db.session.add(new_product)
    db.session.commit()