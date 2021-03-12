# implement a string Brian Faure YT tutorial

f = open("alice_in_wonderland.txt", "r")
text = f.read()

# length function
print(len(text))

# individual characters
print(text[0])
print(text[100])
print(text[-1])

# useful for parsing or cleaning up plain txt: split function
# default is the space character
every_word = text.split() # list
for e in every_word:
    print(e)

every_sentence = text.split(".")
for s in every_sentence:
    print(s)

# lower function to replace upper with lower
lowercase = text.lower()
print(lowercase)

# and with upper
uppercase = text.upper()
print(uppercase)

# capitalize function is similar to upper, but copy where only the first char is capitalize - title case
# capitalize returns copy of string with just first word of whole string capitalized
# title returns copy of string with first char of every word capitalized
words = text.split()
for w in words:
    upper = w.capitalize()
    print(upper)

# find is useful for parsing - find the index of
# first index instance
print(text.find("Alice"))

# count function gives integer of how many times that string is found
print(text.count("Alice"))

# replace returns copy of the string with each instance of first argument replaced w/ 2nd argument
print(text.replace("Alice", "Kate"))

