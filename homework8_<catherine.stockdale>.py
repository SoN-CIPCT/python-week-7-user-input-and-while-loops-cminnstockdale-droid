
#You are in charge of making sure all pizza orders are made on time at your restaurant.  Perform the following to check that all orders have been fulfilled.
#1.	Make a list called pizza_orders and populate it with names of pizzas that have been ordered.
pizza_orders = [
        "Pepperoni",
        "Hawaiian",
        "12th Man Primo",
        "Veggie",
        "Cheese with Stuffed Crust",
        "Dessert",
]

#2.	Make an empty list called finished_pizzas.
finished_pizzas = []
#3.	Loop through the list of pizza orders and print a message for each order, saying “Your pizza pie is finished!”.
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print(f"Your {current_pizza} pizza pie is finished!")
#4.	After the pizza is made and a message has been printed for a pizza order, move that pizza to the list finished_pizzas.
    finished_pizzas.append(current_pizza)
#5.	After all of the pizzas have been made, print a message “The pizza {name} was made.” for each finished pizza, replacing {name} with the pizza’s name. 
for finished_pizza in finished_pizzas:
    print(f"The pizza {finished_pizza} was made.")
#6.	Submit your finished program.
