from curses.ascii import isalnum

char = input("Enter a character: ")

if len(char)>1:
  print("Enter only one character")
  exit()

"""Checks if the input character is a vowel (a, e, i, o, u) in either uppercase or lowercase.
"""


if(char=="a" or char=="A" or char=="e" or char=="E" or char=="i" or char=="I" or char=="o" or char=="O" or char=="u" or char=="U"):
  print("Vowel")
elif(char.isdigit()):
  print("is Number")
else:
  print("Consonant")
