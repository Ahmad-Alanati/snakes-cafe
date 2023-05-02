menu = {
    "Appetizers":["Wings","Cookies","Spring Rolls"],
    "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"]
}

def intro():
    str_intro = '''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
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
    return user_input

def main():
    intro()
    showmenu()
    
main()