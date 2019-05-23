#pickle drawback is that all objects have to be loaded back into memory
#uf your dealing with large set of objects loading that might not be realistic
#the shelve module provides a shelf, think of it like a dictionary and is
#stored in a file rather than in memory
#Think of them as a persistent dictionary


import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cidar"
    fruit['lemon'] = "a sour, orange, citrus fruit"
    fruit['grape'] = "a small, orange, citrus fruit"
    fruit['lime'] = "a sour, orange, citrus fruit"


    print(fruit["lemon"])
    print(fruit["grape"])

print(fruit)
