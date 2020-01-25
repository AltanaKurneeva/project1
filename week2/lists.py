# # What are this lists?
# # DATA STRUCTURES - LIST, DICTIONARIES, SETS, TUPLES
# countries = [] # empty list
# city = 'brooklyn'
# cities = ['brooklyn', 'manhattan', 'queens', 'bronx', 'staten island'] 
# odd_numbers = [1,3,5,7,9,11]

# # accessing elements in a list
# print(cities)

# # indexing starts with 0 not 1
# print(cities[3])
# print(cities[0])
# print(f"the best city in NYC is {cities[0].title()}.")
# print(f"the biggest city in NYC is {cities[2].title()}.")
# print(f"the biggest populated city in NYC is {cities[1].title()}.")
# print(f"the last element in the list is {cities[4]}.")
# print(f"the first from the last element in the list is {cities[-1]}.")

# print(f"the second from the last element in the list is {cities[-2]}.")

# exercise 3-1
names = ['ahmed', 'alexa', 'dilshod']
# # print(names[0].upper() , names[1].upper() )
# # print(names[1].upper() )
# # print(names[2].upper() )

# # changing adding and removing elements
# # modifying elements in a list
# print(names)
# names[0] = 'dina' # replacing the old value with new one
# print(names)

# # adding elements to a list
# # to the end of the list - append()
# names.append('aida')
# print(names)

# # inserting elements into a list - insert(index, newvalue)
# names.insert(2, 'artem') # insert a new value and expand the list, not loosing any value here
# print(names)
# indexOfaida = names.index('aida')
# print(f"indexOfaida is {indexOfaida}")

# # removing elements from a list
# # removing an item using the del statement
# del names[1]
# print(names)

# # removing an item Using the pop() method
# removed_names = []
# popped_name = names.pop()
# print(popped_name)
# print(names)
# # poping items from any position in a list
# print("last element from the names will be removed...")
# removed_names.append(names.pop(1))
# print(names)
# print(removed_names)

#removing an item by value
# names.remove('artem')
# print(names)

# exercise 3-4
print("$$$$$$$$$$$$ exercise 3-4 $$$$$$$$$$$$$$$$$$$$$$")
guests = ['bruce lee', 'jackie chan', 'khabib nur', 'obama']

print(f"Heeeey, {guests[0].title()} welcome to my house!")
print(f"Heeeey, {guests[1].title()} welcome to my house!")
print(f"Heeeey, {guests[2].title()} welcome to my house!")
print(f"Heeeey, {guests[3].title()} welcome to my house!")
guest_not_coming = ['khabib nur', 'obama']
guests.remove(guest_not_coming[0])
guests.remove(guest_not_coming[1])
print()
print(guests)
print(f"Heeeey, {guests[0].title()} welcome to my house!")
print(f"Heeeey, {guests[1].title()} welcome to my house!")
# print(f"Heeeey, {guests[2].title()} welcome to my house!")
# print(f"Heeeey, {guests[3].title()} welcome to my house!")

# HOMEWORK 3-6, 3-7
numberOfGuests = len(guests) # returns number of elements you have in guests
print(f"I have {numberOfGuests} people coming to a dinner today.")