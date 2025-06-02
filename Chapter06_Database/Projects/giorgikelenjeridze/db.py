import datetime

from app import app, db, Product, IDcard, Person

products = [
    {
        "id": 0,
        "name": "შაურმა პატარა",
        "price": 11,
        "image": "shaurma.jfif",
        "description": "ლავაში, ღორის ხორცი 200გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
    },
    {
        "id": 1,
        "name": "შაურმა სტანდარტი",
        "price": 13,
        "image": "shaurma.jfif",
        "description": "ლავაში, ღორის ხორცი 250გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
    },
    {
        "id": 2,
        "name": "შაურმა დიდი",
        "price": 18,
        "image": "shaurma.jfif",
        "description": "ლავაში, ღორის ხორცი 300გ, პომიდორი, ხახვი, სალათის ფურცელი(აისბერგი), წიწაკა, მაიონეზი, კეტჩუპი"
    },
    {
        "id": 3,
        "name": "კოლა",
        "price": 3,
        "image": "cola.jfif",
        "description": "ცივი გაზიანი სასმელი, კოკა-კოლა 500მლ"
    },
    {
        "id": 4,
        "name": "სპრაიტი",
        "price": 3,
        "image": "sprite.jfif",
        "description": "ცივი გაზიანი სასმელი, სპრაიტი 500მლ"
    },
    {
        "id": 5,
        "name": "ბურგერი",
        "price": 10,
        "image": "burger.png",
        "description": "ბურგერის ბული, ღორის ხორცი 200გ, ყველი, პომიდორი, სალათის ფურცელი, კეტჩუპი, მაიონეზი"
    }
]


with app.app_context():

    db.create_all()

    for product in products:
        new_product = Product(name=product["name"], price=product["price"], image=product["image"])
        db.session.add(new_product)

    idcard = IDcard(serial_number="01201115242", expiry_data=datetime.datetime.now())
    db.session.add(idcard)
    db.session.commit()
    person = Person(name="Giorgi", surname="Kelenjeridze", birthday=datetime.datetime.now(), idcard_id=idcard.id)
    db.session.add(person)
    db.session.commit()