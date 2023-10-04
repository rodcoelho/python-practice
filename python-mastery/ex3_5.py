import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)

# formatter = tableformat.TextTableFormatter()
# tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)

# formatter = tableformat.CSVTableFormatter()
# tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)

formatter = tableformat.create_formatter("text")
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)

