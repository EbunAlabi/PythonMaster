
import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cidar"
fruit['lemon'] = "a sour, orange, citrus fruit"
fruit['grape'] = "a small, orange, citrus fruit"
fruit['lime'] = "a sour, orange, citrus fruit"


print(fruit["lemon"])
print(fruit["grape"])


fruit["lime"] = "great with tequila"

for snack in fruit:
    print(snack+ ": " + fruit[snack])


while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key =="quit":
        break


    if shelf_key in fruit:
        description = fruit.get(shelf_key, "We are closed yayyyy" + shelf_key)
        print(description)
    else:
        print("We dont have a " + shelf_key)



fruit.close()
print(fruit)