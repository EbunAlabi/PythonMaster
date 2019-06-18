#Imperative programming involves providing a series of instructions to follow in the defined order
#aims to combine data and the processes that run on that data into objects in a process called
#which is called encapsulation. OOP makes use of imperative programming within the methods used in
# that program.
#A self lighting cigarette, kinda demonstrate the concept of OOP quite well

#replacing one object with another one that performs the same task without having to bother oursleves with the details of hoe it perform s the task is
#central to the OOP approach


#Model of an electric kettle as a class
class Kettle(object):

     def __init__(self, make, price):
         self.make = make
         self.price = price
         self.on = False

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make
                                        , hamilton.price))




