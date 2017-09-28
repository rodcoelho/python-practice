
# ## CHECK STRING FOR DUPLICATES
# s1 = 'abccc'
# s2 = 'abcd'
#
# def check_string(s):
#     x = 0
#     for chars in s:
#         if s.count(chars)>1:
#             x+=1
#     if x>0:
#         print (False)
#     else:
#         print (True)
#
# check_string(s1)
# check_string(s2)



# ## Reverse C-Style Strings (strings with 5 chars... so 'abcd' is really 'abcd_' and would turn into '_dcba')
# s1 = 'abcde'
# s2 = 'abcd'
# s3 = 'abcdef'
#
# def reverse_Cstring(s):
#     if len(s)<5:
#         s+= ' '*(5-len(s))
#     elif len(s)>5:
#         s=s[:5]
#     rev_s = s[::-1]
#     print(rev_s)
#
# reverse_Cstring(s1)
# reverse_Cstring(s2)
# reverse_Cstring(s3)





# # ## Remove duplicate chars in string
#
# s1 = 'abcc'
# s2 = 'abac'
# s3 = 'aaa'
#
# def remove_dup(s):
#     new_s = ''
#     for chars in s:
#         if chars in new_s:
#             continue
#         else:
#             new_s += chars
#     print(new_s)
#
# remove_dup(s1)
# remove_dup(s2)
# remove_dup(s3)




#
# # ## Check if s1 and s2 are anagrams
#
# s1 = 'cinema'
# s2 = 'iceman'
#
# def anagram_test(s1,s2):
#     sl1 = list(s1)
#     sl2 = list(s2)
#     if len(sl1) != len(sl2):
#         print(False)
#     else:
#         ssl1 = sl1.sort()
#         ssl2 = sl2.sort()
#         if ssl1 == ssl2:
#             print(True)
#         else:
#             print(False)
#
# anagram_test(s1,s2)





# # Replace spaces in string with '%20'
#
# s1 = 'abc'
# s2 = 'abc cd'
# s3 = 'a  bc '
#
# def rep_space(s):
#     new_s= ''
#     for chars in s:
#         if chars == ' ':
#             new_s += '%20'
#         else:
#             new_s += chars
#     print(new_s)
#
# rep_space(s1)
# rep_space(s2)
# rep_space(s3)





# # Remove duplicates in list
# l1 = ['a','a','a']
# l2 = ['a','b','c']
# l3 = ['a', 'b', 'a', 'b']
# l4 = ['a', 'ab', 'b']
#
# def remove_dup_list(l):
#     temp_list = []
#     for items in l:
#         if items in temp_list:
#             continue
#         else:
#             temp_list.append(items)
#     print(temp_list)
#
# remove_dup_list(l1)
# remove_dup_list(l2)
# remove_dup_list(l3)
# remove_dup_list(l4)




# # Return middle element in list
#
# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5,6]
#
# def get_middle_element_in_list(l):
#     if len(l)%2 == 0:
#         print([l[len(l)/2-1],l[len(l)/2]])
#     else:
#         print(l[len(l)//2])
#
# get_middle_element_in_list(l1)
# get_middle_element_in_list(l2)




