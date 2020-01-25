# # DICTIONARIES -  DATA STRUCTURE
# # creat, modify, add an element, delete an element, loop through the elements
# student1 = {}
# student1 = {'name':'John', 'age':25, 'location':'Brooklyn'}
# student2 = {'name':'Mark', 'age':27, 'location':'Queens'}  # name - key, John - value
# # print(student1)   # prints the whole dictionary
# # print(student1['name'])  # pass the key inside the square brackets to see the value of the key
# # print(student1['name'],",", student2['name'])

# # print(f"Student 1 info: Name: {student1['name']}, Age: {student1['age']}, Loc : {student1['location']}")
# # print(f"Student 2 info: Name: {student2['name']}, Age: {student2['age']}, Loc : {student2['location']}")

# # print(student1.get('name'))    # GEt - accessing to dictionary, besides [] square brackets

# # # Adding key, value to the existing dictionary
# # student1['grade']='A'    # dictionaryName[key] = value
# # print(student1)

# # # modify the value in the dictionary, set a new value with existing key
# # student1['grade'] = 'B'
# # print(student1)

# # del student1['grade']  # will delete key 'grade'
# # print(student1)

# print(type(student1))

# # looping through he dictionary keys
# for key in student1:
#     print(key)
# # SAME
# for key in student1.keys():
#     print(key)     # prints the key in each loop
#     print(student1[key])     # prints the value in each loop


# # looping through the values. Will show only values
# for value in student1.values():
#     print(value)

# for key, value in student1.items():
#     # dict.items() creates 2 lists, first list is list of keys, second list is list of values.
#     print(f"I have {key} with value = {value}")

# # create the list of students from existing objects (student1, student2)
# student3 = {'name':'Nodir', 'age':18, 'location':'Hawaii', 'grade':'A'}
# students = [student1, student2, student3]
# count = 1

# for student in students:
#     print(student['name'], student['location'], student['age'], student.get('grade'))
#     count +=1

# print(students[2]['name'])

# student1['classes'] = ['QA', 'Finance', 'BA', 'Soccer']
# student2['classes'] = ['QA', 'Finance', 'Chess']
# student3['classes'] = ['QA', 'Finance', 'Automation', 'Sleeping']
# print(student1['classes'][0])
# print(student2['classes'][2])

# # get the input from the user
# # return how many time each letter was used
# # hellooo >> h=1, e=1, l=2, o=3

# msg = input('enter your input :')
# letters_count = {}
# for letter in msg:
#     if letter not in letters_count:
#         letters_count[letter] = 1
#     else:
#         letters_count[letter] +=1

# print(letters_count)
# for key, value in letters_count.items():
#     print(f'Letter {key} was used {value} time(s) in the input')

# count the vowels in each input
# vowels =[aouie]
# msg = input('enter the word: ')
# vowels = 'auieo'
# c_vowels = {}

# for letter in msg:
#   if letter in vowels:
#     if letter not in c_vowels:
#       c_vowels[letter] = 1
#     else:
#       c_vowels[letter] +=1

# print(c_vowels)

# SAME >>

msg = input('enter the word: ')
vowels = 'auieo'
c_vowels = {}

for letter in msg:
  if letter in vowels:
    if letter not in c_vowels:
      c_vowels.setdefault(letter, 0)
      c_vowels[letter] +=1

print(c_vowels)

1/19/2020
# sorting the lists
nums = [23, 6, 890, 1, 0, -3, -9]
print(nums)
# permanently sort
nums.sort()
print(nums)
nums.append(45)
print(nums)
nums.sort()
print(nums)

words = ['hello', 'world', 'of', 'engineers', '!']
words.sort()
print(words)

# sorting the list temporarily
words = ['hello', 'world', 'of', 'engineers', '!']
sorted_words = sorted(words)  # ascending order
rev_sorted_words = sorted(words, reverse=True)      #descending order

print(sorted_words, 'sorted list')
print(rev_sorted_words, 'reverse sorted list')
print(words, 'original list')


nums = [23, 6, 890, 1, 0, -3, -9]
nums.reverse()
print(nums)

# print reverse of the string
word = list('hello')
word.reverse()
print(word)
print(''.join(word))
print(*word)



