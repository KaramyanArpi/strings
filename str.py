# message = "Hello World!"
# text = ("Laudate omnes gentes laudate "
#         "Magnificat in secula ")
# print(text)
#
# print(message[0],len(message),message[:3])
#
# name = "Tom"
# surname = "Smith"
# fullname = name + " " + surname
# print(fullname)  # Tom Smith
#
# print("a" * 3)  # aaa
# print("he" * 4)  # hehehehe"
import collections


#homework
# name = "Arpi"
# surname = "Karamyan"
# profession = "I'm programmer"
# print(f"Name: {name}   Surname: {surname}   Profession: {profession}")
# print("Name: {}   Surname: {}   Profession: {}".format(name, surname, profession))
# print("Name: {1}   Surname: {0}   Profession: {2}".format(surname, name, profession))
# print("Name: {name1}   Surname: {surname1}   Profession: {profession1}".
#       format(name1=name, surname1=surname, profession1=profession))


#138
# def string_func(len_str, string, symbol):
#     try:
#         if len(string) == len_str:
#             count = string.count(symbol)
#             # for i in user_string:
#             #     if symbol == i:
#             #         count += 1
#             if count > 0:
#                 return f"Str: {string}  Length str: {len_str}  Count symbol: {count}"
#             else:
#                 return "There is no such symbol in the string"
#         raise ValueError("The length of the line must match the number you entered")
#
#     except ValueError as e:
#         print(f"Exception handled: {e}")
#
#
# len_string = int(input("Enter string length: "))
# user_string = input("Enter string: ")
# symbol_u = input("Enter the symbol, you want to find in the string: ")
#
# print(string_func(len_string, user_string, symbol_u))

#139
# def palindrome(string):
#     if string == string[::-1]:
#         return True
#     return False
#
#
# user = input("Enter string: ")
# print(palindrome(user))

#140
# def zero_count(len_str, string):
#     if len(string) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#     index_x = string.find("x")
#     if index_x == -1:
#         return 0
#     return string[index_x + 1:].count("0")
#
#
# num = int(input("Enter length string: "))
# user_str = input("Enter string: ")
# print(zero_count(num, user_str))

#141
# def find_symbol(len_str, string):
#     res = 0
#     if len(string) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#     first_index_z = string.index("z")
#     second_index_z = string.rindex("z")
#     if string.count("z") <= 1:
#         return 0
#     return len(string[first_index_z + 1:second_index_z])
#
#
# num = int(input("Enter length string: "))
# user_str = input("Enter string: ")
# print(find_symbol(num, user_str))

#142
# def str_func(len_str, string1, string2):
#     count = 0
#     set1 = set()
#     if len(string1) != len_str or len(string2) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#     for i in string1:
#         if i in string2 and i not in set1:
#             if string1.count(i) <= 2:
#                 count += 1
#                 set1.add(i)
#
#     return count
#
#
# num = int(input("Enter length string: "))
# user_str1 = input("Enter string 1: ")
# user_str2 = input("Enter string 2: ")
# print(str_func(num, user_str1, user_str2))


#142/2
# def str_func(len_str, string1, string2):
#     count = 0
#     if len(string1) != len_str or len(string2) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#
#     dict1 = {}
#     dict2 = {}
#
#     for i in string1:
#         dict1[i] = dict1.get(i, 0) + 1
#
#     for i in string2:
#         dict2[i] = dict2.get(i, 0) + 1
#
#     for i in string1:
#         if dict1.get(i) == dict2.get(i):
#             count += 1
#
#     return count
#
#
# num = int(input("Enter length string: "))
# user_str1 = input("Enter string 1: ")
# user_str2 = input("Enter string 2: ")
# print(str_func(num, user_str1, user_str2))


#143
# def new_str(len_str, string):
#     new_string = ""
#     if len(string) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#     for i in string:
#         if string.count(i) == 1:
#             new_string += i
#
#     return new_string
#
#
# num = int(input("Enter length string: "))
# user_str = input("Enter string: ")
# print(new_str(num, user_str))


#144
# def str_func(len_str, string1, string2):
#     new_str = ""
#     if len(string1) != len_str or len(string2) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#     for i in string1:
#         if string1.count(i) == string2.count(i):
#             new_str += i
#
#     return new_str
#
#
# num = int(input("Enter length string: "))
# user_str1 = input("Enter string 1: ")
# user_str2 = input("Enter string 2: ")
# print(str_func(num, user_str1, user_str2))


