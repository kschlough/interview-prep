# implement list Brian Faure YT tutorial

array = [1, 2, 3]

# iterate over the elements in the list
for a in array:
    print(a)

# if you don't want any value stored when iterating, like just # of times or length:
count = 0
for _ in array:
    count += 1
print(count)

# another way to iterate is using indices
for i in range(len(array)):
    print(array[i])

# two lists, iterate through them taking the item of each at the same index
# they don't have to be the same length
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

for i, x in zip(a, b): # zip ties them together so they can be iterated as one entity
    print(i, x)
    # or, string formatting:
    print("%d,%d"%(i,x)) # d is int

# delete an element
del(array[1])
print(array)

# indices go from 0 to the len of the list minus 1

# implement a pseudostack or pseudoqueue (just accessing last or 1st element)
# use built-in pop function
a.pop() # pops and prints out the last element, changes the string

# search a list for an element using .index function
# also can use 'if x in a' language
print(a.index(1))

# if you don't know if the element's in the list, use try/catch so you don't catch the function
try: 
    print(a.index(5))
except:
    print("element not in list")

# sort basic integer list - from lowest to highest
x = [44, 55, 7, 2, 3]
x.sort()
print(x)

# list comprehension - cool way to create lists that mirrors writing mathematical document
def f(x):
    return x**2

a = [f(x) for x in range(10)] # all the ints from 0-9 squared
print(a)

#specific list of inputs
b = [1, 7, 4, 3, 9]
a = [f(x) for x in b] # iterates over all elements in b
print(a)

# reverse the indices of every element
a.reverse()
print(a)

# count - print # of instances it finds of the item
y = [4, 4, 4, 2]
print(y.count(4))

# can add any data structure to a list in python
class example:
    def __init__(self):
        self.value = 10

a = []
# create 10 of the example data structures & put in list
for _ in range(10): # i isn't stored
    new_example = example()
    a.append(new_example)

print(a) # prints memory address of where each example is stored