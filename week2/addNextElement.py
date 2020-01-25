numbers = [25,12,20,30]
new_nums = []
# pseudocode
# looping through the list, accessing to elements in each loop
# add two elements and append to new list
size = len(numbers)
# indexing you can do with i, j, k
for i in range(size-1):
    sum = numbers[i] + numbers[i+1]
    new_nums.append(sum)
print(new_nums)
# ?????????
# SAME >>
for i in range(len(numbers)-1):
    new_nums.append(numbers[i] + numbers[i+1])
print(new_nums)