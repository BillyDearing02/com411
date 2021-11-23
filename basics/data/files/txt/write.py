# imports os module
import os


# sorts the books
def search(f_path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(f_path) as file:
        data = file.read()
        lines = data.split("\n")
        for line in lines:
            if line.startswith("Section"):
                sections = sections + line + "\n"
            else:
                books = books + line + "\n"

    write = f"{sections}\n\n{books}"

    return write


# writes to the file
def save(f_path, text):
    print("Saving...")
    print(text)
    with open(f_path, "w") as file:
        file.write(text)
    print("Done!")


# runs the program
def run():
    f_path = "books.txt"
    f_name = "section-books.txt"
    write = search(f_path)
    save(f_name, write)


# begins the program
if __name__ == "__main__":
    run()