#!/usr/bin/env python3

# function print_fibo(n):
    # create an empty list called fib_sequence
    # if n is 0, return empty 
    # if n is 1, return [0]
    # if n is 2, return [0,1]

    # list starts with [0,1]
    # loop from 2 up to n:
        # next_num = last num + second last num
        # add next_num to list
    # print list
def print_fibonacci(length):
    fibonacci_seq = []

    if length <= 0:
        print(fibonacci_seq)
        return
    elif length == 1:
        fibonacci_seq = [0]
    elif length == 2:
        fibonacci_seq = [0,1]
    else:
        fibonacci_seq = [0,1]
        for i in range(2, length):
            next_num = fibonacci_seq[i-1] + fibonacci_seq[i-2]
            fibonacci_seq.append(next_num)
    print(fibonacci_seq)

    

# my_list = [3,6,4,2,1,5]
# my_list.sort()
# print(my_list)

# my_list = ['Cabbage', 'Apple', 'Banana', 'Potato']
# my_list.sort()
# print(my_list)

# my_list = ['This is a long sentence', 'Word', 'z']
# my_list.sort(key=len)
# print(my_list)

# my_list = ['This is a long sentence', 'Word', 'z']
# my_list.sort(key=len, reverse=True)
# print(my_list)

# my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

# def sort_tuple(tuple_value):
#     return tuple_value[1]

# sorted_tuple = sorted(my_list)
# sorted_tuple.sort(key=sort_tuple)
# print(my_list)
# print(sorted_tuple)

# my_list = [0, 1, 2, 3]
# my_list.insert(3, 20)
# print(my_list)