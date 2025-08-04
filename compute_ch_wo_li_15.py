def file_statistics(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        num_words = 0
        num_chars = 0

        for line in lines:
            num_chars += len(line)
            words_in_line = line.split()
            num_words += len(words_in_line)

        print(f"File statistics for '{filename}':")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Example usage:
filename = "sample.txt"
file_statistics(filename)
