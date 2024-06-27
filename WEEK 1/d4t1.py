# Create a script to count the frequency of words in a text.

text = """
In the heart of bustling cities, where concrete and steel dominate the skyline, urban gardens are sprouting as green oases. These patches of greenery not only beautify the urban landscape but also offer numerous benefits to city dwellers. Urban gardening is more than a trend; it's a movement that brings people closer to nature, promotes sustainability, and enhances community well-being.
"""
words = text.split()
frequency = {}

def word_frequency_counter():
    for i in words:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    print(frequency)
    
word_frequency_counter()