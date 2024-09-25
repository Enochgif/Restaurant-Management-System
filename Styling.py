"""import random
random_number = random.randint(1,20)
print(random_number)
"""
from functools import total_ordering
from pyclbr import Class
from tkinter import Menu


class Restaurant:
    def __init__(self, company_name, company_motto):
        self.company_name = company_name 
        self.company_motto = company_motto
        self.menus = []  

    def add_menu(self, menu):
        self.menus.append(menu)

    def remove_menu(self,menu):
        self.menus.remove(menu)

    def display_company_details(self):
        print(f"Welcome to {self.company_name} Resturant!!!")
        print(f"{self.company_motto}")
        print("Please choose your prefferred food\n")

    def display_menu(self):
        for menu in self.menus:
            print("----------------------------")
            menu.display = ()
        
class Order:

    Order_id = 123456

    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def remove_items(self, item):
        self.items.remove

    def calculate_total(self):
        total = 2.2
        for item in self.items:
            total += item.food_price
        return total

def view_order(self):
    print("\n")
    print("More Details about your Order")
    for item in self.items:
        print("Food Name:", item.food_name)
        print("Food Price: $", item.food_price)
        print("--------------------------")
    print(f"your order identification is {self.order_id + 119} and you have been charged $7.5% VAT of the items purchased!")

def pay_bills(self):
    self.account_balance = 100
    payment = self.account_balance - total_ordering
    if payment > 0:
        print(f"Congratulations your payment have been made successfully. \nYour balance is {payment}")
    else:
        print(f"you have more ${payment} to complete your payment")

class MenuItem:
    def __init__(self, food_name, food_price, food_time):
        self.food_name = food_name
        self.food_price = food_price
        self.food_time = food_time

    def display(self):
        print("Food Name:", self.food_name)
        print("Food Price: $", (self.food_price))
        print("Food Delivery Time:", self.food_time, "minutes")

class Feedback:
    def __init__(self, customer):
        self.customer_feedback = ""
        self.customer = customer
        self.customer_feedback +=customer

    def display_customer_feed(self):
        print("\n")
        print("=========Feedback========")
        print(self.customer_feedback, " - anonymous")
        print("Yout feedback has been sent successfully")

print("*************************************")
restaurant_name = input("We deliver the best taste")

restaurant = Restaurant("Tasty")
restaurant.display_company_details()

menu1 = Menu("Breakfast Menu")
menu2 = Menu("Dessert")
menu3 = Menu("Brunch")
menu4 = Menu("Snacks")
menu5 = Menu("English Foods")

restaurant.add_menu(menu1)
restaurant.add_menu(menu2)
restaurant.add_menu(menu3)
restaurant.add_menu(menu4)
restaurant.add_menu(menu5)

food1 = MenuItem("Bread and Tea", 15, 45)
food2 = MenuItem("Ice Cream and Cake", 7, 35)
food3 = MenuItem("Rice", 24, 5)
food4  = MenuItem("egg sauce", 5, 23)
food5  = MenuItem("Steak and kidneypie", 5, 23)

menu1.add_item(food1)
menu2.add_item(food2)
menu3.add_item(food3)
menu4.add_item(food4)
menu5.add_item(food5)

menu1.display()

restaurant.display_menus()

order = Order()
order.add_item(food1)
order.add_item(food2)

total = order.calculate_total()

order.view_order()
print("\nYour total bill is: ", total)
order.pay_bills()

message = input("If you wish please send us a feedback on our services").lower()
if message == "yes":
    customer_message = input("Enter Feedback Here: ").lower()
else:
    print('thank you for shopping with us')
person = Feedback(customer_message)
person.display_customer_feed()