# def str_func(len_str, string1, string2):
#     new_str = ""
#     set1 = set()
#     if len(string1) != len_str or len(string2) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#     for i in string1:
#         if i in string2 and i not in set1:
#             new_str += i
#             set1.add(i)
#
#     return new_str
#
#
# num = int(input("Enter length string: "))
# user_str1 = input("Enter string 1: ")
# user_str2 = input("Enter string 2: ")
# print(str_func(num, user_str1, user_str2))

#145
# def new_str(len_str, string):
#     new_string = ""
#     if len(string) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#
#     # for i in string:
#     #     if i != "a":
#     #         new_string += i
#     #     elif i == "a":
#     #         new_string += i + "c"
#     return string.replace("a", "ac")
#
#
# num = int(input("Enter length string: "))
# user_str = input("Enter string: ")
# print(new_str(num, user_str))

#146
# def new_str(len_str, string):
#
#     if len(string) != len_str:
#         raise ValueError("The length of the line must match the number you entered!")
#     # for i in string:
#     #     if i != "a":
#     #         new_string += i
#
#     return string.replace("a", " ")
#
#
# num = int(input("Enter length string: "))
# user_str = input("Enter string: ")
# print(new_str(num, user_str))


#1
# string = input("Enter string: ")
# print(len(string))

#2
# def my_dict(string):
#
#     dict_sym = {}
#
#     for i in string:
#         dict_sym[i] = dict_sym.get(i, 0) + 1
#
#     return dict_sym
#
#
# user = input("Enter string: ")
# print(my_dict(user))

#3
# def new_string(string):
#     if len(string) <= 1:
#         return None
#     elif len(string) <= 3:
#         return string * 2
#     else:
#         return string[2:] + string[-2:]
#
#
# user = input("Enter string: ")
# print(new_string(user))

#4
# def symbol_of_str(string):
#     if len(string) <= 1:
#         return None
#
#     new_str = ""
#     first_sym = string[0]
#
#     for i in range(len(string)):
#         if string[i] == first_sym and i != 0:
#             new_str += "$"
#         else:
#             new_str += string[i]
#
#     return new_str
#
#
# user = input("Enter string: ")
# print(symbol_of_str(user))

#5
# def swap_first_two_chars(str1, str2):
#     if len(str1) < 2 or len(str2) < 2:
#         return None
#
#     new_str1 = str2[:2] + str1[2:]
#     new_str2 = str1[:2] + str2[2:]
#
#     return f"{new_str1} {new_str2}"
#
#
# string1 = input("Enter: ")
# string2 = input("Enter: ")
# print(swap_first_two_chars(string1, string2))

#6
# def my_string(string):
#     if len(string) < 3:
#         return None
#
#     if string.endswith("ing"):
#         string += "ly"
#     else:
#         string += "ing"
#
#     return string
#
#
# user = input("Enter: ")
# print(my_string(user))

#7
# def not_poor(string):
#     if string.startswith("not"):
#         string = "good"
#     return string
#
#
# user = input("Enter: ")
# print(not_poor(user))

#8
# def max_length(string):
#     maximum = ""
#     max_len = 0
#     for word in string:
#         if len(word) >= max_len:
#             maximum = word
#
#     return maximum
#
#
# user = input("Enter: ").split()
# print(max_length(user))

#9
# def remove_sym(num, string):
#     if len(string) < 1:
#         return None
#     new_str = ""
#     for i in range(len(string)):
#         if num != i:
#             new_str += string[i]
#
#     return new_str
#
#
# number = int(input("Enter num: "))
# user = input("Enter: ")
# print(remove_sym(number, user))

#10
# def start_end(string):
#     if len(string) <= 1:
#         return string
#     return string[-1] + string[1:-1] + string[0]
#
#
# user = input("Enter: ")
# print(start_end(user))

#11
# def odd_index_remove(string):
#     new_str = ""
#
#     for i in range(len(string)):
#         if i % 2 == 0:
#             new_str += string[i]
#     return new_str
#
#
# user = input("Enter: ")
# print(odd_index_remove(user))

#12
# def count_word(string):
#     words = string.split()
#     word_count = {}
#
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1
#
#     return word_count
#
#
# user = input("Enter: ")
# print(count_word(user))

#13
# string = input("Enter: ")
# print(string.lower())
# print(string.upper())

