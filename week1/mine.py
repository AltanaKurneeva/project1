# a = 21
# b = 34
# print(b)
# print(a-b)

# print("hello 1")
# print("hello 2")
# print("Hello world")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

name = "Altana"
age = 31

# print("Hello everybody my name is " + name + ", ")
# print("I am " + str(age) + " years old. ")

# print("Giraffe\nAcademy")
# print("Giraffe\"Academy\"")

# phrase = "Giraffe Academy"
# print(phrase +" is cool")
# print(phrase.upper())
# print(phrase.replace ("Giraffe", "Elephant"))
# print(len(phrase))

# weekday = ['monday', 'tuesday', 'wednesday', 'thursday']
# print(weekday[0].title())
# print(f"I work every {weekday[0].title()}.")
# print(f"I have day off only on {weekday[2]} and on {weekday[3]}, so we can go out those days.")
# print('\t\t\thello')

# weekday.append('friday')
# print(weekday)
# weekday.insert(0, 'sunday')
# print(weekday)
# weekday.insert(5, 'saturday')
# print(weekday)

# weekday.pop()
# print(weekday)

# weekday[0] = 'sunday'
# print(weekday)

# del weekday[0]
# print(weekday)

# weekday.remove('tuesday')
# print(weekday)

# b = ['banana', 'apple', 'microsoft']
# b[0], b[1] = b[1], b[0]
# print(b)
# print(f"Hello everybody, I like {b[0]}")
# print("hello my name is " + name + ", ")
# print("I am " + str(age) + ". ")

# b.append('strawberry')
# # print(b)
# b.insert(0, 'strawberry')
# print(b)
# b.pop()
# print(b)
# b[0] = 'orange'
# print(b)
# del b[0]
# print(b)
# b.remove('banana')
# print(b)

# firstName = 'Altana'
# lastName = 'Kurneeva'
# fullName = firstName + " " + lastName
# print(fullName)
# firstName.rstrip()
# print(firstName)

# message = "One of Python's strenghts is its diverse community"
# print(message)

# print(firstName.title())
# quote = "A person who never made a mistake never tried anything new"
# print(f"Albert Einstein once said, {quote}. ")

# famous_person = "Albert Einstein"
# message = famous_person + " said, " + quote
# print(message)

fruits = ['banana', 'mango', 'apple']
# favourite_fruit = fruits.pop()
# print(f"My favourite fruite is {favourite_fruit}")

# fruits.sort()
# print(fruits)
# print()
# fruits.reverse()
# # print(fruits)
# for fruit in fruits:
#     print(fruits)

# for fruit in fruits:
#     print(fruit.title() + " is a delicious fruit!")
#     print("I need to go and buy " + fruit.title() + ".\n")
# print("I love fruits!")

# for value in range(1,6):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,20,3))
# print(even_numbers)

# squares = []
# for value in range(1,5):
#     square = value**2
#     squares.append(square)
# print(squares)

# numbers = list(range(1,5))
# print(min(numbers))

# squares = [value**2 for value in range(1,5)]
# print(squares)

# squares = []
# for value in range(1,10):
#     square = value*2
# print(square)

# nums_by_five =[]
# for num in range(0, 100, 5):
#     nums_by_five.append(num)
#  print(nums_by_five)

# for num in range(21):
#     print(num)
# print()

# for value in range(1,1000001):
#     print(value)

# for value in range(1,21):
#     print(value)

# numbers = list(range(1,1000001))
# print(min(numbers))

# for value in range(3, 31, 3):
#     print(value)

# cube = []
# for value in range(1,10):
#     cube = value**3
#  print(cube)

# cube = [value**3 for value in range(1,11)]
# print(cube)

fruits = ['banana', 'apple', 'mango', 'peach', 'plum']
# print(fruits[2:])

# print("Here are the most delicious fruits")
# for fruit in fruits[:3]:
#     print(fruit.title())

# friend_fruits = my_fruits[:]
# print("My favourite fruits are:")
# print(my_fruits)

# print("\nMy friend's favourite fruits are:")
# print(friend_fruits)

# Umai_fruit = my_fruits[:2]
# print("Umai favourite fruits are:")
# print(Umai_fruit)

# Umai_fruit.append('orange')
# print(Umai_fruit)


# print("The fruits from the middle of the list are:")
# print(fruits[2:4])

# pizzas = ['margarita', 'peperoni', 'mushroome']
# freind_pizza = my_pizza[:]
# my_pizza.append('supreme')
# print(my_pizza)
# freind_pizza.append('spinach')
# print(freind_pizza)

# print("My favourite pizzas are:")
# print(my_pizza)
# print("\nMy freind's favourite pizzas are:")
# print(freind_pizza)

# for pizza in pizzas:
#     print(f"My favourite pizza is {pizza}.")
# print("I really love pizza!")

# dimensions = (200, 500)
# print(dimensions[0])

# dimensions[0] = 150
# print = dimensions # not executing

# for dimension in dimensions:
#     print(dimensions)



# 1/18/2020 recap lists, tuples, if conditions
nums = [4, 8, 3, 44, 1, 89, 7, 54.55]
# find how many even numbers in the list
# print this message : "the list contains {count} even numbers"
# count = 0
# for num in nums:
#     if num % 2 == 0:
#            count = count + 1
#         count += 1         # decrement will be >> count -= 1
# print(f"The list contains {count} even numbers")

# # find odd numbers
# count = 0
# for num in nums:
#     if num % 2 == 1:
#         # count = count + 1
#         count += 1         # decrement will be >> count -= 1
# print(f"The list contains {count} odd numbers")

# find odd and even numbers at the same time
# countOdds = 0
# countEvens = 0
# for num in nums:
#     if num % 2 == 1:
#         # count = count + 1
#         countOdds += 1         # decrement will be >> count -= 1
#     elif num % 2 == 0:
#         countEvens += 1
# print(f"The list contains {countEvens} even numbers and {countOdds} odd numbers")

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#          print(car.upper())
#     else:
#          print(car.title())

age = 19
if age >= 18:
     print("You are old enough to vote!")