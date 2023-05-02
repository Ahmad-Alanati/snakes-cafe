import re

menu = {
    "Appetizers":["Wings","Cookies","Spring Rolls"],
    "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"]
}

user_orders ={}

def intro():
    str_intro = '''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
** To see your cart, type "cart" **
**************************************
'''
    print(str_intro)

def showmenu():
    for category in menu:
        str_menu = '''{}
----------------------------------------------------------------------------------------------------------------------------------\n'''
        for item in menu[category]:
            str_menu+= "\\" + item + "\t"
        print(str_menu.format(category)+"\n")

def user_input_menu():
    user_input = input(">")
    user_input = user_input.replace(user_input[0],user_input[0].upper())
    return user_input

def orders():
    show_promt = '''
***********************************
** What would you like to order? **
***********************************'''
    print(show_promt)
    order = user_input_menu()
    while(order.lower() != "quit"):
        if(order.lower() == "cart"):
            show_orders()
            order = user_input_menu()
            continue
        if check_if_exists(order):
            if order in user_orders:
                user_orders[order] = user_orders[order]+1
            else:
                user_orders[order] = 1
        else:
            print("sorry this item dosen't exists in our menu")
        order = user_input_menu()

def check_if_exists(order):
    if order in menu["Appetizers"]:
        return True
    if order in menu["Desserts"]:
        return True
    if order in menu["Drinks"]:
        return True
    if order in menu["Entrees"]:
        return True
    return False

def show_orders():
    for item in user_orders:
        str = "{} order of {} has been added to your meal"
        print(str.format(user_orders[item],item))


def main():
    intro()
    showmenu()
    orders()

main()