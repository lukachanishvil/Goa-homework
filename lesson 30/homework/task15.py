def get_string_lengths(string_list):
    # Create a list of lengths of each string in the input list
    return [len(string) for string in string_list]

# Example usage
strings = ["apple", "banana", "cherry"]
lengths = get_string_lengths(strings)

print("Lengths of the strings:", lengths)

