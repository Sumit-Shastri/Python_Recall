# Find the most Frequent word in file.

"""
file = "file_50.txt"
count_dict = {}

with open(file, "r") as f:
    data = f.read()
    words = data.split()
    for word1 in words:
        count = 0
        for word2 in words:
            if(word2 == word1):
                count = count + 1
                words.remove(word1)
        count_dict[word1] = count

print(count_dict)

print("Most frequent is : ", max(count_dict, key = count_dict.get))

"""

from collections import Counter

with open("file_50.txt", "r") as f:
    words = f.read().split()

count_dict = Counter(words)

print(count_dict)
print("Most frequent is:", count_dict.most_common(1)[0])