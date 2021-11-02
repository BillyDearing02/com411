# lets the user know the program started
print("Program Started!")
# defines letter as an int
asciiCode = 0
# while loop to check if its only 1 letter
while asciiCode not in range(32, 126, 1):
    asciiCode = int(input("Please enter an ASCII code:\n"))
# prints the letter for whatever ASCII code the user put in
print(f"The character represented by the ASCII code {asciiCode} is: {chr(asciiCode)}")
print("Program Ended!")