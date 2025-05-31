from src.ext import db
from src.models import BaseModel


class User(BaseModel):

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

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    def edit(self, form):
        self.username = form.username.data
        self.password = form.password.data
        db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
