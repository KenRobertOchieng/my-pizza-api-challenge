from flask import Blueprint,make_response ,jsonify ,request
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import Restaurant_pizza
from  server.extentions import db

another_restaurant_bp = Blueprint('another_restaurant_bp', __name__, url_prefix='/restaurant-alt')

@another_restaurant_bp.route('/<int:id>', methods=['GET'])
def my_get(id):

    a_list=[]

    get_restaurant_data=Restaurant.query.get(id)

    if not get_restaurant_data :
        error_message={"error": f"Restaurant not found."}
        return make_response(jsonify(error_message), 404)

    # we will be returning a single restaurant and its pizzas

    # looping over pizzas

    for x in get_restaurant_data.pizzas :
        a_dict={
            'id':x.pizza.id,
            'name':x.pizza.name,
            'ingredients':x.pizza.ingredients
        }
        a_list.append(a_dict)

    restaurant_dict={
        'id':get_restaurant_data.id,
        'name':get_restaurant_data.name,
        'address':get_restaurant_data.address,
        'pizzas':a_list
    }

    return make_response(jsonify(restaurant_dict),200)

my_another_restaurant_bp = Blueprint('my_another_restaurant_bp', __name__, url_prefix='/restaurant-alt-delete')

@my_another_restaurant_bp.route('/<int:id>',methods=['DELETE'])
def my_delete(id):
    get_my_delete=Restaurant.query.get(id)

    if not get_my_delete :
       error_message={"error": f"Restaurant not found."}
       return make_response(jsonify(error_message), 404)
    
    # deleting the restaurant itself
    db.session.delete(get_my_delete)
    db.session.commit()

my_post_restaurant_pizza_bp = Blueprint('my_post_restaurant_pizza_bp', __name__, url_prefix='/restaurant-alt-post')

@my_post_restaurant_pizza_bp.route('',methods=['POST'])
def post_restaurant_pizza():
    thee_data=request.get_json()

    pizza_id=thee_data.get('pizza_id')
    restaurant_id=thee_data.get('restaurant_id')
    prize=thee_data.get('prize')

    # validation that price ranges between 1 and 30
    if not(1<= prize <=30):
        message_error={"errors": ["Price must be between 1 and 30"]}
        return make_response(jsonify(message_error),400)

    # retrieving existing pizza and restaurant from our data base
    pizza=Pizza.query.get(pizza_id)
    restaurant=Restaurant.query.get(restaurant_id)

    if restaurant is None or pizza is None:
        my_error_massage={"errors": ["Invalid pizza or restaurant ID"]}
        return make_response(jsonify(my_error_massage),400)

    # create our restaurant_pizza
    my_restaurant_pizza=Restaurant_pizza(prize=prize,restaurant=restaurant,pizza=pizza)

    db.session.add(my_restaurant_pizza)
    db.session.commit()

    #our full data
    post_restaurant_pizza_dict={
        'id':my_restaurant_pizza.id,
        'prize':my_restaurant_pizza.prize,
        'restaurant_id':my_restaurant_pizza.restaurant.id,
        'pizza_id':my_restaurant_pizza.pizza.id,
        'pizza':{
            'id':pizza.id,
            'name':pizza.name,
            'ingredients':pizza.ingredients
        },
        'restaurant':{
            'id':restaurant.id,
            'name':restaurant.name,
            'address':restaurant.address
        }
    }

    return make_response(jsonify(post_restaurant_pizza_dict),201)
    







