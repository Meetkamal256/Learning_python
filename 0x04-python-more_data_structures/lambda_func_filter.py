def mul_by_2(num):
    return num * 2


times_two = mul_by_2
print("4 * 2 =", times_two(4))


def do_math(func, num):
    return func(num)


print("9 * 2 =", do_math(mul_by_2, 9))


# --------PROBLEM----------
# create a function that receives a list and a function
# the function passed will return true or false if a list
# value is odd
# the surrounding function will return a list of odd numbers


def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def change_list(list, func):
    odd_list = []
    for i in list:
        if func(i):
            odd_list.append(i)

    return odd_list


aList = range(1, 20)
print(change_list(aList, is_it_odd))

Sum = lambda x, y: x + y
print("sum:", Sum(4, 5))

can_vote = lambda age: True if age >= 18 else False
print("can vote:", can_vote(90))

oneTo10 = range(1, 11)


def dbl_num(num):
    return num * 2


print(list(map(dbl_num, oneTo10)))
print(list(map((lambda x: x * 3), oneTo10)))
aList = list(map((lambda x, y: x + y), [1, 2, 3, 4], [1, 2, 3, 4]))
print(aList)
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
print(list)

print(list(filter((lambda x: x % 9 == 0), range(1, 1000))))
print(list)

# -------------PROBLEM-----------------
# Find the multiples of 9 from a random 100 value list
# with values between 1 and 1000


import random

# generate a random list with randint btw 1 and 1000
# use range to generate 100 values
rand_list = list(random.randint(1, 1000) for i in range(1, 100))
# use modulus to find multiples of 9
print(list(filter((lambda x: x % 9 == 0), rand_list)))

from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 6)))