#14
# def sort_str(string):
#     words = string.split(", ")
#     seen = set()
#     new_str = []
#
#     for word in words:
#         if word not in seen:
#             seen.add(word)
#             new_str.append(word)
#
#     return ", ".join(new_str)
#
#
# user = input("Enter a string: ")
# print(sort_str(user))

#15
# def add_tags(tag, word):
#     return f"<{tag}>{word}</{tag}>"
#
#
# print(add_tags("i", "Python"))
# print(add_tags("b", "Python Tutorial"))

#16
# def string_middle(original, insert):
#
#     middle_index = len(original) // 2
#
#     return original[:middle_index] + insert + original[middle_index:]
#
#
# print(string_middle('[[]]<<>>', "Python"))
# print(string_middle('(f)', 'PHP'))

#17
# def end(string):
#     if len(string) < 2:
#         return None
#     return string[-2:] * 4
#
#
# print(end("Python"))
# print(end("Exercises"))

#18
# def first_three(string):
#     return string[:3] if len(string) >= 3 else string
#
#
# print(first_three('ipy'))
# print(first_three('python'))

#19
# def get_last_part_before_char(string, char):
#     index = string.rfind(char)
#
#     if index != -1:
#         return string[:index]
#     else:
#         return string
#
#
# print(get_last_part_before_char("https://www.w3resource.com/python-exercises", "/"))
# print(get_last_part_before_char("https://www.w3resource.com/python", "/"))

#20
# def reverse_if_multiple_of_4(string):
#
#     if len(string) % 4 == 0:
#         return string[::-1]
#     else:
#         return string
#
#
# print(reverse_if_multiple_of_4("hello"))
# print(reverse_if_multiple_of_4("test"))
# print(reverse_if_multiple_of_4("abcd"))


#147
# def str_fun(n):
#     string = ""
#     for i in range(n):
#         user = input(f"Enter letter {i + 1}: ")
#         string += user
#
#     string = string[::-1]
#     return string
#
#
# num = 5
# print(str_fun(num))

#148
# def str_func(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                      for i in range(n))
#
#     return string.replace("x", "yy")
#
#
# number = int(input("Enter number: "))
# print(str_func(number))

#149
# def function(string):
#     str1 = ""
#     for i in range(0, len(string) - 1, 2):
#         if string[i] > string[i + 1]:
#             str1 += string[i]
#         else:
#             str1 += string[i + 1]
#     return str1
#
#
# user = input("Enter: ")
# print(function(user))

#150
# def str_func(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                      for i in range(n))
#
#     if "x" in string:
#         return f"There is 'x' in the string. Quantity 'c': {string.count("c")}"
#     else:
#         return f"There is not 'x' in the string. Quantity 'd': {string.count("d")}"
#
#
# number = int(input("Enter number: "))
# print(str_func(number))

#151
# def function(string):
#     new_str = ""
#     for i in range(len(string)):
#         if i % 3 == 2:
#             new_str += "a"
#         else:
#             new_str += string[i]
#     return new_str
#
#
# user = input("Enter: ")
# print(function(user))

#152
# def str_func(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                      for i in range(n))
#
#     index_v = string.find("v")
#     if index_v == -1:
#         return string
#
#     return string[:index_v + 1]
#
#
# number = int(input("Enter num: "))
# print(str_func(number))

#153
# def function(string):
#     new_str1 = ""
#     new_str2 = ""
#     new_str3 = ""
#     symbol = "r"
#     for i in string:
#         if i > symbol:
#             new_str1 += i
#         if i == symbol:
#             new_str2 += i
#         if i < symbol:
#             new_str3 += i
#
#     return new_str1 + new_str2 + new_str3
#
#
# user = input("Enter: ")
# print(function(user))

#154
# def str_func(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str: ")
#                      for i in range(n))
#     count = 0
#     for i in range(len(string)):
#         if string[i] == "c":
#             count += i
#     return round(count / string.count("c"), 2)
#
#
# num = int(input("Enter num: "))
# print(str_func(num))

#155
# def function(string):
#     for i in string:
#         if "c" in string and i > "c":
#             return string.count("c")
#         else:
#             return string.count("b")
#
#
# user = input("Enter: ")
# print(function(user))

