import jedi
import tabnine

# Get the current code and cursor position.
source_code = input("Enter some code: ")
cursor_position = (1, 0)

# Get code completion suggestions.
completions = get_code_completions(source_code, cursor_position)

# Display the code completion suggestions to the user.
print("Code completion suggestions:")
for completion in completions:
  print(completion.name)
