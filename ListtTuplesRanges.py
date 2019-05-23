#sequence type
#list is a sequence of strings , infact a  sequence of lists
parrot_list= ["non pinin", "no more", "a stiff", "bereft of live"]
parrot_list.append("Hey New Parrot")

for state in parrot_list:
    print("This parrot is " , state )

even = [2,4,6,8]
odd= [1,3,5,7,9]
numbers = even + odd
numbers.sort()
print(numbers)

menu = []
menu.append(["egg", "spam", "Bacon"])
menu.append(["egg",  "Bacon"])
menu.append(["egg", "spam"])
menu.append(["egg",  "Bacon", "spam"])
menu.append(["egg", "Bacon","sausage", "spam"])
menu.append(["egg", "spam", "Bacon"])

print (menu)
for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingre in meal:
            print(ingre)