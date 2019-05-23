farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(['lion', 'tiger', 'panther', 'elephant', 'hare'])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

empty_set = set()
empty_set_2 = {}
empty_set.add("a")
even = set(range(0,40,2))
print(even)
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(squares)

#sets are unordered

#union been a function of sets
even = set(range(0,40,2))
print(even)
print(len(even))

squares_tuple = (4,6,9,16,25)
squares= set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))

print("-" *40)

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

#you can call sorted function on results
print(sorted(even))
print('symmetric even minus squares')
print(sorted(even.symmetric_difference(squares)))

print('symmetric squates minus even')
print(sorted(squares.symmetric_difference(even)))


squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)

#keyys
try:
    squares.remove(8)
except KeyError:
    print("the item 8 is not a member of the set")

if squares.issubset(even):
    print("Squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

