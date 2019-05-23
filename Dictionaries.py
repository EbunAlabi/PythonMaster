#lists are used to store similar items
#sets are similar to lists, but you cant access individual indexex
#dict are ordered and accessed by key value pairs
#split amd join will be introduced - fuctions

fruit = {"orange": "a good orange citrus juice",
         "apple": "good fr making cider",
         "lemon": "good for lemonade",
         "grape": "a smal, sweet fruit groing in bunches",
         "lime": "a sour, green citrus growing in bunches"}

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmm, Lovely",
       "spinach": "can i have some more fruits please"}

print(veg)

#cobine two dictionaries together
veg.update(fruit)
print(veg)
nice_copy = veg.copy()
nice_copy.update(fruit)
print(nice_copy)

print(fruit)
print(fruit["lemon"])

fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["pear"] = "an odd shaped apple and great with tequiila"
del(fruit["lemon"])
print(fruit)

for f in sorted(fruit.keys()):
    print (f + " - " + fruit[f])

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

