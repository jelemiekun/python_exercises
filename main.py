from io import TextIOWrapper


def file_read(path: str) -> None:
    file: TextIOWrapper = open(path, "rt")

    print(file.read())

    file.close()


def file_append(path: str, string: str) -> int:
    file: TextIOWrapper = open("dummy.txt", "at")
    line_added: int = file.write(f"\n{string}")
    file.close()
    return line_added


FILE_PATH: str = "dummy.txt"
file_read(FILE_PATH)
print(file_append(FILE_PATH, "MEOW!!!"))
file_read(FILE_PATH)
