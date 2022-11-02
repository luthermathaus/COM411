def display_chars(file_path, num_of_chars):
    with open(file_path) as file:
        print(file.read(num_of_chars))


def display_line(pathfile):
    with open(pathfile) as file:
        print(file.readline())


def display_text(patty_fi):
    with open(patty_fi) as file:
        print(file.read())



def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
