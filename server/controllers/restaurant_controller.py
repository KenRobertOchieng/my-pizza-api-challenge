from flask import Blueprint,make_response
from models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurant')

@restaurant_bp.route('',methods=['GET'])
def my_get():
    my_list=[]
    for r in Restaurant.query.all() :
        my_dict={
            'id':r.id,
            'name':r.name,
            'address':r.address
        }
        my_list.append(my_dict)

    return make_response(my_list)    
