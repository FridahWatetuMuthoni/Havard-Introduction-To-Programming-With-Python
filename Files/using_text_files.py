
def get_user_input():
    names = []
    for _ in range(3):
        name = input("What's your name: ")
        names.append(name)
    return names


def sorting_storing_names(names):
    sorted_names = sorted(names)
    with open("./Files/names.txt", 'a') as file:
        for name in sorted_names:
            file.write(f"{name} \n")
    return sorted_names


# sorting_storing_names(get_user_input())


def reading_file():
    file_path = "./Files/names.txt"
    with open(file_path, 'r') as file:
        for line in file:
            print(f"Hello, {line}", end='')


def reading_and_sorting():
    file_path = "./Files/names.txt"
    names = []
    with open(file_path, 'r') as file:
        for line in file:
            names.append(line.rstrip())
    sorted_names = sorted(names)
    for name in sorted_names:
        print(name)


# reading_and_sorting()
