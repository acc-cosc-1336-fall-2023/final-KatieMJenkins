#add import

from question_a import create_multiplication_table
from question_a import display_multiplication_table

def try_again():
    while True:
        z = input("Would you like to try again? type yes or no: ")
        if z == 'yes' or z == 'Yes':
            run_main()
            break
        elif z == 'no' or z == 'No':
            print('Exiting now. Goodbye.')
            break
        else:
            print('Invalid selection. Type yes or no: ')

def run_main():
        while True:
            try:
                rows = int(input("Please enter the number of rows for your multiplication table: "))
                columns = int(input("Please enter the number of columns for your multiplication table: "))
            except ValueError:
                 print('Please enter integer values for rows and columns.')
                 continue
            mult_table = create_multiplication_table(rows, columns)

            display_multiplication_table(mult_table)
            print()
            try_again()
            break


print("This program will create a multiplication table for you!")
run_main()