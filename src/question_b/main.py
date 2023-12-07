#add import

from question_b import get_most_likely_ancestor_consensus

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
            dna_string1 = str(input("Enter DNA string of length 8 to 16 characters: "))
            dna_string2 = str(input("Enter DNA substring of 4 characters: "))
            break
        except ValueError:
            print('Not a valid Entry')
    if (len(dna_string1) >= 8 and len(dna_string1) <= 16 and len(dna_string2) == 4): 
                result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
                print(result)
                try_again()
    else:
        print('Invalid entry')
        run_main()        

print("We will find all starting locations of your DNA substring withing your DNA strand.")
run_main()


