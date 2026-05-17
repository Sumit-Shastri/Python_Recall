# Count frequencies of elements in Dictionary

def CountFrequency(d):

    frequency = {}

    for i in d.values():
        counter = 0
        for j in d.values():
            if(i == j):
                counter = counter + 1
                frequency[i] = counter
    
    print(frequency)

data = {1:23, 2:34, 3:23, 4:56, 5:63, 6:34, 7:34, 8:65}
print(data)

CountFrequency(data)

        

