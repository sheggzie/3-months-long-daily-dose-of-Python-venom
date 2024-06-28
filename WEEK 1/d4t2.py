# Write a program that sorts a list of tuples based on the second element.

words = ('banana', 'cherry', 'melon', 'peach', 'kiwi', 'berry', 'mango', 'grape', 'plum', 'apple')

# sort the tuple by using lambda function to take second letter from each word and sort them with the "sorted" function 
sorted_words = sorted(words, key=lambda x: x[1])

print(sorted_words)