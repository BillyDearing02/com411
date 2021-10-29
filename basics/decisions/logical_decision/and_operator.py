# user inputs
hear = input("What did I hear?\n\n")
see = input("What did I see?\n")
# if statement using and operator to check if the two conditions are met
if ("grrr" in hear.lower()) and ("two red eyes" in see.lower()):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")