#ordered set of data
#similar to list
#immutable; cant be changed : major doff from list
#tuples are suppose to hold heterogeneous items unlike lists
#lists tend to hold homogeneous items

a = b= c = 12
print(c)
a,b= 12,13
print(b)
a,b = b, a
print("a is {}".format(a))
print("b is {}".format(b))

#album tuples
welcome = "Welcome to my life", "Alice Copper", 1927
bad = "Bad Company" "Bad Company", 1972
imelda = "More Mayhem", "Itlian May", 2011
budgie = "Nightflight", "Budgie", 1981
metallica = "Rid ethe lightning", "Metallica", 1984

metallic2 = ["Rid ethe lightning", "Metallica", 1984]
print(metallic2)
title, artist, yerar = imelda
print(title)
print(artist)
print(yerar)

listvstup = ("hey", 34, 'yasa')
print(listvstup)






#challenge
imeldaT = "More Mayhem", "Itlian May", 2011, ((1, "Pulling the rug"),(2, "Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz"))
#extract fields
title,artist,year, tracks = imeldaT

for song in tracks:
    print("\t", song )



for char in imeldaT:
    print(char)
for tracks in imeldaT[3]:
    print(tracks)




