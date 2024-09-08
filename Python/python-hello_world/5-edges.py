#!/usr/bin/python3

# Your program should be exactly 8 lines long
# word_first_3 should contain the first 3 letters of the variable word
# word_last_2 should contain the last 2 letters of the variable word
# middle_word should contain the value of the variable word without the first and last letters

word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
