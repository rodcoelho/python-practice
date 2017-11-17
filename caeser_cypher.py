def decimal_to_roman(ameri_num):
    roman_output = ""
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    for i in range(len(ints)):
        # divide the input number by the ints, if ameri_num is divided by a bigger number, then
        # the non_fraction variable becomes zero and nothing is added to the final output
        # the loop forces itself to the next largest number until something divisible takes place
        non_fraction = int(ameri_num / ints[i])
        roman_output += nums[i] * non_fraction
        ameri_num -= ints[i] * non_fraction
    return roman_output

def roman_to_dec(roman_num):
    nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    ints = [1000, 500, 100, 50, 10, 5, 1]
    pos_list = []
    real_list = []
    ameri_num = 0
    for letters in roman_num:
        location = nums.index(letters)
        pos_list.append(ints[location])
    for i in range(len(pos_list)):
        try:
            nexti = pos_list[i+1]
            if pos_list[i]> nexti:
                real_list.append(pos_list[i])
            else:
                real_list.append(pos_list[i]*-1)
        except:
            real_list.append(pos_list[-1])
    for elements in real_list:
        ameri_num += elements
    return ameri_num