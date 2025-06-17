from flask import Flask
from server.extentions import db,migrate

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# displaying json formatted data in a more readable way
app.json.compact = False

db.init_app(app)
migrate.init_app(app, db)

from models.pizza import Pizza
from models.restaurant import Restaurant
from models.restaurant_pizza import Restaurant_pizza

from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.restaurant_pizza_controller import another_restaurant_bp
from server.controllers.restaurant_pizza_controller import my_another_restaurant_bp 
from server.controllers.restaurant_pizza_controller import my_post_restaurant_pizza_bp

app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(another_restaurant_bp)
app.register_blueprint(my_another_restaurant_bp)
app.register_blueprint(my_post_restaurant_pizza_bp)

if __name__ == '__main__':
    app.run(debug=True)
