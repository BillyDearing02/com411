# lets the user know the program started
print("Program Started!")
# defines letter as a string
letter = ""
# while loop to check if its only 1 letter
while len(letter) != 1:
    letter = input("Please enter a letter:\n")
# prints the ASCII code for whatever letter the user put in
print(f"The ASCII code for {letter} is: {ord(letter)}")
print("Program Ended!")

