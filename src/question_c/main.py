#add import

import question_c
from question_c import stock_list, Stock


def display_menu():
    print('Choose a menu option:')
    print('1:Show stock purchase history')
    print('2:Exit Program')

def run_menu(Stock):
    display_menu()
    option = str(input('Select Option 1 or 2: '))
    while(option != '1' and option != '2'):
        print(str(input('invalid selection. Please type 1 or 2: ')))
    menu_option(option, Stock)

def menu_option(option, Stock):
    if option == '1':
        Stock.stock_purchase_history(stock_list)
        try_again(Stock)
    if option == '2':
        while True:
            exit = input("Are you sure you would like to exit? Type yes or no: ")
            if exit == "yes" or exit == "Yes":
                print("Exiting now. Goodbye!")
                break
            elif exit == "no" or exit == "No":
                run_menu(Stock)
            else:
                print("please Enter yes or no: ")
    

def try_again(Stock):
    while True:
        x = input("Would you like to continue? Type yes or no: ")
        if x.casefold() == "no":
            print("Exiting Now! Bye!")
            break
        elif x.casefold() == "yes":
            run_menu(Stock)
            break

run_menu(Stock)
