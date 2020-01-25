# # variables and data types
# # string - text, date (libraries to handle dates)
# # numbers - integeres (-50, -1, 0, 1), floats (10.25), doubles ()
# # boolean - 0/1, True/False

# # variable - storage dor data, declare, assign a value
# # variable names - 1. dont start with numbers, start with lower case letter, dont use spaces
#        # a. test_name      b.testName - CAMEL CASE STYLE
#        # HAVE A MEANINGFUL VARIABLE NAME
       
# # integeres
# a = 10
# b = 20
# print(a+b)
# a = 456
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# #strings
# car = 'audi'
# model = 'q7'
# owner = 'aslan'
# print(car, model)
# print(f"{'*'*15} \n\t{owner} is a owner of {car} {model} {'*'*10}")
# #fstring helps to cat
# a = 45
# b = 85
# print(car.upper(), model) # AUDI
# print(car.title(), model) #audi

# car = '     BMW      '
# print(f"I have a {car.strip() }.")

# years = 10
# # converting int, double, float to a string >> str(ing)
# print(owner.title() + " owns " + car +' '+model+' '+ str(years)+ ' years' )
# print(f"{owner.title()} owns {car.strip()} {model} {years} years")

# # # integers and strings
# # a = '45' # this is regulat text not number
# # b = '65'
# a = input("enter your first number: ")
# b = input("enter your second number: ")
# print(a+b)
# print(int(a) + int(b)) # 'int' converts text to number

# # string >> functions: upper(), lower(), title(), 
# # rstrip(), lstrip(), strip() - to remove whitespace (spaces, tabs, enters.. all non printable characters)
# # using fstring
# # convert string to int :(string)
# # convert int to string : str(int)
# # input(message): message is prompt and function to accept the string from user

# print('hello'.upper())
# msg = 'hello'
# print(msg.upper())
# print('\t\t\thello\n'.upper().strip() )

# operators with numbers: +, -, /, %
number1 = 10
number2 = 3
print(number1*number2)
print(number1/number2)
print(number1-number2)
print(number1+number2)
print(number1%number2) # it returns the remainder - modulo
print(number1 // number2) # how many number2s in number1 - division floor