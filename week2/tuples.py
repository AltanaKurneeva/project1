# # Tuples 69 - ARE IMMUTABLE DATA STRUCTURES (CANNOT CHANGE SIZE, REPLACE VALUE. ONCE YOU CREATE YOU CANNOT CHANGE)

# # Defining a Tuple 69
# dimensions_rectangle = (100, 150)
# print(dimensions_rectangle)
# # dimensions_rectangle[0] = 110 # cant do this because tuples are immutable

# # Writing over a Tuple 71
# dimensions_rectangle = (110, 250)
# print(dimensions_rectangle)

# print(dimensions_rectangle.index(110))
# print(dimensions_rectangle.index(250))

# # Looping Through All Values in a Tuple 70
# for dimension in dimensions_rectangle:
#     print(f"Dimension of rectangle is : {dimension}")

# # find the size of tuple with len()
# print(len(dimensions_rectangle))

# Exercise 4-13: Buffet 71
foods = ('gyro', 'shish kebab', 'humus', 'turkish tea', 'baklava')
for food in foods:
    print(f"we have {food}.")
# foods[4] = 'doner' # we verified that it cant be done
print("OUR MENU HAVE CHANGED")
foods = ('gyro', 'lamb kebab', 'humus', 'turkish tea', 'doner')
for food in foods:
    print(f"we have {food}.")

cars = ['audi', 'bmw', 'tesla', 'volvo', 'mercedes']
# '==' COMPARISON of right and left values
for car in cars:
    if car == 'tesla' :  #comparing the value of each loop with string 'tesla'
        print(f'{car} is electric car! dont go to gas station.')
    else:
        print(f'{car} is gas car, go to the gas station.')
print('execution completed!!') # ouside the for loop, to be run once only