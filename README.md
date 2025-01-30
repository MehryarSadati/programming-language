# Simple Programming Language

This repository contains a simple programming language implemented using ANTLR4 and Python. The language's grammar is defined in `Grammar.g4`, and the corresponding lexer, parser, and visitor are generated accordingly.

## Getting Started

### Prerequisites

- **Python 3.x**
- **ANTLR4 Tool**: Required for generating lexer and parser from the grammar file.

### Installation

1. **Clone the Repository**:

  ```bash
  git clone https://github.com/MehryarSadati/programming-language.git
  cd programming-language
  ```
2. **Install Dependencies**:

  ```bash
  pip install -r requirements.txt
  ```

3. **Install ANTLR4**:

    Download ANTLR4 Tool: ANTLR4 Complete JAR
    Move the JAR File: Place it in the project directory.

    For convenience, you can add an alias to your shell profile.

4. **Generate Lexer, Parser and Visitor (with -no-listener flag)**:
  ```bash
  antlr4 -Dlanguage=Python3 -no-listener -visitor Grammar.g4
  ```

5. **Run programs written in this language using the interpreter by executing script.py**:
  ```bash
  python3 script.py
  ```


# Syntax

## Basic Structure
The language supports variable assignments, print statements, and conditional statements. Each statement should be on a new line.

## Variables and Data Types
- **Identifiers**: Variable names can contain letters, numbers, and underscores
  - Must start with a letter or underscore
  - Case-sensitive
  - Examples: `myVar`, `counter1`, `_temp`

- **Data Types**:
  - Numbers: Integer values (e.g., `42`, `100`, `0`)
  - Strings: Text enclosed in double quotes (e.g., `"Hello World"`)

## Operators
### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `^` Exponentiation

### Comparison Operators
- `<` Less than
- `>` Greater than
- `==` Equal to
- `!=` Not equal to

## Statements

### Assignment
  Variables are assigned using the `:=` operator:
  ```
  variable := value
  ```
Example:
  ```
  x := 42
  message := "Hello"
  ```

### Print Statement
Output values using the `print` keyword:
  ```
  print expression
  ```
Example:
  ```
  print x
  print "Hello World"
  print 42
  ```

### Conditional Statement
If-else statements follow this syntax:
  ```
  if condition statement
  if condition statement else statement
  ```
Example:
  ```
  if x > 10 print "Greater than 10"
  if x == 5 print "Five" else print "Not five"
  ```

## Examples

Here are some complete code examples:

  ```
  x := 42
  print x

  if x > 20 print "x is greater than 20" else print "x is less than or equal to 20"

  message := "Hello"
  print message

  if message == "Hello" print "Greeting detected"
  ```

## Notes
- Each statement must be on a new line
- Whitespace is ignored except for newlines
- String literals must use double quotes
- Comments are not supported in the current version