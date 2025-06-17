from server.extentions import db

# initializa a restaurant model

class Restaurant(db.Model):
    __tablename__='my_restaurant'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)

    pizzas=db.relationship('Restaurant_pizza',back_populates='restaurant',cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name}, {self.address}'