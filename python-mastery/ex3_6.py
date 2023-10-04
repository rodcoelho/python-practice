import stock, reader, tableformat

portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
# print(portfolio)

# s1 = stock.Stock("GOOG", 10, 100.0)
# s2 = stock.Stock("GOOG", 10, 100.0)
# print(s1==s2)

with tableformat.redirect_stdout(open("out.text", "w")) as file:
    
    formatter = tableformat.create_formatter('text')
    tableformat.print_table(portfolio, ['name','shares','price'], formatter)
    file.close()