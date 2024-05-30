name = "Julius"
age = 30
celebration_message = f"Let's celebrate {name}'s {age}th birthday!"

#accessing a string by indexing and slicing
indexing = celebration_message[6:]

#By spliting
text = "This is a string with examples."
words = text.split()  # Split by default whitespace separator
#print(words)

text_with_spaces = "   Extra spaces at the beginning and end.  "
trimmed_text = text_with_spaces.strip()
print(trimmed_text)
original_text = "This is a string with is"
replaced_text = original_text.replace("1s", " an", 1)  # Replace only the first occurrence
#print(replaced_text)

#print(celebration_message)