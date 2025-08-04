def count_char_frequency(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        frequency = {}
        for char in content:
            frequency[char] = frequency.get(char, 0) + 1
        
        print("Character frequencies in the file:")
        for char, count in sorted(frequency.items()):
            # For better readability, replace newline and tab characters with visible names
            display_char = char
            if char == '\n':
                display_char = '\\n (newline)'
            elif char == '\t':
                display_char = '\\t (tab)'
            elif char == ' ':
                display_char = "'space'"
            print(f"{display_char}: {count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Example usage:
filename = "sample.txt"
count_char_frequency(filename)
