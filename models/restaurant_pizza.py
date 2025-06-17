from server.extentions import db
from sqlalchemy import CheckConstraint

# initializa a restaurant_pizza model

class Restaurant_pizza(db.Model):
    __tablename__='restaurant_pizza'

    id=db.Column(db.Integer, primary_key=True)
    prize=db.Column(
        db.Integer,
        CheckConstraint('price >= 1 AND price <= 30', name='price_between_1_and_30'),
        nullable=False
        )

    restaurant_id=db.Column(db.Integer,db.ForeignKey('my_restaurant.id'))
    pizza_id=db.Column(db.Integer,db.ForeignKey('my_pizza.id'))

    restaurant=db.relationship('Restaurant',back_populates='pizzas')
    pizza=db.relationship('Pizza',back_populates='restaurants')

    def __repr__(self):
        return f'<Restaurant_pizza {self.id}, Price: {self.prize}'
    


