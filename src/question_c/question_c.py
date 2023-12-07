#write functions here, don't add input('') statements here!

class Stock:

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
    def stock_purchase_history(stock_list):
        for s in stock_list:
            stock_dict = {s.__symbol: s.__company_name for s in stock_list}
        print("Stock List")
        print('{:<10} {:<10}'.format("Symbol", "Company Name"))
        print('-' * 23)
        for symbol, company_name in stock_dict.items():
            print('{:<10} {:<10}'.format(symbol, company_name))
                
s1 = Stock('AAPL', 'Apple Inc')
s2 = Stock('CAT', 'Caterpillar')
s3 = Stock('EK', 'Eastman Kodak')
s4 = Stock('Goog', 'Google')
s5 = Stock('MSFT', 'Microsoft')
stock_list = [s1, s2, s3, s4, s5]
        