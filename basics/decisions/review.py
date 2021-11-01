import random

room = input("What room should I go in?")

if "bedroom" in room.lower():
    light = input("Should I switch the light on?")
    if light.lower() == "yes":
        bObject = input("There is a bed, a cupboard and a shelf in the bedroom. Where should I go to?")
        if "bed" in bObject.lower():
            print("The bed is not made up. The pillows have been slashed and the pillow stuffing litters the bed.")
        elif "cupboard" in bObject.lower():
            if "open" in bObject.lower():
                open = True
            else:
                cOpen = input("The cupboard is old. a layer of dust covers the top. Should I open it?")
                if "yes" in cOpen:
                    open = True
                else:
                    open = False
            if open == True:
                book = input(
                    "I open the cupboard. The door is a little stiff but it eventually opens with some force.\n"
                    "I find a worn out book with a bookmark inside. Should I open it?")
                if "open" in book.lower() and "bookmark" in book.lower():
                    print("The books pages have been cut out in a dagger-like shape starting at this page.")
                elif "open" in book.lower() or "yes" in book.lower():
                    responseList = "The book seems to have a dagger-like cutout in the centre. You figure out that it starts at where the bookmark is.","It appears to just be a normal book."
                    response = random.choice(responseList)
                    print(response)
    else:
        print("You begin walking, stumble over and bash your brains out on the kitchen cabinet. You are now part of the crime scene")

elif "kitchen" in room.lower():
    light = input("Should I switch the light on?")
    if light.lower() == "yes" or "switch" in light.lower() and "light on" in light.lower():

    else:
        print("You begin walking, stumble over and bash your brains out on the kitchen cabinet. You are now part of the crime scene")