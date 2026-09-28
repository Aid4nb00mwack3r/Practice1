# CS 1430 - Practice 1: Say It Again
#
# Ask for a whole number, then ask for a phrase, then print the phrase
# that many times. The steps are in README.md.
#
# Write your code below this comment.
number = int(input("Please select a number: "))
word = input("Please input a word you would like to use: ")
repeat = word * number
print(repeat)