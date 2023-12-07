#write functions here, don't add input('') statements here!

class Stock:

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
    def get_stock_list():
        stock_dict = {}

        with open('stocklist.txt', 'r') as file:
            lines = (file.readlines())

            for line in lines:
                symbol, company_name = line.strip().split(',')
                s = Stock(symbol, company_name)
                stock_dict[symbol] = company_name

        return stock_dict
    