#156
# def str_func(n, m):
#     string1 = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                       for i in range(n * 2))
#     print(end="\n")
#     string2 = "".join(input(f"Enter {i + 1} symbol for str 'm': ")
#                       for i in range(m))
#
#     central = len(string1) // 2
#     return string1[:central] + string2 + string1[central:]
#
#
# num1 = int(input("Enter n: "))
# num2 = int(input("Enter m: "))
# print(f"Res: {str_func(num1, num2)}")

#157
# def str_func(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                      for i in range(n * 2 + 1))
#
#     central = len(string) // 2
#
#     return string[:central - 1] + string[central + 2:]
#
#
# num = int(input("Enter n: "))
# while num <= 3:
#     num = int(input("Enter n: "))
# print(str_func(num))

#158
# def str_func(n):
#     summ = 0
#     multi = 1
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                      for i in range(n))
#
#     for i in range(len(string)):
#         if string[i] == "z":
#             summ += i
#             multi *= i
#     return f"Sum: {summ}   Multi: {multi}"
#
#
# num = int(input("Enter num: "))
# print(str_func(num))

#159
# def str_func(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                      for i in range(n))
#     new_str = "".join(string[i] for i in range(len(string)) if i % 3 != 0)
#
#     return new_str
#
#
# num = int(input("Enter num: "))
# print(str_func(num))

#160
# def str_palindrome(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")\
#                      for i in range(2 * n + 1))
#
#     if string == string[::-1]:
#         return f"String is palindrome. Quantity 'a': {string.count("a")}"
#
#     return f"String is not palindrome. Quantity 'b': {string.count("b")}"
#
#
# num = int(input("Enter num: "))
# print(str_palindrome(num))

#161
# def str_func(n):
#     string = "".join(input(f"Enter {i + 1} symbol for str 'n': ")
#                      for i in range(n))
#     new_str = string[1:-1]
#
#     return max(new_str)
#
#
# num = int(input("Enter num: "))
# print(str_func(num))

#162
# def phone_num(n, lines, True_number="295454"):
#     for line in lines:
#         name_surname = line[:-6].strip()
#         phone_number = line[-6:]
#         if phone_number == True_number:
#             return name_surname
#     return "Subscriber is not found!"
#
#
# length_str = int(input("Enter string length: "))
# count_str = int(input("Enter count str: "))
# peoples_list = []
#
# for i in range(count_str):
#     person_info = input(f"Enter info for person {i + 1} (name surname + phone): ")
#     peoples_list.append(person_info)
#
# print(phone_num(length_str, peoples_list))

#163
# def str_func(n):
#     string1 = "".join(input(f"Enter {i + 1} string for str 1: ")
#                       for i in range(n))
#     print(end="\n")
#     string2 = "".join(input(f"Enter {i + 1} string for str 2: ")
#                       for i in range(n))
#
#     return string1.replace("x", string2)
#
#
# num = int(input("Enter num: "))
# print(str_func(num))

#164
# def people_surname(n):
#     string = "".join(input(f"Enter {i + 1} string for str: ")
#                      for i in range(n))
#     if string.endswith("yan"):
#         return True
#     return False
#
#
# num = int(input("Enter num: "))
# print(people_surname(num))

#165
# def sentence(n):
#     string = "".join(input(f"Enter {i + 1} string for str: ")
#                      for i in range(n)).replace("a", "b")
#
#     return string
#
#
# num = int(input("Enter num: "))
# print(sentence(num))

#166
# def ab_remove(n):
#     string = "".join(input(f"Enter {i + 1} string: ") for i in range(n))
#     return string.replace("ab", "")
#
#
# user = int(input("Enter num: "))
# print(ab_remove(user))

#167
# print(ord("a"))

#168
# def func(len_str, num):
#     string = "".join(input(f"Enter {i + 1} symbol or letter: ") for i in range(len_str))
#     for i in string:
#         if ord(i) == num:
#             return f"Symbol cod: {ord(i)}   Symbol: {i}"
#     return f"In the string '{string}' the corresponding character was not found for the number '{num}'"
#
#
# length = int(input("Enter length: "))
# number = int(input("Enter num: "))
# print(func(length, number))

#169
# string = input("Enter: ")
# symbol = input("Enter sym: ")
# sym_find = string.find(symbol)
# right = string[sym_find + 1]
# left = string[sym_find - 1]
# print(left, right)

