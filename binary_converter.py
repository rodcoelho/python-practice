def prep_num_for_rev(num):
    num_string = str(num)
    num_list = list(num_string)
    rev_list = num_list[::-1]
    return rev_list

def binary_to_decimal(num):
    rev_list = prep_num_for_rev(num)
    dec_pre_sum = []
    dec = 0
    for i in range(len(rev_list)):
        dec_pre_sum.append(int(rev_list[i])* (2**i))
    dec = sum(dec_pre_sum)
    return dec

def decimal_to_binary(num):
    print('The conversion of decimal {} in binary is: '.format(num),end='')
    def recursive_dec_to_bin(num):
        if num > 1:
            recursive_dec_to_bin(num // 2)
        print(num % 2, end= '')
    recursive_dec_to_bin(num)
    print()