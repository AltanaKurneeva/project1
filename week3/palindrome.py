# 1. find the palindrome
# get the input from the user (one only)
# return to the user is this word polindrome or not

# word = input('enter your word: ')
# # word = 'hello'

# lword = list(word)
# lword.reverse()

# # print(word)
# # print(lword)

# if ''.join(lword) == word:
#     print(f"{word} is palindrome." )
# else:
#     print(f"{word} is not palindrome, don't you see!")


# word = input('enter your word: ')
word = 'hello'

# lword = list(word)
rev_word = word[::-1]  # copying the original list elements in reverse order, -1 means step backwords

print(word)
print(rev_word)

# if ''.join(lword) == word:
#     print(f"{word} is palindrome." )
# else:
#     print(f"{word} is not palindrome, don't you see!")