#170
# import string
#
#
# def alphabet_str(n):
#     alphabet = "".join([letter.upper() + letter.lower() for letter in string.ascii_letters])
#     if n > len(alphabet):
#         return None
#
#     return alphabet[1: n + 1: 2]
#
#
# num = int(input("Enter num: "))
# print(alphabet_str(num))

#171
# def alphabet(user, string="WwXxYyZz"):
#     if user > len(string):
#         return None
#
#     # reverse = string[::-1]
#     # return reverse[1: user + 1: 2]
#     return string[len(string) - 2: len(string) - 2 * user: -2]
#
#
# num = int(input("Enter num: "))
# print(alphabet(num))

#172
# def sym_x(x):
#     if x.isdigit():
#         return f"X is digit. Returned: {1}"
#     elif x.isupper():
#         return f"X is upper. Returned: {2}"
#     elif x.islower():
#         return f"X is lower. Returned: {3}"
#     else:
#         return f"X is other symbol. Returned: {4}"
#
#
# user = input("Enter x: ")
# print(sym_x(user))

#173
# def str_func(string):
#     return f"Start symbol code: {ord(string[0])}   End symbol code: {ord(string[-1])}"
#
#
# user = input("Enter str: ")
# print(str_func(user))

#174
# def str_x(n):
#     return "".join("x" * n)
#
#
# user = int(input("Enter num: "))
# print(str_x(user))

#175
# def even_number(n):
#     symbol1 = "X"
#     symbol2 = "Y"
#
#     return "".join(symbol1 + symbol2) * n
#
#
# num = int(input("Enter num: "))
# while True:
#     if num % 2 != 0:
#         num = int(input("Enter num: "))
#     print(even_number(num))
#     break

#176
# def join_str(string):
#     return " ".join(string)
#
#
# user = input("Enter str: ")
# print(join_str(user))

#177
# def str_func(n):
#     string = "abcdefg"
#     # new_str = ""
#     # for i in string:
#     #     new_str += i+n*','
#     return "".join(i+n*"," for i in string)
#
#
# num = int(input("Enter num: "))
# print(str_func(num))

#178
# def str_digit(string):
#     return len([string.count(i) for i in string if i.isdigit()])
#
#
# user = input("Enter str: ")
# print(str_digit(user))

#179
# def uppers(string):
#     count = 0
#     for i in string:
#         if i.isupper():
#             count += 1
#     return count
# s = "ffAAAjfhjf"
# c = collections.Counter("upper" if x.isupper() else "" for x in s )
# print(c)
# user = input("Enter: ")
# print(uppers(user))

#179/2
# def uppers(string):
#     return len([i for i in string if i.isupper()])
#
#
# user = input("Enter str: ")
# print(uppers(user))

#180
# string = "AbCdEfg"
# print(string.upper())

#181
# def lower_upper(string):
#     return "".join(i.upper() if i.islower() else i.lower() for i in string)
#
#
# user = input("Enter str: ")
# print(lower_upper(user))

#181/2
# def lower_upper(string):
#     return string.swapcase()
#
#
# user = input("Enter str: ")
# print(lower_upper(user))

#182
# def str_func(string):
#     if string.isdigit():
#         return f"String is digit. Returned: 1"
#     try:
#         float(string)
#         return f"String is float. Returned: 2"
#     except ValueError:
#         return f"String is not digit. Returned: 1"
#
#
# user = input("Enter str: ")
# print(str_func(user))

#183
# def digit(number):
#     string = str(number)
#     return string[::-1]
#
#
# user = int(input("Enter str: "))
# print(digit(user))

#184
# def sum_num(string):
#     num_list = [int(i) for i in string if i.isdigit()]
#     return sum(num_list)
#
#
# user = input("Enter nums: ")
# print(sum_num(user))

#185
# def eval_str(string):
#     return eval(string)
#
#
# user = input("Enter math str: ")
# print(eval_str(user))

#186
# def str_func(str1, str2):
#     return str1.replace("x", str2)
#
#
# user1 = input("Enter str1: ")
# user2 = input("Enter str2: ")
# print(str_func(user1, user2))

#187
# def two_strings(str1, str2):
#     return str1.count(str2)
#
#
# user1 = input("Enter str 1: ")
# user2 = input("Enter str 2: ")
# print(two_strings(user1, user2))

#188
# def two_strings(str1, str2):
#     return str1.rfind(str2)
#
#
# user1 = input("Enter str 1: ")
# user2 = input("Enter str 2: ")
# print(two_strings(user1, user2))

