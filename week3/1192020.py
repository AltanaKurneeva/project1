# split - the opposite of ''. join() function,split will return you the list
# msg = 'Hello everyone, we are doing some exercises on python!'
# words = msg.split(',')
# print(words)
# # print(words[-1])  # when splitted by space


# msg = 'price is $100'
# # print the new price if 20% discount is applied
# price = msg.split('$')[1]
# int_price = float(price)
# dis_price = int_price * 0.8
# print(f"discounted price is {dis_price}")

# PRINT THE CAPITALS OF THE COUNTRY
# create repository for 10 countries with their capital cities
# when user enters the country print the capital city
# return >> "Capital city of UK is London"
# countries = {'AFGHANISTAN' : 'KABUL', 'ALBANIA':'TIRANA', 'ALGERIA':'ALGIERS', 'ANDORRA':'ANDORRA LA VELLA', 'ANGOLA':'LUANDA'}
# msg = input('enter the country name: ')

# # if msg.upper() in countries.keys:
# for key in countries.keys():
#     if msg.lower() == key.lower():
#         print(f"Capital city of {key.title()} is {countries[key].title()}.")
#     else:
#         print(f"{msg} doesn't exist in our database.")

# while loops
# stopSignal = True
# while stopSignal:
#     msg = input('I am Tom, tell me the word i will repeat it loudly: ')
#     print(msg.upper())
#     if msg.lower() == 'quit':
#       stopSignal = False

# BREAK, CONTINUE

# while True:
#     msg = input('I am Tom, tell me the word i will repeat it loudly: ')
#     print(msg.upper())

#     if msg.lower() == 'quit':
#       break

# find given number from the list and print the message if exists
# nums = [12, 34, 5, 9, 0, 1, 23]
# key_num = int(input('enter the number'))
# for num in nums:
#     if key_num == num:
#         print(f"{key_num} is found, stopping the search ...")
#         break    # will stop the search
#     else:
#         print(f"{key_num} was not found, searching ...")

student1 = {'name':'John', 'age':26, 'classes':'python'}
print(student1.pop('classes'))
print(student1)