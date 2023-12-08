import sys


# Getting commandline Arguements

def get_commandline_arguements():
    print(type(sys.argv))
    program_name = sys.argv[0]
    print(f"Program Name: {program_name}")
    if (len(sys.argv) > 2):
        for arg in sys.argv[1:]:
            print(arg)
    else:
        print("To few arguements")


get_commandline_arguements()


def get_commandline_arguements_two():
    if (len(sys.argv) < 2):
        print("Too few arguements")
        sys.exit()
    elif (len(sys.argv) > 2):
        print("To many arguements")
        sys.exit()
    print(f"Hello, {sys.argv[1]}")


# get_commandline_arguements_two()


# Getting the path of the file that you are working on
print(f"Current file path: {sys.path}")
