from server.app import app
from server.extentions import db
from models.restaurant import Restaurant
from models.pizza import Pizza 
from models.restaurant_pizza import Restaurant_pizza

# creating pizza objects
with app.app_context():
  
  pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
  pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
  pizza3 = Pizza(name="BBQ Chicken", ingredients="BBQ Sauce, Chicken, Red Onions, Mozzarella")
  pizza4 = Pizza(name="Hawaiian", ingredients="Tomato, Ham, Pineapple, Mozzarella")
  pizza5 = Pizza(name="Veggie Delight", ingredients="Tomato, Bell Peppers, Olives, Mushrooms, Onions")


  db.session.add_all([pizza1,pizza2,pizza3,pizza4,pizza5])
  db.session.commit()

# creating restaurant objects

  restaurant1 = Restaurant(name="Mama's Kitchen", address="123 Garden Lane")
  restaurant2 = Restaurant(name="Ocean Breeze Diner", address="45 Seaside Avenue")
  restaurant3 = Restaurant(name="Mountain View Grill", address="789 Summit Road")
  restaurant4 = Restaurant(name="Downtown Bites", address="101 City Center Blvd")
  restaurant5 = Restaurant(name="The Rustic Spoon", address="66 Countryside Drive")


  db.session.add_all([restaurant1,restaurant2,restaurant3,restaurant4,restaurant5])
  db.session.commit()

# Many-to-many relationship between pizza and restaurant through restaurant_pizza

  assocition_1=Restaurant_pizza(prize=25.0,restaurant=restaurant4,pizza=pizza2)
  assocition_2=Restaurant_pizza(prize=21.0,restaurant=restaurant5,pizza=pizza1)
  assocition_3=Restaurant_pizza(prize=16.0,restaurant=restaurant1,pizza=pizza1)
  assocition_4=Restaurant_pizza(prize=23.0,restaurant=restaurant3,pizza=pizza4)
  assocition_5=Restaurant_pizza(prize=10.0,restaurant=restaurant4,pizza=pizza3)
  assocition_6=Restaurant_pizza(prize=29.0,restaurant=restaurant1,pizza=pizza4)
  assocition_7=Restaurant_pizza(prize=24.0,restaurant=restaurant5,pizza=pizza2)
  assocition_8=Restaurant_pizza(prize=29.0,restaurant=restaurant1,pizza=pizza5)
  assocition_9=Restaurant_pizza(prize=27.0,restaurant=restaurant5,pizza=pizza3)
  assocition_10=Restaurant_pizza(prize=23.0,restaurant=restaurant5,pizza=pizza4)
  assocition_11=Restaurant_pizza(prize=20.0,restaurant=restaurant5,pizza=pizza5)
  assocition_12=Restaurant_pizza(prize=15.0,restaurant=restaurant1,pizza=pizza2)

  db.session.add_all([assocition_1,assocition_2,assocition_3,assocition_4,assocition_5,assocition_6,assocition_7,assocition_8,assocition_9,assocition_10,assocition_11,assocition_12])
  db.session.commit()


