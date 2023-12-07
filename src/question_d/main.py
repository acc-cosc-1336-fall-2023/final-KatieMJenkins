#add import

from question_d import Stock 

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
        result_dict = Stock.get_stock_list()
        print("Stock Purchase History")
        print('-' * 23)
        print('{:<10} {:<10}'.format("Symbol", "Company Name"))
        print('-' * 23)
        for symbol, company_name in result_dict.items():
            print('{:<10} {:<10}'.format(symbol, company_name))
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