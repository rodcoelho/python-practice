import stock, reader
from tableformat import TextTableFormatter, ColumnFormatMixin, print_table, PortfolioFormatter, create_formatter

portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)

formatter = create_formatter("text", upper_headers=True, column_formats=['"%s"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)