from flask import Flask, render_template

app = Flask(__name__)

images = [
    {"src": "https://colaisteneifinn.com/wp-content/uploads/2023/10/about-us.webp", "alt": "About Us", "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus, cupiditate animi asperiores aliquam esse, exercitationem quasi officia illum sunt in explicabo tempore eaque cum accusamus mollitia voluptate nemo, molestiae quam!"},
    {"src": "https://evmedianetwork.com/wp-content/uploads/2024/10/depositphotos_49080337-stock-photo-about-us-1.webp", "alt": "About Us", "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus, cupiditate animi asperiores aliquam esse, exercitationem quasi officia illum sunt in explicabo tempore eaque cum accusamus mollitia voluptate nemo, molestiae quam!"},
    {"src": "https://cdnwebsite.databox.com/wp-content/uploads/2020/12/01062702/about-us-page-examples.png", "alt": "About Us", "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus, cupiditate animi asperiores aliquam esse, exercitationem quasi officia illum sunt in explicabo tempore eaque cum accusamus mollitia voluptate nemo, molestiae quam!"}
]

customers = [
    {"image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D", "comment": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Odio error consequuntur possimus ipsa, fugiat laborum dolor vero a quam necessitatibus molestiae unde, labore itaque culpa. Aliquam ut similique repudiandae nostrum."},
    {"image": "https://images.unsplash.com/photo-1581403341630-a6e0b9d2d257?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHdvbWFuJTIwcHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D", "comment": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Odio error consequuntur possimus ipsa, fugiat laborum dolor vero a quam necessitatibus molestiae unde, labore itaque culpa. Aliquam ut similique repudiandae nostrum."},
    {"image": "https://media.istockphoto.com/id/1285124274/photo/middle-age-man-portrait.jpg?s=612x612&w=0&k=20&c=D14m64UChVZyRhAr6MJW3guo7MKQbKvgNVdKmsgQ_1g=", "comment": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Odio error consequuntur possimus ipsa, fugiat laborum dolor vero a quam necessitatibus molestiae unde, labore itaque culpa. Aliquam ut similique repudiandae nostrum."}
]

faqs = [
    {"question": "Quaerat maxime aperiam iste provident necessitatibus repellendus consequuntur quae odio laboriosam quos delectus nobis quidem aliquam quod, vitae distinctio dolore et illo?", "answer": "Cupiditate quos voluptas accusantium ut molestiae officia, dolorem, iure obcaecati ratione modi consequatur quidem? Incidunt quo repellendus nemo officia error harum ipsam modi illum, accusantium ut animi quod odio laborum vero ratione tenetur fugit repellat! Voluptatum sapiente, quo mollitia voluptas dolorem cupiditate dolores recusandae, reiciendis totam dolore enim, animi consequuntur quaerat. Iusto!"},
    {"question": "iusto delectus animi assumenda iste at? Adipisci?", "answer": "fuga saepe nihil minima quos maxime cumque soluta harum earum assumenda aspernatur ducimus voluptatum numquam eaque porro, nam ut voluptatibus? Vel quasi assumenda illum ipsam optio voluptatibus, ducimus, placeat dolores impedit, sunt quo cumque a laboriosam magnam. Architecto cum accusantium sapiente iusto doloribus maxime, blanditiis hic porro iste autem vel voluptatem provident sit fugit magnam excepturi saepe consequuntur maiores, officiis expedita, illo molestiae est culpa? Fugit a fuga odio ipsam ullam."},
    {"question": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequatur, inventore?", "answer": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt, officia odit qui, animi inventore ad iste ipsa dolore, repellat minima voluptatem! A debitis atque, dicta illumdignissimos harum maxime adipisci."},
    {"question": "consequuntur minima sed voluptate fuga quod omnis, aut, sint odio hic non impedit velit in quaerat aspernatur iste eos ducimus?", "answer": "odit Magnam obcaecati nemo sequi possimus molestiae, nulla reprehenderit natus porro, voluptatibus, ducimus veritatis maiores minus nihil esse!"}
]

@app.route("/")
def index():
    return render_template("about.html", images=images)

@app.route("/customers")
def customers_page():
    return render_template("customers.html", customers=customers)

@app.route("/faq")
def faqs_page():
    return render_template("faq.html", faqs=faqs)

app.run(debug=True)