#189
# def str_func(string="A bc D ef G"):
#
#     first_idx = string.find(" ")
#     second_idx = string.find(" ", first_idx + 1)
#
#     if second_idx != -1:
#         return string[first_idx + 1:second_idx]
#
#     return second_idx[first_idx + 1:]
#
#
# print(str_func())

#190
# def str_func(string="A bc D ef G"):
#     first_idx = string.find(" ")
#     last_idx = string.rfind(" ")
#
#     return string[first_idx + 1:last_idx]
#
#
# print(str_func())

#191
# def word_count(string):
#     return len(string.split(" "))
#
#
# user = input("Enter words: ")
# print(word_count(user))

#192
# def name_func(string, letter):
#
#     for name in string:
#         if name.istitle() and name.startswith(letter):
#             return string.count(name)
#     return None
#
#
# user = input("Enter names: ")
# let = input("Enter upper letter: ")
# print(name_func(user, let))

#192/2
# def name_func(string):
#     names = string.split()
#
#     count_dict = {}
#
#     for name in names:
#         first_letter = name[0].upper()
#         if first_letter in count_dict:
#             count_dict[first_letter] += 1
#         else:
#             count_dict[first_letter] = 1
#
#     for letter, count in count_dict.items():
#         if count > 1:
#             return f"Name upper letter: {letter}   Count names: {count}"
#     return f"First letters all unique. Returned: {string}"
#
#
# user_input = input("Enter names: ")
# print(name_func(user_input))

#193
# def str_func(string):
#     word_list = string.split()
#
#     count_dict = {}
#
#     for word in word_list:
#
#         count_b = word.count("B")
#
#         if count_b >= 1:
#             if "B" in count_dict:
#                 count_dict["B"] += 1
#             else:
#                 count_dict["B"] = 1
#
#     for letter, count in count_dict.items():
#         if count > 1:
#             return f"{letter}: {count}"
#
#
# user = input("Enter: ")
# print(str_func(user))

#194
# def str_func(string):
#     word_list = string.split()
#
#     count_dict = {}
#
#     for word in word_list:
#         count_b = word.count("B")
#
#         if count_b == 2:
#             if "B" in count_dict:
#                 count_dict["B"] += 1
#             else:
#                 count_dict["B"] = 1
#
#         for letter, count in count_dict.items():
#             if count > 1:
#                 return f"Word with {letter}: {count}"
#
#
# user = input("Enter: ")
# print(str_func(user))

#195
# def length_min_word(string):
#     word_list = string.split()
#     return min(word_list, key=len)
#
#
# user = input("Enter string: ")
# print(length_min_word(user))

#196
# def length_max_word(string):
#     word_list = string.split()
#     return max(word_list, key=len)
#
#
# user = input("Enter string: ")
# print(length_max_word(user))

#197
# def title_func(string):
#     return string.title()
#
#
# user = input("Enter string: ").lower()
# print(title_func(user))

#198
# def str_func(string):
#     word_l = string.split()
#     return min(word_l, key=len)
#
#
# user = input("Enter words: ").lower()
# print(str_func(user))

#199
# def space_func(string):
#     word_l = string.split()
#     return " ".join(word_l)
#
#
# user = input("Enter string with space: ")
# print(space_func(user))

#21
# def is_upper(string):
#     uppers = ""
#     for i in string[0:4]:
#         if i.isupper():
#             uppers += i
#
#     if len(uppers) >= 2:
#         return string.upper()
#     return string
#
#
# user = input("Enter str: ")
# print(is_upper(user))

#22
# def str_func(string):
#     word_l = string.split()
#     return " ".join(sorted(word_l))
#
#
# user = input("Enter string: ")
# print(str_func(user))

#23
# def str_func(string):
#     return string.replace("\n", " ")
#
#
# user = "She\nis\nbeautiful"
# print(str_func(user))

#24
# def str_func(string, sym):
#     if string.startswith(sym):
#         return True
#     return False
#
#
# str_user = input("Enter str: ")
# symbol = input("Enter symbol: ")
# print(str_func(str_user, symbol))

#25
# import string
#
#
# def caesar(str_user, shift):
#     alphabet = string.ascii_lowercase
#     shifted = []
#
#     for i in str_user:
#         if i in alphabet:
#             new_i = (alphabet.index(i) - shift) % len(alphabet)
#             shifted.append(alphabet[new_i])
#         else:
#             shifted.append(i)
#     return "".join(shifted)
#
#
# user = input("Enter string: ")
# shift_u = int(input("Enter shift: "))
# print(caesar(user, shift_u))

