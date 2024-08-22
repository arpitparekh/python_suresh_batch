# Write a program to check whether a character is in the alphabet or not.

from curses.ascii import isalpha


char = input("Enter a character: ")

if char.isalpha():
  print("Alphabet")
else:
  print("Not an alphabet")
