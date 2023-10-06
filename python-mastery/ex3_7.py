import stock, reader
from tableformat import print_table, TableFormatter

portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)

class MyFormatter(TableFormatter):
    def headings(self,headers): 
        pass
    def row(self,rowdata): 
        pass


print_table(portfolio, ['name','shares','price'], MyFormatter())
