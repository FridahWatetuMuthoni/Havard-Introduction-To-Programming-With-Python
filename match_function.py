name = "Draco"


def determine_house_one(name):
    if (name == "Harry"):
        print("Gryffindor")
    elif (name == "Hermione"):
        print("Gryffindor")
    elif (name == "Ron"):
        print("Gryffindor")
    elif (name == "Draco"):
        print("Slytherin")
    else:
        print("Who?")


# determine_house_one(name)

def determine_house_two(name):
    if (name == "Harry" or name == "Hermione" or name == "Ron"):
        print("Gryffindor")
    elif (name == "Draco"):
        print("Slytherin")
    else:
        print("Who?")


# determine_house_two(name)

def determine_house_three(name):
    match name:
        case "Harry":
            print("Gryffindor")
        case "Hermione":
            print("Gryffindor")
        case "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")


# determine_house_three(name)


def determine_house_four(name):
    match name:
        case "Harry" | "Hermoine" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")


determine_house_four(name)
