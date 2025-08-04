def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()

        with open(destination_file, 'w') as dest:
            dest.write(content)

        print(f"Contents copied from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except IOError as e:
        print(f"IO error occurred: {e}")

# Example usage:
source = "sample.txt"
destination = "copy.txt"

copy_file(source, destination)
