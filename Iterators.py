#represents a stream of data
#strings and lists are iterable

string =  "123456789"
for char in string:
    print(char)

#using the iter fnction to iterate and then call next on subsequent ones
my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


ebzString =  "abcdefgh"
my_iter = iter(ebzString)


for i in range(0,len(ebzString)):
    next_item = next(my_iter)
    print(next_item)