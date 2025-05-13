from flask import Flask, render_template
app = Flask(__name__)
tours = [
    {
        "id": 0,
        "country": "Italy",
        "title": "Rome Ancient Wonders Tour",
        "description": "Discover the Colosseum, Roman Forum, and Vatican City.",
        "price": 279.99,
        "old_price": 329.99,
        "currency": "EUR",
        "image": "https://www.agoda.com/wp-content/uploads/2024/08/Colosseum-Rome-Featured.jpg",
        "duration": "4 days",
        "rating": 4.9,
        "reviews": 150,
        "available": True
    },
    {
        "id": 1,
        "country": "Egypt",
        "title": "Cairo & Pyramids Adventure",
        "description": "Visit the Great Pyramids of Giza and the Egyptian Museum.",
        "price": 349.99,
        "old_price": 399.99,
        "currency": "USD",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/af/All_Gizah_Pyramids.jpg",
        "duration": "5 days",
        "rating": 4.8,
        "reviews": 180,
        "available": True
    },
    {
        "id": 2,
        "country": "Australia",
        "title": "Sydney & Blue Mountains",
        "description": "Explore Sydney Opera House, Harbour Bridge, and Blue Mountains.",
        "price": 499.99,
        "old_price": 550.00,
        "currency": "AUD",
        "image": "https://www.sydneytravelguide.com.au/wp-content/uploads/2024/09/sydney-australia.jpg",
        "duration": "6 days",
        "rating": 4.7,
        "reviews": 130,
        "available": True
    },
    {
        "id": 3,
        "country": "Spain",
        "title": "Barcelona",
        "description": "Admire Sagrada Familia, Park Güell, and Gothic Quarter.",
        "price": 259.99,
        "old_price": 299.99,
        "currency": "EUR",
        "image": "https://www.introducingbarcelona.com/f/espana/barcelona/barcelona.jpg",
        "duration": "3 days",
        "rating": 4.9,
        "reviews": 210,
        "available": True
    },
    {
        "id": 4,
        "country": "Turkey",
        "title": "Istanbul Heritage Tour",
        "description": "Visit Hagia Sophia, Blue Mosque, and Grand Bazaar.",
        "price": 199.99,
        "old_price": 249.99,
        "currency": "USD",
        "image": "https://deih43ym53wif.cloudfront.net/small_cappadocia-turkey-shutterstock_1320608780_9fc0781106.jpeg",
        "duration": "4 days",
        "rating": 4.8,
        "reviews": 170,
        "available": True
    }
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/trips")
def trips():
    return render_template("trips.html", tours=tours)

@app.route("/trips/<int:tour_id>")
def tour_detail(tour_id):
    chosen_tour = tours[tour_id]
    return render_template("tour_detail.html", tour=chosen_tour)

app.run(debug=True)
