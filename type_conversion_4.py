# Example values
string_num = "123"
string_float = "45.67"
integer_num = 89
float_num = 12.34
boolean_val = True

# Convert string to integer
int_from_str = int(string_num)
print(f"String to int: {string_num} -> {int_from_str} (type: {type(int_from_str)})")

# Convert string to float
float_from_str = float(string_float)
print(f"String to float: {string_float} -> {float_from_str} (type: {type(float_from_str)})")

# Convert integer to string
str_from_int = str(integer_num)
print(f"Int to string: {integer_num} -> '{str_from_int}' (type: {type(str_from_int)})")

# Convert float to integer (note: truncates decimal part)
int_from_float = int(float_num)
print(f"Float to int: {float_num} -> {int_from_float} (type: {type(int_from_float)})")

# Convert integer to float
float_from_int = float(integer_num)
print(f"Int to float: {integer_num} -> {float_from_int} (type: {type(float_from_int)})")

# Convert boolean to integer
int_from_bool = int(boolean_val)
print(f"Bool to int: {boolean_val} -> {int_from_bool} (type: {type(int_from_bool)})")

# Convert integer to boolean (0 is False, others are True)
bool_from_int = bool(0)
print(f"Int to bool: 0 -> {bool_from_int} (type: {type(bool_from_int)})")
bool_from_int = bool(42)
print(f"Int to bool: 42 -> {bool_from_int} (type: {type(bool_from_int)})")

# Convert string to boolean (non-empty string is True, empty string is False)
bool_from_str = bool("")
print(f"Empty string to bool: '' -> {bool_from_str} (type: {type(bool_from_str)})")
bool_from_str = bool("Hello")
print(f"Non-empty string to bool: 'Hello' -> {bool_from_str} (type: {type(bool_from_str)})")
