#write functions here, don't add input('') statements here!
def test_config():
    return True


def create_multiplication_table(rows, columns):
    table = []
    for i in range (rows):
        row = []
        for j in range (columns):
            row.append((i + 1) * (j + 1))
        table.append(row)
    return(table)

def display_multiplication_table(table):
    for row in table:
        print()
        for value in row:
            print(f'{value:4}', end = '')

   



    
      
        

    
    