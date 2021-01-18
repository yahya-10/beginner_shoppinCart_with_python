import sys


def main_menu():
    while True:
        print()
        print('''###SHOPPING CART
        
        Select an option from the list below
        
        1.Show all items in the cart
        2.Add item to the cart
        3.Remove item from cart
        4.Check if item exists in the cart
        5.How many items in the cart
        6.Cleat the cart
        7.Exit
        ''')

        selection = input("Enter your option: ")
        if selection == "1":
            show_items()
        elif selection == "2":
            add_item()
        elif selection == "3":
            remove_item()
        elif selection == "4":
            check_item()
        elif selection == "5":
            count_of_items_in_cart()
        elif selection == "6":
            clear_cart()
        elif selection == "7":
            sys.exit()
        else:
            print("Wrong option!!")


shopping_cart = ["Milk", "Whole Grain Bread", "Chicken Breasts", "Bananas"]


def show_items():
    for i in shopping_cart:
        print("-> ", i)


def add_item():
    new_item = input("Enter the new item you want to add: ")
    shopping_cart.append(new_item)
    print(new_item + " has been added to the cart")


def remove_item():
    unwanted_item = input("Enter the item you want to remove from cart: ")
    shopping_cart.remove(unwanted_item)
    print(unwanted_item + " has been removed successfully!!")


def check_item():
    item_to_check = input("Enter the item you're looking for: ")
    for i in shopping_cart:
        if i == item_to_check:
            print(item_to_check + " exists in the cart!")


def count_of_items_in_cart():
    print("There are ", len(shopping_cart), " item in cart")


def clear_cart():
    shopping_cart.clear()
    print("Shopping cart is clear!!")


main_menu()




