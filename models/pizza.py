from server.extentions import db

# initializa a pizza model

class Pizza(db.Model):
    __tablename__='my_pizza'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)

    restaurants=db.relationship('Restaurant_pizza',back_populates='pizza')

    def __repr__(self):
        return f'<Pizza {self.id}, {self.name}, {self.ingredients}>'