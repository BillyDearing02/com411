# gets what room the user wants to look in
look = input("Where should I look?")
# checks if bedroom was in the user input
if "bedroom" in look.lower():
    where = input("Where in the bedroom should I look?")
    # use of a nested if statement to check if cupboard was used in the user input
    if "cupboard" in where.lower():
        print("Found some mess but no battery.")
# checks if bathroom was in the user input
elif "bathroom" in look.lower():
    where = input("Where in the bathroom should I look?")
    # use of a nested if statement to check if bathtub was used in the user input
    if "bathtub" in where.lower():
        print("Found a rubber duck but no battery")
# checks if lab was in the user input
elif "lab" in look.lower():
    where = input("Where in the lab should I look?")
    # use of a nested if statement to check if table was used in the user input
    if "table" in where.lower():
        print("Yes! I found my battery!")
# makes sure the code doesnt break if the user doesnt input the correct rooms
else:
    print("That room doesnt exist")