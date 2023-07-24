import numpy as np

FILE = 'testmatrix.txt'

# loads the txt file
def import_matrix(txtfile):
    raw = []
    ready = []
    with open(txtfile,'r') as f:
        for line in f:
            raw.append(line.split())
    # results = list(map(int, raw))
    return raw

# data in the matrix is in string format, this func changes it into int
def parse_matrix_string_to_int():
    raw = import_matrix(FILE)
    less_raw = []
    for rows in raw:
        temp_l = []
        for elements in rows:
            temp_l.append(float(elements))
        less_raw.append(temp_l)
    return less_raw

def make_matrix_into_np_array():
    matrix = parse_matrix_string_to_int()
    npm = np.array(matrix)
    return npm

# sums the rows in the matrix
def sum_rows_in_matrix():
    matrix = parse_matrix_string_to_int()
    return [sum(row) for row in matrix]

# sums the columns in the matrix
def sum_columns_in_matrix():
    matrix = parse_matrix_string_to_int()
    return [sum(col) for col in zip(*matrix)]

# adds enumerates to the sum_row_matrix
def enum_sum_row():
    matrix = sum_rows_in_matrix()
    enum_row_list = []
    for count, sum_num in enumerate(matrix):
        enum_row_list.append([count, sum_num])
    return enum_row_list

# adds enumerates to the sum_column_matrix
def enum_sum_columns():
    matrix = sum_columns_in_matrix()
    enum_col_list = []
    for count, sum_num in enumerate(matrix):
        enum_col_list.append([count, sum_num])
    return enum_col_list

# sorts the enum row list
def sort_enum_row():
    # key function to help sort through enumurated lists
    def my_key(item):
        return item[1]
    return sorted(enum_sum_row(), key = my_key)

# sorts the enum column list
def sort_enum_col():
    # key function to help sort through enumurated lists
    def my_key(item):
        return item[1]
    return sorted(enum_sum_columns(), key=my_key)

# extracts emum from row list
def get_enum_only_row():
    entire_row = sort_enum_row()
    enum_row_list = []
    for elements in entire_row:
        enum_row_list.append(elements[0])
    return enum_row_list

# extracts emum from col list
def get_enum_only_col():
    entire_col = sort_enum_col()
    enum_col_list = []
    for elements in entire_col:
        enum_col_list.append(elements[0])
    return enum_col_list

def final_transformation_row():
    npm = make_matrix_into_np_array()
    row = get_enum_only_row()
    new_row_matrix = npm [row]
    return new_row_matrix

def final_transformation_col():
    npm = make_matrix_into_np_array()
    col = get_enum_only_col()
    new_col_matrix = npm[:, col]
    return new_col_matrix

x ,y = final_transformation_row(), final_transformation_col()

print('The Matrix transformed by row: {}'.format(x))
print(' ')
print('The Matrix transformed by column: {}'.format(y))