#26
# def text(name, age):
#     return "Name: {} Age: {}".format(name, age)
#
#
# n = input("Enter name: ")
# a = input("Enter age: ")
# print(text(n, a))

#27
# def deleted_space(string):
#     return string.replace(" ", "")
#
#
# user = input("Enter string: ")
# print(deleted_space(user))

#28
# def prefix(string, prf):
#     lines = string.splitlines()
#     pref_lines = [prf + line for line in lines]
#     return "\n".join(pref_lines)
#
#
# user_l = []
#
# while True:
#     user = input("Enter strings: ")
#     if user == "":
#         break
#     user_l.append(user)
#
# text = "\n".join(user_l)
#
# pref = input("Enter prefix: ")
# res = prefix(text, pref)
# print("\nResult")
# print(res)

#29
# def str_func(num):
#     string = "\n".join(input("Enter string: ") for _ in range(num))
#     for i in string[0]:
#         return " " + i + string[1:]
#
#
# user = int(input("Enter num: "))
# print(str_func(user))

#30
# def is_float(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False
#
#
# def str_func(string):
#     new_str = ""
#     lst = string.split()
#
#     for num in lst:
#         if is_float(num) and float(num) % 1 != 0:
#             new_str += f"{float(num):.2f} "
#
#     return new_str
#
#
# user = input("Enter string: ")
# print(str_func(user))

#31
# def is_float(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False
#
#
# def str_func(string):
#     new_str = ""
#     lst = string.split()
#     for i in lst:
#         if i.startswith("-") or i.startswith("+"):
#             if is_float(i) and float(i) % 1 != 0:
#                 new_str += f"{float(i):.2f} "
#
#     return new_str
#
#
# user = input("Enter str: ")
# print(str_func(user))

#32
# def int_str(string):
#     new_str = ""
#     lst = string.split()
#
#     for i in lst:
#         if i.isalnum():
#             new_str += f"{int(i)} "
#     return new_str
#
#
# user = input("Enter str: ")
# print(int_str(user))

#33
# def zero_num(string):
#     new_str = ""
#
#     for i in string:
#         if i.isdigit():
#             new_str += i
#     return new_str.zfill(5)
#
#
# user = input("Enter str: ")
# print(zero_num(user))

#34
# def str_func(string, num):
#     new_str = ""
#
#     for i in string:
#         if i.isdigit():
#             new_str += i.ljust(num, "*") + " "
#     return new_str
#
#
# user = input("Enter string: ")
# number = int(input("Enter num: "))
# print(str_func(user, number))

#35
# def format_num(num):
#     return f"{num:,}".replace(".",  ",")
#
#
# number = float(input("Enter num: "))
# print(format_num(number))

#35/2
# def format_num(num):

#36
# def percent_format(number):
#     return "{:.2%}".format(number)
#
#
# user = float(input("Enter num: "))
# print(percent_format(user))

#37
# def numbers(num):
#     left_num = "{:<10}".format(num)
#     right_num = "{:>10}".format(num)
#     center = "{:^10}".format(num)
#     return "Left: {}\nRight: {}\nCenter: {}".format(left_num, right_num, center)
#
#
# user = input("Enter num: ")
# print(numbers(user))

#38
# def str_fun(string, substring):
#     return string.count(substring)
#
#
# user_str = input("Enter string: ")
# user_sub = input("Enter substring: ")
# print(str_fun(user_str, user_sub))

#39
# def str_func(string):
#     return string[::-1]
#
#
# user = input("Enter str: ")
# print(str_func(user))

#40
# def str_func(string):
#     w_l = string.split()
#     reverse_w = w_l[::-1]
#     return " ".join(reverse_w)
#
#
# user = input("Enter str: ")
# print(str_func(user))


# def number_func(num):
#     try:
#         if len(num) != 3 or not num.isdigit():
#             raise ValueError("The length of the numbers must be 3!")
#
#     except ValueError as e:
#         print(f"Error {type(e)}. Please enter only {type(int)} nums!")
#     digits = [int(digit) for digit in num]
#     if digits[0] == digits[1] + digits[2]:
#         return True
#     else:
#         return False
#
#
# user = input("Enter num: ")
# print(number_func(user))

