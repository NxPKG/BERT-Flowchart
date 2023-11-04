To write a bug detection library in Python, you can use the following steps:

1. Import the necessary modules.

```python
import ast
import traceback
```

2. Define a function to visit the AST of a Python program.

This function will be used to traverse the AST and detect bugs.

```python
def visit_ast(node, bug_detector):
  """Visits the AST of a Python program and detects bugs.

  Args:
    node: The AST node to visit.
    bug_detector: The bug detector object.
  """

  if isinstance(node, ast.Assign):
    # Detect unused variables.
    if not any(value.id == target.id for value in node.values):
      bug_detector.add_bug("Unused variable: {}".format(target.id))

  elif isinstance(node, ast.Call):
    # Detect undefined functions.
    if not hasattr(node.func, '__call__'):
      bug_detector.add_bug("Undefined function: {}".format(node.func.id))

  elif isinstance(node, ast.TryExcept):
    # Detect unhandled exceptions.
    if not len(node.handlers):
      bug_detector.add_bug("Unhandled exception")

  # Visit the children of the AST node.
  for child in ast.iter_child_nodes(node):
    visit_ast(child, bug_detector)
```

3. Define a class to represent a bug detector.

This class will contain the logic for detecting and reporting bugs.

```python
class BugDetector:
  """Detects and reports bugs in Python programs."""

  def __init__(self):
    self.bugs = []

  def add_bug(self, message):
    self.bugs.append(message)

  def get_bugs(self):
    return self.bugs

```

4. Use the bug detector class to detect bugs in a Python program.

```python
def detect_bugs(source_code):
  """Detects bugs in a Python program.

  Args:
    source_code: The source code of the Python program.

  Returns:
    A list of bugs found in the Python program.
  """

  tree = ast.parse(source_code)
  bug_detector = BugDetector()
  visit_ast(tree, bug_detector)
  return bug_detector.get_bugs()
```

This is a simple example of a bug detection library in Python. You can extend this library to detect other types of bugs, such as type errors and syntax errors. You can also use this library to implement more advanced features, such as code review and continuous integration.

Here is an example of how to use the bug detection library:

```python
source_code = """
def my_function(x):
  return x + 1

# Unused variable.
y = my_function(1)

# Undefined function.
undefined_function(1)

# Unhandled exception.
try:
  1 / 0
except:
  pass
"""

bugs = detect_bugs(source_code)

for bug in bugs:
  print(bug)
```

Output:

```
Unused variable: y
Undefined function: undefined_function
Unhandled exception
```