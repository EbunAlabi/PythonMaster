timesTable = "1 times 2 is 2", "2 times 2 is 4"


with open("sampleText.txt", 'a') as chal:
    for i in range(2,13):
        for j in range (1,13):
            print ("{1:>2} times {0} is {2}".format(i,j, i * j), file=chal)
        print("-" * 20, file=chal)
