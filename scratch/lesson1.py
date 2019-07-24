##Data Structures


def hello_world(name):
    print(name)


# hello_world("ravi")

names = ['ravi', 'sabin', 'ishwar']

#
# names.sort()
#
# print(names)
#
# names.reverse()
#
# print(names)

names.append('shyam')


for index, name in enumerate(names):
    print(index)

nums = [1, '2', '2', 'six']

# print(nums)

for number in range(1, 10):

    if number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    elif number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")

    else:
        print("fizz buzz")










