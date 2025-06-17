from flask import Blueprint, make_response
from models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizza')

@pizza_bp.route('', methods=['GET'])
def my_get():
    this_list=[]
    for p in Pizza.query.all():
        this_dict={
            'id':p.id,
            'name':p.name,
            'ingredients':p.ingredients
        }
        this_list.append(this_dict)

    return make_response(this_list)    