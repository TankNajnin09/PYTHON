#write content in a file
def write_to_file(filename, content):
    """Write content to a file (overwrite if file exists)."""
    with open(filename, 'w') as file:
        file.write(content)
    print("Content written to file.")

#read content in a file
def read_file(filename):
    """Read entire content of a file."""
    with open(filename, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)

#main part
filename = "sample.txt"
content = "Hello World... \nThis is demo file...\n"

write_to_file(filename, content)
read_file(filename)
